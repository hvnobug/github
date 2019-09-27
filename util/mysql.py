"""
@功能：创建数据库连接池
"""
from common.config import mysql as config
from DBUtils.PooledDB import PooledDB
from util import logger
from util.pool import ConnectionPool


class MySqlConnectionPool(ConnectionPool):
    __pool = None

    def __init__(self):
        if not self.__pool:
            self.__pool = PooledDB(
                creator=config['creator'],
                mincached=config['min_cached'],
                maxcached=config['max_cached'],
                maxshared=config['max_shared'],
                maxconnections=config['max_connections'],
                blocking=config['blocking'],
                maxusage=config['max_usage'],
                setsession=config['set_session'],
                host=config['host'],
                port=config['port'],
                user=config['username'],
                passwd=config['password'],
                db=config['database'],
                use_unicode=config['use_unicode'],
                charset=config['charset']
            )

    # 创建数据库连接conn和游标cursor
    def __enter__(self):
        self.conn = self.__get_conn()
        self.cursor = self.conn.cursor()

    # 创建数据库连接池
    def __get_conn(self):
        return self.__pool.connection()

    # 释放连接池资源
    def __exit__(self):
        self.cursor.close()
        self.conn.close()

    # 从连接池中取出一个连接
    def get_conn(self):
        conn = self.__get_conn()
        cursor = conn.cursor()
        return cursor, conn


# 获取连接池,实例化
def get_connection():
    return MySqlConnectionPool()


class MySqLHelper(object):
    def __init__(self):
        self.db = get_connection()  # 从数据池中获取连接

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'inst'):  # 单例
            cls.inst = super(MySqLHelper, cls).__new__(cls, *args, **kwargs)
        return cls.inst

    # 封装执行命令
    def execute(self, sql, param=None, auto_close=False):
        """
        【主要判断是否有参数和是否执行完就释放连接】
        :param sql: 字符串类型，sql语句
        :param param: sql语句中要替换的参数"select %s from tab where id=%s" 其中的%s就是参数
        :param auto_close: 是否关闭连接
        :return: 返回连接 conn 和游标 cursor
        """
        cursor, conn = self.db.get_conn()  # 从连接池获取连接
        count = 0
        try:
            # count : 为改变的数据条数
            if param:
                count = cursor.execute(sql, param)
            else:
                count = cursor.execute(sql)
            conn.commit()
            if auto_close:
                self.close(cursor, conn)
        except Exception as e:
            logger('execute fail:' + str(e))

            pass
        return cursor, conn, count

    # 执行多条命令
    def execute_base(self, lis):
        """
        :param lis: 是一个列表，里面放的是每个sql的字典'[{"sql":"xxx","param":"xx"}....]'
        :return:
        """
        cursor, conn = self.db.get_conn()  # 从连接池获取连接
        try:
            for order in lis:
                sql = order['sql']
                param = order['param']
                if param:
                    cursor.execute(sql, param)
                else:
                    cursor.execute(sql)
            conn.commit()
            self.close(cursor, conn)
            return True
        except Exception as e:
            logger('execute_base fail:' + str(e))
            conn.rollback()
            self.close(cursor, conn)
            return False

    # 释放连接
    @staticmethod
    def close(cursor, conn):
        """释放连接归还给连接池"""
        cursor.close()
        conn.close()

    # 查询所有
    def select_all(self, sql, param=None):
        try:
            cursor, conn, count = self.execute(sql, param)
            res = cursor.fetchall()
            return res
        except Exception as e:
            logger('execute insert_all fail:' + str(e))
            self.close(cursor, conn)
            return count

    # 查询单条
    def select_one(self, sql, param=None):
        try:
            cursor, conn, count = self.execute(sql, param)
            res = cursor.fetchone()
            self.close(cursor, conn)
            return res
        except Exception as e:
            logger('execute select_one fail:' + str(e))
            self.close(cursor, conn)
            return count

    # 增加
    def insert_one(self, sql, param):
        try:
            cursor, conn, count = self.execute(sql, param)
            # _id = cursor.lastrowid()  # 获取当前插入数据的主键id，该id应该为自动生成为好
            conn.commit()
            self.close(cursor, conn)
            return count
            # 防止表中没有id返回0
            # if _id == 0:
            #     return True
            # return _id
        except Exception as e:
            logger('execute insert_one fail:' + str(e))
            conn.rollback()
            self.close(cursor, conn)
            return count

    # 增加多行
    def insert_base(self, sql, param):
        """
        :param sql:
        :param param: 必须是元组或列表[(),()]或（（），（））
        :return:
        """
        cursor, conn, count = self.db.get_conn()
        try:
            cursor.executemany(sql, param)
            conn.commit()
            return count
        except Exception as e:
            logger('execute insert_base fail:' + str(e))
            conn.rollback()
            self.close(cursor, conn)
            return count

    # 删除
    def delete(self, sql, param=None):
        try:
            cursor, conn, count = self.execute(sql, param)
            self.close(cursor, conn)
            return count
        except Exception as e:
            logger('execute delete fail:' + str(e))
            conn.rollback()
            self.close(cursor, conn)
            return count

    # 更新
    def update(self, sql, param=None):
        try:
            cursor, conn, count = self.execute(sql, param)
            conn.commit()
            self.close(cursor, conn)
            return count
        except Exception as e:
            logger('execute update fail:' + str(e))
            conn.rollback()
            self.close(cursor, conn)
            return count
