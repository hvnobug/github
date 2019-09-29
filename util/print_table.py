from collections.abc import Iterable
from datetime import datetime

from pymongo.cursor import Cursor as MongoCursor
from util import simple_datetime_format
from math import ceil

from util import logger, str_zh_count
from prettytable import PrettyTable


def print_table(params):
    if not params:
        logger.warning('参数 param 不合法')
        return
    if not isinstance(params, Iterable):
        logger.warning('param 为不可迭代对象')
        return
    if isinstance(params, MongoCursor):
        params = [param for param in params]
    attrs = __get_all_attrs(params)
    values = __get_all_values(attrs, params)
    table = PrettyTable(attrs)
    for item in values:
        table.add_row(item)
    print(table)


def __get_all_attrs(params):
    attrs = []
    for param in params:
        attrs.extend(__get_attrs(param))
    return list(set(attrs))


def __get_all_values(attrs, params):
    result = []
    for param in params:
        values = []
        for attr in attrs:
            try:
                value = param[attr]
            except KeyError:
                value = None
            values.append(__value2string(value))
        result.append(values)
    return result


def __value2string(param):
    if param is None:
        return '-'
    if isinstance(param, datetime):
        return simple_datetime_format(param)
    return str(param)


def __get_attrs(param):
    assert isinstance(param, Iterable), 'param 为不可迭代对象'
    return [attr for attr in param]


def __get_max_length(params):
    result = [0 for item in params[0]]
    for param in params:
        for i in range(len(param)):
            value = param[i]
            length = len(value) + ceil(str_zh_count(value) * 0.5)
            if length > result[i]:
                result[i] = length
    return result
