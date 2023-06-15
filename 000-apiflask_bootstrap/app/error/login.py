from apiflask import HTTPError


class DecryptPasswordError(HTTPError):
    status_code = 200
    message = '密码解密失败'


class UsernameOrPasswordError(HTTPError):
    status_code = 200
    message = '用户名或密码错误'
