def get_object_attrs(bean):
    """
    返回对象或类的属性列表
    :param bean: 对象或属性
    :return: 属性列表
    """
    return list(filter(lambda attr: not attr.startswith('_') and not callable(getattr(bean, attr)), dir(bean)))


def object2dict(bean):
    result = {}
    for attr in get_object_attrs(bean):
        result[attr] = getattr(bean, attr)
    return result
