## 接口程序代码

### 整体说明

#### 代码说明

| 功能层                    | 功能说明                                                     |
| ------------------------- | ------------------------------------------------------------ |
| 网关层：api_gateway       | 权限校验+指标分发(dispatch)                                  |
| 拆分层：get_splited_apis  | 一个接口拆分成多个接口                                       |
| 解析层：get_parsed_api    | 将简写还原（如 year=now）                                    |
| 查询层：get_dataframe     | 查询数据库（普通模式/sql插件模式/custom插件模式）            |
| 补充层：makeup_dataframe  | 排序补零+limit                                               |
| 转换层：convert_dataframe | 转换成前端需要的格式（value/name-value/name-stack-value/embedding） |

#### 文件目录

- bin：存放二进制启动脚本目录
- client：存放各项目的前端目录
- layers：核心功能代码：分六层
- libs：系统级模块
- refresh：系统级定时刷新模块          未开发完成
- settings：存放各项目的配置目录
- utils：存放辅助功能代码目录
- app.py：入口文件
- env_test.py：数据库配置测试
- uwsgi.ini： centos的生产环境启动
- win-server.py： windows生产环境启动

### 项目开发

#### 1. 复制一份已有项目的配置文件

如：`settings/gdxf`   --->   `settings/newProject`

#### 2. 修改配置

配置文件说明如下：文件路径相对于  `settings/newProject/`

| 配置文件           | 说明                                                         |
| ------------------ | ------------------------------------------------------------ |
| `custom文件夹`     | 存放custom自定义模式下需要的脚本（特殊接口）                 |
| `extensions文件夹` | 存放项目自定义的计算方式的脚本                               |
| `init_files文件夹` | 存放记录有联动列的文件（如 省市县的联动关系） 补零时使用     |
| `refresh文件夹`    | `__init__.py` 中定义的方法 会在访问  ip:port/refresh时调用   |
| `report文件夹`     | 生成报告需要的脚本（特殊接口）   此功能暂未开发，生成报告使用的是自定义接口 |
| `__init__.py`      | 项目的主要配置文件，包括数据库连接，缓存，权限等           **使用详解见附录** |
| `apis_dispatch.py` | 指标分发配置，对接口进行包装，方便后期调试                   |
| `apis_plugins`     | 指标的特殊写法，包括sql和custom两种模式                      |
| `auth.py`          | 权限代码配置，访问分权限时使用                               |
| `init_dicts.py`    | 指标的初始化配置（没有联动关系的指标）                       |
| `param_trans.py`   | 项目特殊的参数转换方法（如请求 shij_02=北京市海淀区时，改成 shij_02=海淀区） |

#### 3. 开发接口

- 指标开发分为两种模式：普通模式/插件模式(custom/sql)

  - 普通模式：基本前端请求参数见附录，其他高级参数见 `settings/global.py`
    - value格式：只有一个数
    - name-value格式：name/value 的列表
    - name-stack-value格式：两层前套
    - embedding格式：目前应用只有多层前套的旭日图

  - 插件模式：在 `apis_plugins.py` 中指定
     - sql模式：支持直接写sql，目前主要用于列表的反查
     - custom模式：支持自定义写法，目前主要用于报告的生成这种大面积的文本

- 指标编写分为两种模式：直接写接口/dispatch模式

  - 直接写接口：用普通模式或者插件模式写接口，接口会较为复杂
  - dispatch分发：在`apis_dispatch.py`中给直接写的接口起名字，相当于进行一次接口包装
    - 优势：之后可以在后台直接修改具体的接口，不经过前端
    - 优势：可以利用已完成的接口生成工具，生成接口文档给前端实现

#### 4. 生成接口文档

**注意：需要按照apis_dispatch的方法写接口**

1. 参考重庆项目的格式编写 `apis_dispatch.py`文件
2. 将 `apis_dispatch.py` 文件拷贝至dev_tools/目录下
3. 修改`dev_tools/dispatch2front.py`  
   - 输入文件文件名
   - 输出文件文件名
4. 执行`python dispatch2front.py` 生成md文档

