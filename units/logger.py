import logging
from logging.handlers import RotatingFileHandler
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)


def setup_logger(name='app', level=logging.INFO, filename="app.log"):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.handlers:
        return logger
    formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] "
                                  "%(name)s:%(filename)s:%(lineno)d - %(message)s")

    file_handler = RotatingFileHandler(os.path.join(LOG_DIR, filename), maxBytes=20 * 1024 * 1024, backupCount=5,
                                       encoding='utf-8')

    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
