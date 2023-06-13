from app import app
from app.util.response import make_response
from app.logger import logger


@app.get('/ping')
def ping():
    logger.info('ping')
    return make_response(data='pong')
