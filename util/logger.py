import logging.config

from common import logger_config as config

logging.config.dictConfig(config)
StreamLogger = logging.getLogger("StreamLogger")
FileLogger = logging.getLogger("FileLogger")
logger = StreamLogger
