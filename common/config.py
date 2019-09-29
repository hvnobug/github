email = {
    'sender': ['xx@qq.com', 'sender_name'],
    'secure': 'xxx',
    'host': 'smtp.qq.com',
    'receivers': [
        ['xx@163.com', 'receiver_name']
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
    'username': 'username',
    'password': 'password',
    'database': 'test',
    'auth_database': 'admin',
    'auth_mechanism': 'MONGODB-CR',
    'auth': True
}
