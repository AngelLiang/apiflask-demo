from apiflask import APIFlask

from . import setting

app = APIFlask(__name__, title='接口文档', version='1.0')
app.config.from_object(setting)

# api route
from .api.ping import *  # noqa
