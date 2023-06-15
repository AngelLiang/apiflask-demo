from apiflask import HTTPError
from apiflask.exceptions import _ValidationError


def init_app(app):
    @app.error_processor
    def app_error_processor(error):
        # print(type(error))
        msg = '操作失败'
        if isinstance(error, _ValidationError):
            msg = '传参校验错误，请检查传参'
        elif isinstance(error, HTTPError):
            msg = error.message
        # 获取业务错误码
        code = getattr(error, 'code', 1)
        return {
            'code': code,
            'msg': msg,
            'data': error.detail
        }, 200, error.headers


class UsernameExistError(HTTPError):
    status_code = 200
    message = '用户名已经存在'
    # extra_data = {
    #     'error_code': '2323',
    #     'error_docs': 'https://example.com/docs/missing'
    # }
