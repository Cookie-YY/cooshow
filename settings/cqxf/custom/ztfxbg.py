# -*- coding: utf-8 -*-
import datetime
import os

import pypandoc


def search_sb(conn, sql, value1, value2):
    try:
        pre = '<span class="index" style="color: #F2DE58;">'
        post = '</span>'
        cur = conn.cursor()
        sql1 = sql % value1
        cur.execute(sql1)  # 查询数据
        res = cur.fetchall()  # 获取结果
        total_num = res[0][0]
        sql2 = sql % value2
        cur.execute(sql2)  # 查询数据
        res = cur.fetchall()  # 获取结果)
        last_total_num = res[0][0]
        if last_total_num == None:
            total_num = str(int(total_num)) if total_num != None else "0"
            tb = "0.00"
            total_num, tb = f'{pre}{total_num}{post}', f'{pre}{tb}{post}'
        else:
            tb = int(total_num) / last_total_num  # 同比
            from app import app
            tb = round(tb, app.config.get("SIGNIFICANT_DIGITS", 4))
        return f'{pre}{total_num}{post}', f'{pre}{tb}{post}'
    except Exception as e:
        print(e)


def run(start, end, zt, zb_pymysql, **kwargs):
    s_time = start
    e_time = end
    sql_qhauth_sheshixj = kwargs.get("sql_qhauth_sheshixj")
    sql_qhauth_qh = kwargs.get("sql_qhauth_qh")
    sql_qhauth_djjg_qh = kwargs.get("sql_qhauth_other").get("djjg_qh")
    qh = sql_qhauth_qh.replace("'", "").replace("qh","").replace("=","").strip()
    s_time1 = datetime.datetime.strptime(s_time, "%Y-%m-%d %H:%M:%S")
    e_time1 = datetime.datetime.strptime(e_time, "%Y-%m-%d %H:%M:%S")
    str1 = s_time1.strftime("%Y{y}%m{m}%d{d}").format(y="年", m="月", d="日")
    str2 = e_time1.strftime("%Y{y}%m{m}%d{d}").format(y="年", m="月", d="日")
    last_s_time = str(s_time1.year - 1) + s_time[4:]
    last_e_time = str(e_time1.year - 1) + e_time[4:]

    total_time = str1 + "至" + str2  # 具体时间
    now_time = datetime.datetime.now().strftime("%Y-%m-%d")

    sql = "select sum(xfjc) from xf_xfj_cd_zt_xj_xfjc where zt='"+zt+"' and `day` >= '%s' AND `day` <= '%s' AND" + f" {sql_qhauth_sheshixj} "
    sql_xfxs = "select sum(xfjc) from xf_xfj_cd_zt_xj_xfxs_xfjc where zt='"+zt+"' and xfxs='%s' AND `day` >= '%s' AND `day` <= '%s' AND" + f" {sql_qhauth_sheshixj} "
    sql_xfxs_wx = "select sum(xfjc) from xf_xfj_cd_zt_xj_xfxs_xfjc where zt='"+zt+"' and xfxs!='来信' and xfxs !='来访' AND `day` >= '%s' AND `day` <= '%s' AND" + f" {sql_qhauth_sheshixj} "
    sql_djjg = "select sum(xfjc) from xf_xfj_cd_zt_qh_djjg_xfjc where zt='"+zt+"' and djjg='%s' AND `day` >= '%s' AND `day` <= '%s' AND" + f" {sql_qhauth_djjg_qh} "
    sql_jtf = "select sum(xfjc) from xf_xfj_cd_zt_xj_jtf_xfjc where zt='"+zt+"' and jtf='集体访' AND `day` >= '%s' AND `day` <= '%s' AND" + f" {sql_qhauth_sheshixj} "
    # 全省-同比
    total_num, tb_qs = search_sb(zb_pymysql, sql, (s_time, e_time), (last_s_time, last_e_time))
    # xfxs_tb
    total_num_lx, tb_lx = search_sb(zb_pymysql, sql_xfxs, ('来信', s_time, e_time), ('来信', last_s_time, last_e_time))
    total_num_lf, tb_lf = search_sb(zb_pymysql, sql_xfxs, ('来访', s_time, e_time), ('来访', last_s_time, last_e_time))
    total_num_wx, tb_wx = search_sb(zb_pymysql, sql_xfxs_wx, (s_time, e_time), (last_s_time, last_e_time))
    # djjg_tb
    total_num_gj, tb_gj = search_sb(zb_pymysql, sql_djjg, ('国家', s_time, e_time), ('国家', last_s_time, last_e_time))  # 国家
    total_num_fsf, tb_fsf = search_sb(zb_pymysql, sql_djjg, ('省级', s_time, e_time), ('省级', last_s_time, last_e_time))  # 赴省访
    total_num_dsf, tb_dsf = search_sb(zb_pymysql, sql_djjg, ('市级', s_time, e_time), ('市级', last_s_time, last_e_time))  # 到市访
    total_num_dqx, tb_dqx = search_sb(zb_pymysql, sql_djjg, ('县级', s_time, e_time), ('县级', last_s_time, last_e_time))  # 到区县
    # jtf
    total_num_jtf, tb_jtf = search_sb(zb_pymysql, sql_jtf, (s_time, e_time), (last_s_time, last_e_time))  # 集体访

    from app import app
    report_url = app.config["FILE_URL"] + f"report-{total_time}.docx"
    path = app.config["FILE_PATH"]

    # 标题
    title = f'<h class="wrapper_title" style="display: block;width: 100%;font-size: 0.4rem;font-weight: 700;text-shadow: 0 0 5px #0cafc9;color: #ffffff;text-align: center">{qh}{zt}信访专题分析报告</h></h>'
    # 导出
    dc = f'<a class="dc" href="{report_url}" style="width: 1.2rem;height: 0.4rem;line-height: 0.4rem;position: fixed;right: 4rem;top: 2.2rem;font-size: 0.2rem;border-radius: 3rem;border: 1px solid #155E95;background:#010816;font-weight: 700;text-shadow: 0 0 5px #0cafc9;color: #ffffff;text-align:center;">导出</a>'
    # 生成时间
    report_time = f'<span class="wrapper_time" style="display: block;color: #DBFFFF; font-size: 0.25rem;text-align: center;margin: 0.3rem">{now_time}</span>'

    # 第一部分
    begin_html = f'<div class="report">{title}{dc}{report_time}</div>'
    begin_docx = f'<div class="report">{title}</div>'
    #####################################################################################################################

    # para1
    para1_title = f'<p class="subtitle" style="color: #A2C8CD; font-size: 0.24rem">一：基本情况</p>'
    para1_body = f'<p style="line-height: 0px;margin-bottom: 30px;text-indent: 26px">' \
                 f'<span class="time_span" style="text-indent: 0.2rem;height: 0.3rem;color: #F2DE58;font-size: 0.2rem;line-height: 0.3rem;margin: 0.1rem;">' \
                 f'{total_time}</span>' \
                 f'<span class="time_span" style="color: #B9E4E9;height: 0.3rem;font-size: 0.2rem;line-height: 0.3rem;margin: 0.1rem;">，' \
                 f'{qh}信访系统共登记受理{zt}类信访件{total_num}件次，同比浮动{tb_qs}%。</span>' \
                 f'</p>'
    para1 = para1_title + para1_body

    # para2
    para2_title = f'<p class="subtitle" style="color: #A2C8CD; font-size: 0.24rem">二：信访指标分析</p>'
    para2_body = f'<p style="line-height: 0px;margin-bottom: 30px;text-indent: 26px">' \
                 f'<span class="time_span" style="text-indent: 0.2rem;height: 0.3rem;color: #F2DE58;font-size: 0.2rem;line-height: 0.3rem;margin: 0.1rem;">' \
                 f'{total_time}</span>' \
                 f'<span class="time_span" style="color: #B9E4E9;height: 0.3rem;font-size: 0.2rem;line-height: 0.3rem;margin: 0.1rem;">，' \
                 f'{zt}类来信{total_num_lx}件次，同比浮动{tb_lx}%； 来访{total_num_lf}件次， 同比浮动{tb_lf}%； 网上信访{total_num_wx}件次， 同比浮动{tb_wx}%。' \
                 f'</p>'
    para2 = para2_title + para2_body

    # para3
    para3_title = f'<p class="subtitle" style="color: #A2C8CD; font-size: 0.24rem">三：信访态势分析</p>'
    para3_body = f'<p style="line-height: 0px;margin-bottom: 30px;text-indent: 26px">' \
                 f'<span class="time_span" style="text-indent: 0.2rem;height: 0.3rem;color: #F2DE58;font-size: 0.2rem;line-height: 0.3rem;margin: 0.1rem;">' \
                 f'{total_time}</span>' \
                 f'<span class="time_span" style="color: #B9E4E9;height: 0.3rem;font-size: 0.2rem;line-height: 0.3rem;margin: 0.1rem;">，' \
                 f'{zt}类国家件{total_num_gj}件次，同比浮动{tb_gj}%，赴省访{total_num_fsf}件次，同比浮动{tb_fsf}%；到市访{total_num_dsf}件次，同比浮动{tb_dsf}%；到区县信访{total_num_dqx}件次，同比浮动{tb_dqx}%。' \
                 f'</p>'
    para3 = para3_title + para3_body

    # para4
    para4_title = f'<p class="subtitle" style="color: #A2C8CD; font-size: 0.24rem">四：信访秩序分析</p>'
    para4_body = f'<p style="line-height: 0px;margin-bottom: 30px;text-indent: 26px">' \
                 f'<span class="time_span" style="text-indent: 0.2rem;height: 0.3rem;color: #F2DE58;font-size: 0.2rem;line-height: 0.3rem;margin: 0.1rem;">' \
                 f'{total_time}</span>' \
                 f'<span class="time_span" style="color: #B9E4E9;height: 0.3rem;font-size: 0.2rem;line-height: 0.3rem;margin: 0.1rem;">，' \
                 f'{zt}类集体访{total_num_jtf}件次，同比浮动{tb_jtf}%。' \
                 f'</p>'
    para4 = para4_title + para4_body

    ending = f'<p class="report_time" style="text-align: end;font-weight: 400;font-size: 0.2rem;color: #DAFFFF;">报告生成时间：{str(now_time)}</p>'

    data_for_html = begin_html + para1 + para2 + para3 + para4 + ending
    data_for_docx = begin_docx + para1 + para2 + para3 + para4 + ending

    # 生成docx和html报告文件
    with open(os.path.join(path, f"report-{total_time}.html"), "w", encoding="utf8") as f:
        f.write(data_for_docx)
    pypandoc.convert_file(os.path.join(path, f"report-{total_time}.html"), 'docx', outputfile=os.path.join(path, f"report-{total_time}.docx"))

    # # data = '广东省'+ zt + '信访专题分析报告' + data1 + '\n' + data2 + '\n' + data3 + '\n' + data4 + '\n' + '  '*55 + '报告生成时间：' + str(now_time)
    # data = '<span class="title">' + '广东省'+ zt + '信访专题分析报告' + '</span><span class="date">'+now_time + '</span>' + data1 + data2 + data3 + data4 + '<span class="report_time">' + '报告生成时间：' + str(now_time) + '</span>'
    #
    # from app import app
    # pdf_path = os.path.join(app.config["BASE_DIR"], "client", "gdxfdp", "file", "ztfxbg.pdf")
    # pdfkit.from_string('Hello!', 'ztfxdg.pdf')
    return 200, "success", {"data": data_for_html}


if __name__ == '__main__':
    request = {"day": ["2020-01-01", "2020-01-03"], "zt": "涉众型经济案件", "start": "2020-01-01", "end": "2020-01-03"}
    code, msg, res = run(**request)
    print(res)
