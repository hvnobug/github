email = {
    'sender': ['xxx@qq.com', 'xxx'],
    'secure': 'xxx',
    'host': 'smtp.qq.com',
    'receivers': [
        ['xxx@qq.com', 'xxx'],
        ['xxx@163.com', 'xxx']
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
