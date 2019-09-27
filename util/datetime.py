from datetime import datetime

__UTC_DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
__SIMPLE_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'


def ufc_datetime_format(date_time: datetime):
    """
    datetime 格式化为字符串
    :param date_time:
    :return:
    """
    return date_time.strftime(__UTC_DATETIME_FORMAT)


def format_ufc_datetime(date_time: str):
    """
    字符串格式化为 datetime
    :param date_time:
    :return:
    """
    return datetime.strptime(date_time, __UTC_DATETIME_FORMAT)


def simple_datetime_format(date_time: datetime):
    return date_time.strftime(__SIMPLE_DATETIME_FORMAT)
