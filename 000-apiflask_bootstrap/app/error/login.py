from apiflask import HTTPError


class DecryptPasswordError(HTTPError):
    status_code = 200
    message = '密码解密失败'


class UsernameOrPasswordError(HTTPError):
    status_code = 200
    message = '用户名或密码错误'
    # extra_data = {
    #     'error_code': '2323',
    #     'error_docs': 'https://example.com/docs/missing'
    # }
