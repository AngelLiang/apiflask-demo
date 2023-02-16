import datetime
from apiflask import APIFlask
import scheduler

SECRET_KEY='secret-key'

SCHEDULER_ENABLE=1

# 是否启用 API
SCHEDULER_API_ENABLED=True

# API 后缀
# SCHEDULER_API_PREFIX=/scheduler

# 允许访问的主机
# SCHEDULER_ALLOWED_HOSTS=["*"]

# SCHEDULER_JOBSTORES={}
# SCHEDULER_EXECUTORS={}
# SCHEDULER_JOB_DEFAULTS={}
# SCHEDULER_TIMEZONE={}


app = APIFlask(__name__, title='接口文档', version='1.0')
app.config.from_object(__name__)
if app.config['SCHEDULER_ENABLE']==1:
    scheduler.init_app(app)


@app.get('/index')
def index():
    return {'hello': 'world'}

if __name__ == "__main__":
    app.run()