#### 5. 集成前端

- 获取前端打包好的压缩包文件

- 解压压缩包后，修改`url.js`文件 如下

  ~~~js
  // 线上环境URL，可根据实际情况自行修改
   const $URL = {
       BASE_API: '/hbxfdp', //部署地址               修改这一行：直接从/开始
       // BASE_API: './', //部署地址
       DATA_API: '/api/xf',   //接口地址             修改这一行：直接从/开始
       JSON: false //true:本地json数据、false:接口数据
   }
  ~~~

- 在`settings/newProject/__init__.py`中修改大屏的访问路径和地址

  `__init__.py`中的DP_URL变量需要和 前端的`url.js`文件中的`BASE_API`的路径保持一致

### 项目启动

#### 1. 确认安装envs中的所有依赖

#### 2. 修改目标项目

- 修改：`settings/__init__.py`   中的 `PROJECT` 变量值为当前项目
- 删除无关项目：client文件夹中的无关项目 & settings文件夹中的无关项目

#### 3. 修改数据库连接

- 在`settings/newProject/__init__.py`中修改FX_DB, ZB_DB的值
  - newProject：当前项目
  - FX_DB, ZB_DB：输入库和输出库
- 注意如果密码中包含特殊值时的写法：需要使用  `urllib.parse.unquote_plus`

#### 4. 检查数据库连接

`/root/anaconda3/bin/python3 env_test.py`

- 若数据库连接成功，返回数据库的URL
- 若数据库连接失败，报错退出

#### 5. 启动代码程序后台运行

##### 开发模式`python3 app.py`

- 默认端口3389
- 查看大屏需要在端口后拼接大屏路径：如127.0.0.1:3389/hbxfdp

##### 生产模式[centos]

- 修改 `uwsgi.ini` 中的端口号和项目路径
- 启动：`/root/anaconda3/bin/uwsgi --ini uwsgi.ini`
- 重启：`/root/anaconda3/bin/uwsgi --reload uwsgi.pid`
- 停止：`/root/anaconda3/bin/uwsgi --stop uwsgi.pid`

##### 生产模式[windows]

- 修改  `win-server.py`  中的端口号
- 启动：`/root/anaconda3/bin/python3 win-server.py`

### 其他说明

#### 接口状态码

- 200 正常数据
- 201 空数据
- 202 自定义查询过程，需要走插件流程
- 400 报错

### 附录

#### `__init__.py` 配置参数详解

