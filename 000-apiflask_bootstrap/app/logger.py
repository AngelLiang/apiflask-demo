from loguru import logger
import os
from app.setting import LOG_PATH

os.makedirs(LOG_PATH, exist_ok=True)
log_pathfile = os.path.join(LOG_PATH, 'log_{time:YYYYMMDD}.log')

logger.add(log_pathfile, format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level} | {message}", level="INFO")
