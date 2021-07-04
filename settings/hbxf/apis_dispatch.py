# apis分发
URL_DISPATCH_MAP = {
    ###### 问题分类地图 ######
    # 全部_件次
    "全部_件次": "http://39.107.240.28:3389/api/xf/?index=xfjc_zb&timetype=cd&qh=xj&lx=yjnr&name=shij_02&value=xfjc&transformer=@groupby&day=[2019-01-01,2019-02-02]&full=true",
    # 进京访_件次
    "进京访_件次": "http://39.107.240.28:3389/api/xf/?index=xfjc_zb&timetype=cd&qh=xj&lx=yjnr_jjf&name=shij_02&value=xfjc&transformer=@groupby&day=[2019-01-01,2019-02-02]&jjf=进京访&full=true",
    # 赴省访_件次
    "赴省访_件次": "http://39.107.240.28:3389/api/xf/?index=xfjc_zb&timetype=cd&qh=xj&lx=yjnr_fsf&name=shij_02&value=xfjc&transformer=@groupby&day=[2019-01-01,2019-02-02]&fsf=赴省访&full=true",

    # 全部_问题属地人次
    "全部_人次_问题属地": "http://39.107.240.28:3389/api/xf/?index=wtsdrc_zb&timetype=cd&qh=xj&lx=yjnr&name=shij_02&value=wtsdrc&transformer=@groupby&day=[2019-01-01,2019-02-02]&full=true",
    # 进京访_问题属地人次
    "进京访_人次_问题属地": "http://39.107.240.28:3389/api/xf/?index=wtsdrc_zb&timetype=cd&qh=xj&lx=yjnr_jjf&name=shij_02&value=wtsdrc&transformer=@groupby&day=[2019-01-01,2019-02-02]&jjf=进京访&full=true",
    # 赴省访_问题属地人次
    "赴省访_人次_问题属地": "http://39.107.240.28:3389/api/xf/?index=wtsdrc_zb&timetype=cd&qh=xj&lx=yjnr_fsf&name=shij_02&value=wtsdrc&transformer=@groupby&day=[2019-01-01,2019-02-02]&fsf=赴省访&full=true",

    # 全部_户籍地人次
    "全部_人次_户籍地": "http://39.107.240.28:3389/api/xf/?index=hjdrc_zb&timetype=cd&qh=xj&lx=yjnr&name=shij_02&value=hjdrc&transformer=@groupby&day=[2019-01-01,2019-02-02]&full=true",
    # 进京访_户籍地人次
    "进京访_人次_户籍地": "http://39.107.240.28:3389/api/xf/?index=hjdrc_zb&timetype=cd&qh=xj&lx=yjnr_jjf&name=shij_02&value=hjdrc&transformer=@groupby&day=[2019-01-01,2019-02-02]&jjf=进京访&full=true",
    # 【没有表】赴省访_户籍地人次
    "赴省访_人次_户籍地": "http://39.107.240.28:3389/api/xf/?index=hjdrc_zb&timetype=cd&qh=xj&lx=yjnr_fsf&name=shij_02&value=hjdrc&transformer=@groupby&day=[2019-01-01,2019-02-02]&fsf=赴省访&full=true",

    # 全部_常住地人次
    "全部_人次_常住地": "http://39.107.240.28:3389/api/xf/?index=czdrc_zb&timetype=cd&qh=xj&lx=yjnr&name=shij_02&value=czdrc&transformer=@groupby&day=[2019-01-01,2019-02-02]&full=true",
    # 进京访_常住地人次
    "进京访_人次_常住地": "http://39.107.240.28:3389/api/xf/?index=czdrc_zb&timetype=cd&qh=xj&lx=yjnr_jjf&name=shij_02&value=czdrc&transformer=@groupby&day=[2019-01-01,2019-02-02]&jjf=进京访&full=true",
    # 赴省访_常住地人次
    "赴省访_人次_常住地": "http://39.107.240.28:3389/api/xf/?index=czdrc_zb&timetype=cd&qh=xj&lx=yjnr_fsf&name=shij_02&value=czdrc&transformer=@groupby&day=[2019-01-01,2019-02-02]&fsf=赴省访&full=true",

    # 重点人员姓名列表
    "信访人分析_重点人员_全部":"http://39.107.240.28:3389/api/xf/?table=xf_xfr_cy_zjhm_xm_xfjc&name=xm&value=zjhm&direct_order=-xfjc&direct_limit=100",
    "信访人分析_重点人员_来信":"http://39.107.240.28:3389/api/xf/?table=xf_xfr_cy_zjhm_xm_xfxs_xfjc&name=xm&value=zjhm&direct_order=-xfjc&xfxs=来信&direct_limit=100",
    "信访人分析_重点人员_来访":"http://39.107.240.28:3389/api/xf/?table=xf_xfr_cy_zjhm_xm_xfxs_xfjc&name=xm&value=zjhm&direct_order=-xfjc&xfxs=来访&direct_limit=100",
    "信访人分析_重点人员_网信":"http://39.107.240.28:3389/api/xf/?table=xf_xfr_cy_zjhm_xm_xfxs_xfjc&name=xm&value=zjhm&direct_order=-xfjc&xfxs=网信&direct_limit=100",
    # 暂时没有扬言的数据表
    "信访人分析_重点人员_扬言":"http://39.107.240.28:3389/api/xf/?table=xf_xfr_cy_zjhm_xm_yy_xfjc&name=xm&value=zjhm&direct_order=-xfjc&direct_limit=100",
    "信访人分析_重点人员_专项":"http://39.107.240.28:3389/api/xf/?table=xf_xfr_cy_zjhm_xm_zxbz_xfjc&name=xm&value=zjhm&direct_order=-xfjc&direct_limit=100",

    # 攻坚治理_地图
    "攻坚治理_重点人员_全部_件次":"http://39.107.240.28:3389/api/xf/?table=xf_xfj_cd_xj_zd_xfjc_zb&name=shij_02&value=xfjc&transformer=@groupby&day=[2020-01-01,2020-05-30]&shij_02=invalid",
    "攻坚治理_重点人员_进京访_件次":"http://39.107.240.28:3389/api/xf/?table=xf_xfj_cd_xj_zd_jjf_xfjc_zb&name=shij_02&value=xfjc&transformer=@groupby&day=[2020-01-01,2020-05-30]&shij_02=invalid",
    "攻坚治理_重点人员_赴省访_件次":"http://39.107.240.28:3389/api/xf/?table=xf_xfj_cd_xj_zd_fsf_xfjc_zb&name=shij_02&value=xfjc&transformer=@groupby&day=[2020-01-01,2020-05-30]&shij_02=invalid",
    "攻坚治理_重点人员_全部_人次_问题属地":"http://39.107.240.28:3389/api/xf/?table=xf_xfj_cd_xj_zd_wtsdrc_zb&name=shij_02&value=wtsdrc&transformer=@groupby&day=[2020-01-01,2020-05-30]&shij_02=invalid",
    "攻坚治理_重点人员_进京访_人次_问题属地":"http://39.107.240.28:3389/api/xf/?table=xf_xfj_cd_xj_zd_jjf_wtsdrc_zb&name=shij_02&value=wtsdrc&transformer=@groupby&day=[2020-01-01,2020-05-30]&shij_02=invalid",
    "攻坚治理_重点人员_赴省访_人次_问题属地":"http://39.107.240.28:3389/api/xf/?table=xf_xfj_cd_xj_zd_fsf_wtsdrc_zb&name=shij_02&value=wtsdrc&transformer=@groupby&day=[2020-01-01,2020-05-30]&shij_02=invalid",
    "攻坚治理_重点人员_全部_人次_常住地":"http://39.107.240.28:3389/api/xf/?table=xf_xfj_cd_xj_zd_czdrc_zb&name=shij_02&value=czdrc&transformer=@groupby&day=[2020-01-01,2020-05-30]&shij_02=invalid",
    "攻坚治理_重点人员_进京访_人次_常住地":"http://39.107.240.28:3389/api/xf/?table=xf_xfj_cd_xj_zd_jjf_czdrc_zb&name=shij_02&value=czdrc&transformer=@groupby&day=[2020-01-01,2020-05-30]&shij_02=invalid",
    "攻坚治理_重点人员_赴省访_人次_常住地":"http://39.107.240.28:3389/api/xf/?table=xf_xfj_cd_xj_zd_fsf_czdrc_zb&name=shij_02&value=czdrc&transformer=@groupby&day=[2020-01-01,2020-05-30]&shij_02=invalid"


}
