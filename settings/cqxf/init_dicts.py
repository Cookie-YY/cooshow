# 初始化指标需要的值
INITIALIZATION = {
    "yyxfjc": ["VALUE_INT"],
    "gjjxfjc": ["VALUE_INT"],
    "wtsd": ["省级", "市级", "县级", "乡级"],
    # "year": [2016, 2017, 2018, 2019, 2020, 2021, 2022],
    "year": ["2016", "2017", "2018", "2019", "2020", "2021", "2022"],
    "month": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    # "day": ["date:2016-2020"],

    "shej_02": ["广东省"],
    "shij_02": ["广州市", "深圳市", "佛山市", "东莞市", "中山市", "珠海市", "江门市", "肇庆市", "惠州市", "汕头市", "潮州市", "揭阳市", "汕尾市", "湛江市", "茂名市", "阳江市", "韶关市", "清远市", "云浮市", "梅州市", "河源市"],
    "qh": ["广州市", "深圳市", "佛山市", "东莞市", "中山市", "珠海市", "江门市", "肇庆市", "惠州市", "汕头市", "潮州市", "揭阳市", "汕尾市", "湛江市", "茂名市", "阳江市", "韶关市", "清远市", "云浮市", "梅州市", "河源市"],
    # "xfbm": ["广州市信访局", "深圳市信访局", "佛山市信访局", "东莞市信访局", "中山市信访局", "珠海市信访局", "江门市信访局", "肇庆市信访局", "惠州市信访局", "汕头市信访局", "潮州市信访局", "揭阳市信访局", "汕尾市信访局", "湛江市信访局", "茂名市信访局", "阳江市信访局", "韶关市信访局", "清远市信访局", "云浮市信访局", "梅州市信访局", "河源市信访局"],
    # "xj_02": "D:\\Study\\PKUSE\\all-through\\产品\\指标表初始化\\xj_02.txt",

    # 20201021新增
    "zxdbxfjc": ["VALUE_INT"],
    "shezxdbxfjc": ["VALUE_INT"],
    "shizxdbxfjc": ["VALUE_INT"],
    "xzxdbxfjc": ["VALUE_INT"],
    "gjzxdbxfjc": ["VALUE_INT"],

    # 20200903新增
    "bljc": ["VALUE_INT"],
    "sljc": ["VALUE_INT"],

    # 20200904新增
    "dljc": ["VALUE_INT"],
    "dbjc": ["VALUE_INT"],
    "cqwbjjc": ["VALUE_INT"],
    "bmyjc": ["VALUE_INT"],
    "jbmyjc": ["VALUE_INT"],
    "ypjjc": ["VALUE_INT"],
    "cqwpjjc": ["VALUE_INT"],
    "dpjjc": ["VALUE_INT"],
    "jssljc": ["VALUE_INT"],
    "cqsljc": ["VALUE_INT"],
    "cqwsljc": ["VALUE_INT"],
    # 20200907新增
    "xfrqxfjc": ["VALUE_INT"],
    "djrqxfjc": ["VALUE_INT"],
    "jhrqxfjc": ["VALUE_INT"],
    "xfrqxfrc": ["VALUE_INT"],
    "djrqxfrc": ["VALUE_INT"],
    "jhrqxfrc": ["VALUE_INT"],

    # 20200927新增
    "xfbmxfjc": ["VALUE_INT"],
    "zrdwxfjc": ["VALUE_INT"],

    # 20200909新增
    "xb": ["男", "女", "未知"],
    "yjzt": ["平稳"],
    "mdgjyjzt": ["平稳"],


    "slqk":["及时受理","超期受理","超期未受理"],
    "cfxfbz": ["初件", "重件"],
    "lmj": ["联名件", "非联名件"],
    "jjf": ["进京访", "非进京访"],
    "jtf": ["集体访", "个访"],
    "bj": ["办结", "未办结"],
    "hj": ["化解", "未化解"],
    "hjbz": ["化解", "未化解", "未办结"],
    "pjzt": ["满意", "不满意"],
    "xfjc": ["VALUE_INT"],
    "zb": ["VALUE_FLOAT"],
    "hjlv": ["VALUE_FLOAT"],
    "xfrc": ["VALUE_INT"],
    "zjlv": ["VALUE_FLOAT"],
    "tb": ["VALUE_FLOAT"],
    "hb": ["VALUE_FLOAT"],
    "gfrc": ["VALUE_INT"],
    "jtfrc": ["VALUE_INT"],
    "slxfjc": ["VALUE_INT"],
    "jssllv": ["VALUE_FLOAT"],
    "aqdflv":["VALUE_FLOAT"],
    "cplv": ["VALUE_FLOAT"],
    "mylv": ["VALUE_FLOAT"],
    "wxzb": ["VALUE_FLOAT"],
    "blxfjc": ["VALUE_INT"],
    "dwjc": ["VALUE_INT"],
    "bmjc": ["VALUE_INT"],
    "bmsljc": ["VALUE_INT"],
    "bmjssllv": ["VALUE_FLOAT"],
    "bmcplv": ["VALUE_FLOAT"],
    "bmmylv": ["VALUE_FLOAT"],
    "dwbljc": ["VALUE_INT"],
    "dwjssllv": ["VALUE_FLOAT"],
    "dwcplv": ["VALUE_FLOAT"],
    "dwmylv": ["VALUE_FLOAT"],
    "xfcs": ["VALUE_INT"],
    "jjfjc": ["VALUE_INT"],
    "fsfjc": ["VALUE_INT"],
    "yyjc": ["VALUE_INT"],
    "jtfjc": ["VALUE_INT"],
    "yjfjc": ["VALUE_INT"],
    "cfcs": ["VALUE_INT"],
    "bajc": ["VALUE_INT"],
    "wbjbajc": ["VALUE_INT"],
    "whjbajc": ["VALUE_INT"],
    "yhjbajc": ["VALUE_INT"],
    "bahjlv": ["VALUE_FLOAT"],
    "mdgjhjjc": ["VALUE_INT"],
    "hjjc": ["VALUE_INT"],
    "mdgjbjjc": ["VALUE_INT"],
    "mdgjhjlv": ["VALUE_FLOAT"],
    "mdgjxfjc": ["VALUE_INT"],
    "wtsdrc": ["VALUE_INT"],
    "hjdrc": ["VALUE_INT"],
    "czdrc": ["VALUE_INT"],
    "myjc": ["VALUE_INT"],
    "value": ["VALUE_INT"],

    "chas": ["VALUE_INT"],
    "lmwt": ["联名网投", "非联名网投"],
    "zhy": ["无业人员", "文体人员", "企业管理人员", "现役军人", "专业技术人员", "农民", "其他", "律师", "学生", "退（离）休人员", "自由职业者", "教师", "个体经营者", "工人",
            "医生", "公务员", "事业单位工作人员"],
    "fsf": ["赴省访", "非赴省访"],
    "yjf": ["越级访", "非越级访"],
    "yy": ["扬言", "非扬言"],
    # "xfbm": ["河北省信访局", "市中区信访局", "邯郸市信访局", "承德市信访局", "廊坊市信访局", "张家口市信访局", "邯山区信访局", "衡水市信访局(二)", "长安区信访局", "唐山市信访局",
    #          "石家庄市信访局", "测试一市信访局", "中心街道信访处", "保定市信访局"],
    "zrdw":['广东省住房和城乡建设厅','广东省交通运输厅','广东省水利厅','广东省农业农村厅','广东省卫生健康委员会','广东省国资委','广东省市场监督管理局','广东省应急管理厅','广东省地方金融监督管理局','广东省公安厅','广东省民政厅','广东省司法厅','广东省人力资源和社会保障厅','广东省生态环境厅','广东省教育厅','广东省自然资源厅','广东省科技厅','广东省商务厅','广东省退役军人事务厅'],

    "blfs": ["存", "直接回复", "转送", "交办", "受理告知", "督办", "不予受理", "不再受理"],
    "xfly": ["国家", "省", "市", "县", "乡镇"],
    "ld": ["周焱华", "许勤", "刘一时", "王东峰"],

    "yjnr": ["政法", "科技与信息产业", "纪检监察", "党务政务", "国土资源", "教育文体", "劳动和社会保障", "城乡建设", "农村农业", "卫生计生", " 环境保护", "交通运输", "民政",
             "经济管理", "商贸旅游", "组织人事", "其他"],
    # "ejnr": ["法制建设", "信息化建设", "党政处分", "政治体制", "土地资源管理", "文物管理", "其他", "劳动关系", "惠农补贴", "人口计生", "农垦农场", "环保管理", "诉讼",
    #          "教育体制", "福利慈善", "宏观调控", "国资监管", "科学技术", "社会治安", "医政监管", "社会服务", "文化", "工资福利", "劳动保护", "水库移民", "干部作风",
    #          "建设管理", "土地征收", "野生资源管理", "安全生产", "考试招生", "法律服务", "区划地名", "体育", "建筑市场", "教师队伍和待遇", "城乡规划", "社会救助", "公共卫生",
    #          "优抚", "刑案侦破", "出租车管理", "商业贸易", "水利水电", "住房保障与房地产", "城镇职工社会保险", "基层选举和社区建设", "招录辞退", "林业管理", "工程质量",
    #          "城镇居民社会保险", "人力资源", "交通管理", "救灾募捐", "户籍证件", "仲裁与调解", "市场监管", "土地承包经营", "动物防疫", "集体土地上房屋拆迁与补偿", "滥用职权",
    #          "知识产权", "刑罚执行", "旅游管理", "行政复议", "金融财税", "教育行政管理", "机构改革", "质监检验检疫", "退休政策及待遇", "医患纠纷", "表达情感", "贪污贿赂",
    #          "保险证券期货", "邮政管理", "环境污染", "食品药品监管", "海洋气象地震", "宣传舆论", "民族宗教", "历史遗留问题", "警务督察", "党的建设", "群众团体", "复退安置",
    #          "电信", "选拔任用", "草原草场", "建设项目审批", "村务管理", " 就业培训", "国有土地上房屋征收与补偿", "军转安置", "港澳台侨", "失职渎职", "村镇建设", "农资农技",
    #          "扶贫开发", "领导事务", "客货运输", "编制职位", "失学辍学", "教育收费", "城市建设和市政管理", "矿产资源管理", "农副产品流通", "能源管理", "离休", "企业破产",
    #          "社保基金管理", "民间组织", "国防外交"],
    # "sjnr": "D:\\Study\\PKUSE\\all-through\\产品\\指标表初始化\\sjnr.txt",
    # "ejnr@file": "D:\\Study\\PKUSE\\all-through\\产品\\指标表初始化\\ejnr.txt",

    "rdwt": ["法制建设", "信息化建设", "党政处分", "政治体制", "土地资源管理", "文物管理", "其他", "劳动关系", "惠农补贴", "人口计生", "农垦农场", "环保管理", "诉讼",
             "教育体制", "福利慈善", "宏观调控", "国资监管", "科学技术", "社会治安", "医政监管", "社会服务", "文化", "工资福利", "劳动保护", "水库移民", "干部作风",
             "建设管理", "土地征收", "野生资源管理", "安全生产", "考试招生", "法律服务", "区划地名", "体育", "建筑市场", "教师队伍和待遇", "城乡规划", "社会救助", "公共卫生",
             "优抚", "刑案侦破", "出租车管理", "商业贸易", "水利水电", "住房保障与房地产", "城镇职工社会保险", "基层选举和社区建设", "招录辞退", "林业管理", "工程质量",
             "城镇居民社会保险", "人力资源", "交通管理", "救灾募捐", "户籍证件", "仲裁与调解", "市场监管", "土地承包经营", "动物防疫", "集体土地上房屋拆迁与补偿", "滥用职权",
             "知识产权", "刑罚执行", "旅游管理", "行政复议", "金融财税", "教育行政管理", "机构改革", "质监检验检疫", "退休政策及待遇", "医患纠纷", "表达情感", "贪污贿赂",
             "保险证券期货", "邮政管理", "环境污染", "食品药品监管", "海洋气象地震", "宣传舆论", "民族宗教", "历史遗留问题", "警务督察", "党的建设", "群众团体", "复退安置",
             "电信", "选拔任用", "草原草场", "建设项目审批", "村务管理", " 就业培训", "国有土地上房屋征收与补偿", "军转安置", "港澳台侨", "失职渎职", "村镇建设", "农资农技",
             "扶贫开发", "领导事务", "客货运输", "编制职位", "失学辍学", "教育收费", "城市建设和市政管理", "矿产资源管理", "农副产品流通", "能源管理", "离休", "企业破产",
             "社保基金管理", "民间组织", "国防外交"],

    "nlrange": ["30岁以下", "31-40岁", "41-50岁", "51-60岁", "60岁以上", "未知"],
    "cfcsrange": ["1次", "2-5次", "6-10次", "11-30次", "31-50次", "50次以上"],
    "rsrange": ["1-5人", "6-20人", "21-50人", "50人以上"],
    "xfcsrange": ["1次", "2-5次", "6-10次", "11-30次", "31-50次", "50次以上"],
    "jtfrsrange": ["5-10人", "11-20人", "21-50人", "51-100人", "100人以上"],

    "zd": ["网上", "手机app", "微信", "其他"],
    "djjg": ["省级", "市级", "县级"],
    "xfxs": ["来信", "来访", "网信"],
    "xfmd": ["揭发控告", "意见建议", "其他", "申诉", "求决"],
    # "jglb":"D:\\Study\\PKUSE\\all-through\\产品\\指标表初始化\\jglb.txt",
    "mdgj": ["重点领域", "重点群体", "重点问题", "重点人员"],
    "jsfs": ["交办", "督办"],
    "zfxs": ["越级访", "逐级访"]
}
