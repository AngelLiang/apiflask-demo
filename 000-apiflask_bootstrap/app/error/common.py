from apiflask import HTTPError


class NotFoundError(HTTPError):
    status_code = 200
    code = 4004
    message = '找不到资源'
    # extra_data = {
    #     'error_code': '2323',
    #     'error_docs': 'https://example.com/docs/missing'
    # }
