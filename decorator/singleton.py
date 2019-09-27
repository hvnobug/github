from functools import wraps


def singleton(cls):
    """
    单例模式装饰器
    """
    _instance = {}

    @wraps(cls)
    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton
