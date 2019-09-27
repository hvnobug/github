import string
from zhon.hanzi import punctuation


def is_contain_chinese(check_str):
    """
    判断字符串中是否包含中文
    :param check_str: {str} 需要检测的字符串
    :return: {bool} 包含返回True， 不包含返回False
    """
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


def is_chinese(check_str):
    """
    检查整个字符串是否为中文
    Args: string (str): 需要检查的字符串,包含空格也是False
    Return bool
    """
    for chart in check_str:
        if chart < u'\u4e00' or chart > u'\u9fff':
            return False
    return True


def str_count(check_str):
    """
    找出字符串中的中英文、空格、数字、标点符号个数
    """
    count_en = count_dg = count_sp = count_zh = count_pu = 0

    for s in check_str:
        # 英文
        if s in string.ascii_letters:
            count_en += 1
        # 数字
        elif s.isdigit():
            count_dg += 1
        # 空格
        elif s.isspace():
            count_sp += 1
        # 中文
        elif s.isalpha() or s in punctuation:
            count_zh += 1
        # 特殊字符
        else:
            count_pu += 1
    # print('英文字符：', count_en)
    # print('数字：', count_dg)
    # print('空格：', count_sp)
    # print('中文：', count_zh)
    # print('特殊字符：', count_pu)
    # print(check_str)
    # print({'en': count_en, 'db': count_dg, 'sp': count_sp, 'zh': count_zh, 'pu': count_pu})
    return {'en': count_en, 'db': count_dg, 'sp': count_sp, 'zh': count_zh, 'pu': count_pu}


def str_zh_count(check_str):
    return str_count(check_str)['zh']


def str_zh_and_pu_count(check_str):
    count = str_count(check_str)
    return count['zh'] + count['pu']
