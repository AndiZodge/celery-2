import logging
import sys
from celery import Celery
from config import CELERY_RESULT_BACKEND, CELERY_BROKER_URL

def get_logger(logger_name=None, default_log_level=logging.INFO, module=None):
    logger = logging.getLogger(logger_name)
    logger.setLevel(default_log_level)
    logger.propagate = False
    if not module:
        module = 'Default'
    formatter = logging.Formatter(
        "[%(levelname)s] :: %(asctime)s | %(lineno)s | {0} | %(message)s".format(module))
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(formatter)
    logger.addHandler(stdout_handler)

    return logger


celery = Celery(
    'task',
    broker=CELERY_BROKER_URL,
    # backend=CELERY_RESULT_BACKEND
)