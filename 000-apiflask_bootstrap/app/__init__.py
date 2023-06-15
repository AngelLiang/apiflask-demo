from apiflask import APIFlask

from . import setting

app = APIFlask(__name__, title='接口文档', version='1.0')
app.config.from_object(setting)

# db
from . import db   # noqa
db.init_app(app)

# error
from . import error    # noqa
error.init_app(app)

# api route
from .api.ping import *  # noqa
from .api.login import *  # noqa
from .api.user import *  # noqa
from .api.role import *  # noqa
from .api.menu import *  # noqa
from .api.current_user import *  # noqa
