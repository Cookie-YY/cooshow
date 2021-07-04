import datetime
import platform

from pandas.core.dtypes.common import is_datetime64_any_dtype
from app import app

TIME_FORMAT = app.config.get("TIME_FORMAT", "%Y-%m-%d")

if platform.system() == "Windows":
    import locale
    locale.setlocale(locale.LC_ALL, "en")         # 兼容win7（winserver2012）下会报embedded null type的错误
    locale.setlocale(locale.LC_CTYPE, 'chinese')  # 使得windows下datetime的时间格式化出现中文


def date2datetime(date):
    if type(date) == datetime.date:
        return datetime.datetime.strptime(str(date), "%Y-%m-%d")
    return date


def df_formated_time(results, time_format=TIME_FORMAT):
    time_format = time_format or TIME_FORMAT
    date_columns = [i for i in results.columns if is_datetime64_any_dtype(results[i])]
    for date_column in date_columns:
        results[date_column] = results[date_column].apply(lambda x: datetime.datetime.strftime(x, time_format))
    return results
