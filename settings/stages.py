# 函数名：阶段1.1-1/阶段中文/阶段英文/信息格式

class Stage:
    def __init__(self, stage_code, name_i18n, msg_format):
        self.stage_code = stage_code
        self.stage_name = name_i18n
        self.msg_format = msg_format


STAGES = {
    "authentication": Stage("1-1", {"zh": "", "en": ""}, "[authentication]: ")

}
