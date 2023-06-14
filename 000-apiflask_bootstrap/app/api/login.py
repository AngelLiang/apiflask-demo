from app import app

from app.util.response import make_response
from app.serializer.login import LoginIn, TokenOut
from app.service.login import user_login

TAGS = ['基础模块/登录认证']


@app.post('/api/v1/login')
@app.input(LoginIn)
@app.output(TokenOut)
@app.doc(summary='用户登录', tags=TAGS)
def login(data):
    username = data['username']
    password = data['password']
    out = user_login(username, password)
    return make_response(0, '登录成功！', out)
