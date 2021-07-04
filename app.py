import datetime
import json
import os

from flask import Flask, request, Response, render_template, jsonify, send_from_directory, g, make_response
from layers import parse_data, init_project  # get_parsed_data是所有的入口
from settings import PROJECT   # 导入项目名称、内置extensions
from flask_caching import Cache

from utils.router_type import ReConverter

project_settings = __import__(f"settings.{PROJECT}", globals(), locals(), ["DP_CONTAINER", "DP_ROOT"])  # 导入前端配置

DP_CONTAINER, DP_ROOT = project_settings.DP_CONTAINER, project_settings.DP_ROOT

app = Flask(__name__, template_folder=os.path.join(DP_CONTAINER, DP_ROOT), static_folder=os.path.join(DP_CONTAINER, DP_ROOT))
app.url_map.converters["re"] = ReConverter
# 读取项目配置
app.config["PROJECT"] = PROJECT
app.config.from_object(f"settings.global")
app.config.from_object(f"settings.{PROJECT}")
app.config.from_object(f"settings.{PROJECT}.init_dicts")
app.config.from_object(f"settings.{PROJECT}.apis_dispatch")
app.config.from_object(f"settings.{PROJECT}.apis_plugins")
app.config.from_object(f"settings.{PROJECT}.auth")
# app.config.from_object(f"settings.{PROJECT}.qh_info")

cache = Cache()
cache.init_app(app)
cache_timeout = app.config.get("CACHE_TIMEOUT", 60 * 60 * 24)
# cache_prefix_func = app.config.get("CACHE_PREFIX_FUNC")
init_project.init_project()  # 初始化项目

############################### /api/开头的接口路由 ###############################
# 核心数据接口路由
@app.route('/api/<string:realm>/<string:index>/', methods=['GET'])
@app.route("/api/<string:realm>/", methods=['GET'])
@cache.cached(timeout=cache_timeout, key_prefix=lambda : request.cookies.get(app.config.get("LEVEL_AUTH_COOKIE"), "") + ":" + request.full_path + str(datetime.datetime.now().day))
def data_index_api(realm, index=""):
    request_args = dict(request.args)
    # 兼容可能的解析请求参数时得到列表：部署时使用的anaconda3中的环境会解析成列表
    request_args_str = {i: request_args[i] for i in request_args if isinstance(request_args[i], str)}
    request_args_list = {i: request_args[i][0] for i in request_args if isinstance(request_args[i], list)}
    request_args = {**request_args_list, **request_args_str}

    # 前端调试模式
    g.debug = request_args.get("debug", "false")

    # 得到解析的结果
    # convert层直接返回封装好的结果
    # 如果走插件过程，需要手动补充code和msg
    code, msg, parsed_data = parse_data(realm, index, request_args)
    if code not in [200, 201, 202, 203, 999]:  # 201空数据   202  插件过程   203api分发时直接是字典   204不需要变成json,原始字串
        parsed_data = {"code": code, "msg": msg, "data": {}}
    else:
        if code == 202:
            parsed_data["code"] = 202
            parsed_data["msg"] = "plugin_mode"
        elif code == 203:
            parsed_data["code"] = 203
            parsed_data["msg"] = "test data in apis_dispatch"
        # elif code == 204:
        #     parsed_data["code"] = 204
        #     parsed_data["msg"] = "raw_data"

    data = json.dumps(parsed_data, default=lambda x: int(x))
    # response = Response(response, mimetype='application/json')
    response = make_response(data)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    response.headers['content-type'] = 'application/json'
    if app.config.get("LEVEL_AUTH"):
        if not request.cookies.get(app.config.get("LEVEL_AUTH_COOKIE")) and g.get("level_auth"):
            response.set_cookie(app.config.get("LEVEL_AUTH_COOKIE"), g.level_auth)
    return response


# dead json
@app.route("/api/<string:realm>/<string:dp_dir>/<path:filename>")
def get_deadjson(realm, dp_dir, filename):
    return send_from_directory(os.path.join(app.root_path, DP_CONTAINER, DP_ROOT, dp_dir, "data"), filename)


############################### 前端路由 ###############################
########################### 具体大屏路径开头的 ###########################
dp_dirs = [app.config[i] for i in dict(app.config) if i.startswith("DP_DIR")]
dp_urls = [app.config[i] for i in dict(app.config) if i.startswith("DP_URL")]
dp_url_re = "'"+"|".join(dp_urls)+"'"


# index.html【兼容一个大屏和多个大屏】
@app.route(f"/<re({dp_url_re}):dp>/")  # 路径只有一个值时：需要满足自定义的大屏路径
def get_index(dp):
    from layers.api_gateway import authentication
    authentication(request.args.copy())  # 将level_auth写入g，如果有的话
    index_path = f"{dp}/index.html" if len(dp_dirs) > 1 else "index.html"
    resp = render_template(index_path)
    resp = Response(resp)
    if app.config.get("LEVEL_AUTH"):
        resp.set_cookie(app.config.get("LEVEL_AUTH_COOKIE"), g.get("level_auth", ""))
    return resp


# 多个大屏时走下面的请求
# url.js
@app.route(f"/<re({dp_url_re}):dp>/url.js")
def get_urljs(dp):
    return send_from_directory(os.path.join(app.root_path, DP_CONTAINER, DP_ROOT, dp), "url.js")

# html静态页面
@app.route(f"/<re({dp_url_re}):dp>/<re('.*\.html'):html>")
def get_html(dp, html):
    return send_from_directory(os.path.join(app.root_path, DP_CONTAINER, DP_ROOT, dp), html)


# static resource (static/font/map)
@app.route(f"/<re({dp_url_re}):dp>/<re(r'data|font|map|static|js|image|css'):resource_type>/<path:filename>")
def get_static(dp, resource_type, filename):
    return send_from_directory(os.path.join(app.root_path, DP_CONTAINER, DP_ROOT, dp, resource_type), filename)


# favicon.ico
@app.route(f"/favicon.ico")  # 路径只有一个值时：需要满足自定义的大屏路径
def favicon():
    return send_from_directory(os.path.join(app.root_path, DP_CONTAINER), "favicon.ico")


############################### 定时刷新任务路由 ###############################
# 定时刷新任务的路由
@app.route("/refresh/")
def refresh_all():
    refresh = __import__(f"settings.{PROJECT}.refresh", globals(), locals(), ["refresh"])  # 导入前端配置
    refresh.refresh()
    return jsonify({"code": 200, "msg": "done", "data": {}})

############################### 测试任务路由 ###############################


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3389, debug=app.config.get("DEBUG"))
