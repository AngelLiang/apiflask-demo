from apiflask import HTTPError


class UsernameExistError(HTTPError):
    status_code = 200
    message = '用户名已经存在'


class UserDenyError(HTTPError):
    status_code = 200
    message = '用户已经被禁用'
