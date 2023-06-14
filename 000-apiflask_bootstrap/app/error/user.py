from apiflask import HTTPError


class UsernameExistError(HTTPError):
    status_code = 200
    message = '用户名已经存在'
    # extra_data = {
    #     'error_code': '2323',
    #     'error_docs': 'https://example.com/docs/missing'
    # }


class UserDenyError(HTTPError):
    status_code = 200
    message = '用户已经被禁用'
    # extra_data = {
    #     'error_code': '2323',
    #     'error_docs': 'https://example.com/docs/missing'
    # }