| 配置类别   | 配置项                   | 说明                   | 建议与备注                         |
| ---------- | ------------------------ | ---------------------- | ---------------------------------- |
| 数据库     | FX_DB                    | 分析库连接url          | 注意特殊密码的写法                 |
|            | ZB_DB                    | 指标库连接url          |                                    |
| 缓存       | CACHE_TYPE               | 缓存类型               | "null" 无缓存    "redis" redis缓存 |
|            | CACHE_REDIS_HOST         | 数据库地址             |                                    |
|            | CACHE_REDIS_PORT         | 数据库端口             |                                    |
|            | CACHE_REDIS_DB           | 数据库索引             |                                    |
|            | CACHE_REDIS_PASSWORD     | 数据库密码             |                                    |
|            | CACHE_TIMEOUT            | 过期时间               | 单位：秒                           |
| 前端       | BASE_DIR                 | 项目根路径             | 不要修改                           |
|            | SETTINGS_DIR             | 配置的根据经           | 不要修改                           |
|            | DP_CONTAINER             | 大屏的根路径           | 不要修改                           |
|            | DP_ROOT                  | 大屏文件夹名           | 如果没有子大屏，DP_DIR=""          |
|            | DP_DIR                   | 子大屏文件夹           | 多个大屏使用 DP_DIR_1 区分         |
|            | DP_URL                   | 子大屏访问url          | 多个大屏使用 DP_URL_1 区分         |
|            | FILE_URL                 | 大屏静态资源url        | 头像或生成的报告等                 |
|            | FILE_PATH                | 大屏静态资源路径       | 头像或生成的报告等                 |
| 权限       | LOGIN_AUTH               | 为True时，要求登录     | 布尔值                             |
|            | LEVEL_AUTH               | 为True时，开启权限     | 需要配合 LEVEL_AUTH_COOKIE         |
|            | LEVEL_AUTH_PARAM         | 参数中控制权限的参数   |                                    |
|            | LEVEL_AUTH_COOKIE        | cookie中控制权限的参数 | 写到cookie中带给前端               |
|            | LEVEL_AUTH_ENCRYPT       | 权限参数是否加密       | 尚未开发                           |
| 参数配置   | CUS_SPECIAL_PARAMS       | 特殊参数的校验         |                                    |
|            | CUS_PARAM_TRANS          | 属于该项目的参数转换   |                                    |
| 随机化配置 | RANDOM_OR_ZERO           | 为空时随机化还是0填充  | **测试时选择 "RANDOM"**            |
|            | EFFICIENT_DIGITS         | 随机化保留的小数位数   |                                    |
|            | RANDOM_INT_LOWER         | 随机化的整数上限       |                                    |
|            | RANDOM_INT_UPPER         | 随机化的整数下限       |                                    |
| 返回数据   | NOTABLE_ERROR            | 没有表时 是否报错      | **常配合 RANDOM使用**              |
|            | NOCOLUMN_ERROR           | 没有字段时 是否报错    | **常配合 RANDOM使用**              |
|            | SIGNIFICANT_DIGITS       | 小数位数               |                                    |
|            | TIME_FORMAT              | 时间格式化             | 注意特殊密码的写法                 |
|            | DATE_START               | 精确的时间限制         | 一般接口参数中只有日期             |
|            | DATE_END                 | 精确的时间限制         | 同上                               |
|            | CUS_VALUE_MAP            | 分析库连接url          | 一般用于省市的全称转缩写           |
|            | VALUE_MAP_FOR_PLUGIN_SQL | 转换plugin模式中的数据 | 一般是表格类型的数据               |
|            | INITIALIZATION_FILE_PATH | 有联动关系列的初始化   | 不要修改                           |
|            | INITIALIZATION_FILE_SEP  | 有联动关系列的初始化   | 不要修改                           |
|            | CUS_EXTENSIONS           | 属于该项目的计算方式   |                                    |
|            | RELATION_COLS            | 有联动关系的列组合     |                                    |
|            | DISABLE_FULL_WHEN_NAME   | 不进行补零的情况       | 注意特殊密码的写法                 |
|            | DISABLE_FULL_WHEN_VALUE  | 不进行补零的情况       | 注意特殊密码的写法                 |
| 数据预测   | PREDICT_MIN_DATA         | 预测需要的最少样本     | 否则预测均值                       |
|            | PREDICT_MIN_MULTI_DATA   | 预测需要的最少倍数     | 如预测7天，需要7*3天               |
|            | PREDICT_STRATEGY_FILL_NA | 预测时的补零策略       |                                    |
| 调试       | DEBUG                    | 调试开关               | 仅python app.py 启动时有效         |

#### 前端基本参数详解

| 参数         | 说明                                          |
| ------------ | --------------------------------------------- |
| gd_id | 插件模式下的接口入口 |
| table        | 此次请求需要查询的数据表                      |
| db_engine    | 指定的数据库   zb_db 或 fx_db                 |
| name         | 作为name的列                                  |
| value        | 作为value的列                                 |
| stack        | 前套指标的列                                  |
| direct_order | 数据库查询时，进行的排序                      |
| direct_limit | 数据库查询时，进行的数量限制     提高查询速度 |
| order        | 最终返回时进行的排序                          |
| limit        | 最终返回时进行的数量限制                      |
| param_trans  | 指定参数变换                                  |
| transformer  | 指定特殊计算方式                              |
| full         | 是否排序补零                                  |
| extra_index  | 一个接口多指标时指定额外指标的参数            |
| main_name    | 一个接口多指标时指定额外指标的名字            |
| debug    | 在页面调试接口  debug=true 查看分发的指标     debug=1查看解析后的参数 |