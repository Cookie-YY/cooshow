class Graph:
    """
    convert层继承Graph后，将数据放到__init__中之后，执行父类run方法，得到填充好的数据
    """
    def __init__(self):
        pass

    def get_graph(self):
        """
        根据传过来的参数找合适的图
        """
        pass

    def fill_graph(self):
        """
        拿到format后的数据，天道graph里面
        """
        pass

    def _get_data(self):
        """
        通过gd_id0去拿真实的请求，并走完整的流程拿到数据
        """
        pass

    def _format_data(self):
        """
        转换成echarts图需要的格式
        """
        pass

    def run(self):
        self.get_graph()
        self.fill_graph()
        return self


class Report:
    """
    插件过程的report模式，settings/gdxf/report/xxx.py 继承 Report之后
    self.text_title_1 =   在text里面{gd_id1}
    self.text_bg_2 =
    self.gd_id1 = 发请求的url

    self.wrapper_data =
    self.wrapper_text =
    self.wrapper_all =
    self.wrapper_text1
    self.wrapper_text2
    .....
    调用父类run方法
    1. 模拟发送所有请求，拿到数据
    2. 拼到text里面
    3. 把text拼起来
    """
    pass
