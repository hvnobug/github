import pymysql

email = {
    'sender': ['xx@qq.com', 'xx'],
    'secure': 'xx',
    'host': 'smtp.qq.com',
    'receivers': [
        ['xx@163.com', 'xx']
    ],
    'user_ssl': True,
    'port': 25,
    'ssl_port': 465,
    'charset': 'utf-8'
}

logger = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)s %(process)d - [%(threadName)s] %(filename)s.%(funcName)s:%(lineno)d : %(message)s',
        }
        # 其他的 formatter
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple'
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'github.log',
            'level': 'DEBUG',
            'formatter': 'simple'
        },
        # 其他的 handler
    },
    'loggers': {
        'StreamLogger': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'FileLogger': {
            # 既有 console Handler，还有 file Handler
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
        # 其他的 Logger
    }
}
mongo = {
    'host': '127.0.0.1',
    'port': 27017,
    'username': None,
    'password': None,
    'database': 'test'
}
mysql = {
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'test',
    'username': 'root',
    'password': 'root',
    # 数据库连接编码
    'charset': 'utf8',
    # 启动时开启的闲置连接数量(缺省值 0 开始时不创建连接)
    'min_cached': 10,
    # 连接池中允许的闲置的最多连接数量(缺省值 0 代表不闲置连接池大小)
    'max_cached': 10,
    # 共享连接数允许的最大数量(缺省值 0 代表所有连接都是专用的)如果达到了最大数量,被请求为共享的连接将会被共享使用
    'max_shared': 10,
    # 创建连接池的最大数量(缺省值 0 代表不限制)
    'max_connections': 100,
    # 设置在连接池达到最大数量时的行为(缺省值 0 或 False 代表返回一个错误<toMany......> 其他代表阻塞直到连接数减少,连接被分配)
    'blocking': True,
    # 单个连接的最大允许复用次数(缺省值 0 或 False 代表不限制的复用).当达到最大数时,连接会自动重新连接(关闭和重新打开)
    'max_usage': 0,
    # 一个可选的SQL命令列表用于准备每个会话，如["set datestyle to german", ...]
    'set_session': None,
    # 使用连接数据库的模块
    'creator': pymysql,
    # 使用 unicode
    'use_unicode': True
}
