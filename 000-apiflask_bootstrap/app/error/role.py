from apiflask import HTTPError


class RoleCodeExistError(HTTPError):
    status_code = 200
    message = '角色编码已经存在'
