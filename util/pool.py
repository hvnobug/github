from decorator import singleton


@singleton
class ConnectionPool(object):
    # 创建数据库连接
    def __enter__(self):
        pass

    # 创建数据库连接池
    def __get_conn(self):
        pass

    # 释放连接池资源
    def __exit__(self):
        pass

    # 从连接池中取出一个连接
    def get_conn(self):
        pass
