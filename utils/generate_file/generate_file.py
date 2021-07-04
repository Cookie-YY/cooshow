from reportlab.lib.pagesizes import LETTER  # pdf大小，信纸大小: (612, 792)
from reportlab.lib.units import inch, cm  # 画布，添加自定义内容: 页眉页脚
from reportlab.pdfgen import canvas  # 画布，添加自定义内容: 页眉页脚

from reportlab.pdfbase import pdfmetrics  # 注册字体: 支持中文
from reportlab.pdfbase.ttfonts import TTFont  # 构造字体: 支持中文
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, LongTable, Image  # 构造内容
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle  # 获取与添加样式
from reportlab.lib.enums import TA_JUSTIFY  # 对齐方式


class GenPDF:
    def __init__(self):
        self.header = "第 %d 页"  # 页眉页脚
        self.STYLE = self.get_styles()

    # 基础配置
    def get_styles(self):
        pdfmetrics.registerFont(TTFont('SimSun', '../fonts/SimSun.ttf'))        # 默认不支持中文，需要注册字体
        pdfmetrics.registerFont(TTFont('SimSunBd', '../fonts/SimSun-bold.ttf')) # 默认不支持中文，需要注册字体

        # registerFontFamily('SimSun', normal='SimSun', bold='SimSunBd', italic='VeraIt', boldItalic='VeraBI')

        stylesheet = getSampleStyleSheet()  # 获取样式集

        # 获取reportlab自带样式
        Normal = stylesheet['Normal']
        BodyText = stylesheet['BodyText']
        Italic = stylesheet['Italic']
        Title = stylesheet['Title']
        Heading1 = stylesheet['Heading1']
        Heading2 = stylesheet['Heading2']
        Heading3 = stylesheet['Heading3']
        Heading4 = stylesheet['Heading4']
        Heading5 = stylesheet['Heading5']
        Heading6 = stylesheet['Heading6']
        Bullet = stylesheet['Bullet']
        Definition = stylesheet['Definition']
        Code = stylesheet['Code']

        # 自带样式不支持中文，需要设置中文字体，但有些样式会丢失，如斜体Italic。有待后续发现完全兼容的中文字体
        Normal.fontName = 'SimSun'
        Italic.fontName = 'SimSun'
        BodyText.fontName = 'SimSun'
        Title.fontName = 'SimSunBd'
        Heading1.fontName = 'SimSun'
        Heading2.fontName = 'SimSun'
        Heading3.fontName = 'SimSun'
        Heading4.fontName = 'SimSun'
        Heading5.fontName = 'SimSun'
        Heading6.fontName = 'SimSun'
        Bullet.fontName = 'SimSun'
        Definition.fontName = 'SimSun'
        Code.fontName = 'SimSun'

        # 添加自定义样式
        stylesheet.add(
            ParagraphStyle(name='body',
                           fontName="SimSun",
                           fontSize=10,
                           textColor='black',
                           leading=20,  # 行间距
                           spaceBefore=0,  # 段前间距
                           spaceAfter=10,  # 段后间距
                           leftIndent=0,  # 左缩进
                           rightIndent=0,  # 右缩进
                           firstLineIndent=20,  # 首行缩进，每个汉字为10
                           alignment=TA_JUSTIFY,  # 对齐方式

                           # bulletFontSize=15,       #bullet为项目符号相关的设置
                           # bulletIndent=-50,
                           # bulletAnchor='start',
                           # bulletFontName='Symbol'
                           )
        )
        body = stylesheet['body']
        return {"Normal": Normal, "Italic": Italic, "BodyText": BodyText, "Title": Title, "Heading1": Heading1,
                "Heading2": Heading2, "Heading3": Heading3, "Heading4": Heading4, "Heading5": Heading5,
                "Heading6": Heading6, "Bullet": Bullet, "Definition": Definition, "Code": Code, "body": body}

    # 第一页的页眉
    def set_header(self, canvas, doc):  # 设置首页，参数格式固定
        canvas.saveState()  # 保存之前的画笔格式等状态,并设置新的状态
        canvas.setFont('SimSun', 9)  # 使用注册的字体
        canvas.drawString(doc.width / 5.0, doc.height + 100, str(doc.title))
        canvas.setFont('SimSun', 9)
        canvas.drawString(4 * inch, 0.75 * inch, self.header % doc.page)
        canvas.restoreState()  # 将画笔格式等状态还原

    # # 其他页的页眉
    # def myLaterPages(self, canvas, doc):  # 设置其他页
    #     canvas.saveState()  # 保存之前画笔的格式
    #     canvas.setFont('SimSun', 9)  # 使用注册的字体
    #     canvas.drawString(doc.width / 5.0, doc.height + 100, str(doc.title))
    #     canvas.setFont('SimSun', 9)  # 设置新的样式
    #     canvas.drawString(4 * inch, 0.75 * inch, self.header % doc.page)  # 填充新的内容
    #     canvas.restoreState()  # 画笔样式还原

    def wrap_contents(self, styles, contents):
        wrapped_contents = []

        for k, v in contents.items():
            wrapped_contents.append(Paragraph(v, styles[k]))

        # # title的内容用title_style包装
        # wrapped_contents.append(Paragraph(title, title_style))
        # # 段落的内容用body_style包装
        # for content in contents:
        #     # wrapped_contents.append(Paragraph('<font fontSize=11>'+content+'</font>' + '', body_style))
        #     wrapped_contents.append(Paragraph('<para>' + content + '</para>', body_style))
        return wrapped_contents

    def write2pdf(self, filepath, wrapped_contents, styles_all):
        doc = SimpleDocTemplate(filepath, pagesize=LETTER, title=styles_all.get("title"))
        doc.build(wrapped_contents, onFirstPage=self.set_header, onLaterPages=self.set_header)

    def run(self, filepath, styles, contents):
        """
        filepath: 生成的pdf
        styles: {"title": "", "para1_title": "", "para1_body": ""}       每个部分指定样式
        contens: {"title": "", "para1_title": "", "para1_body": ""}      每个部分指定内容
        """
        styles = {k: self.STYLE.get(v, self.STYLE["body"]) for k, v in styles.items()}  # 得到目标样式
        wrapped_contents = self.wrap_contents(styles, contents)  # 获取内容
        self.write2pdf(filepath, wrapped_contents, self.STYLE)


if __name__ == "__main__":
    run("test.pdf", styles={"title": "Title"}, contents={"title": "testTitle"})