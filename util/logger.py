import logging.config

from common import logger_config as logger

logging.config.dictConfig(logger)
StreamLogger = logging.getLogger("StreamLogger")
FileLogger = logging.getLogger("FileLogger")
logger = FileLogger
