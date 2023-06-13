import os
from dotenv import load_dotenv
from .util.response import BaseResponse


load_dotenv()

# app.config['BASE_RESPONSE_SCHEMA'] = BaseResponse
BASE_RESPONSE_SCHEMA = BaseResponse
BASE_RESPONSE_DATA_KEY = 'data'
SWAGGER_UI_LAYOUT = 'StandaloneLayout'

LOG_PATH = 'log'

DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
DB_PORT = int(os.getenv('DB_PORT', 3306))
DB_USER = os.getenv('DB_USER', 'user')
DB_PASS = os.getenv('DB_PASS', 'pass')
DB_NAME = os.getenv('DB_NAME', 'auto_buy_smoke')

DATABASE = f'mysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
