from apiflask import Schema, fields


class BaseResponse(Schema):
    code = fields.Integer(load_default=0)
    msg = fields.String(load_default='操作成功！')
    data = fields.Field()  # the data key


def make_response(code=0, msg='操作成功！', data=None):
    return {'code': code, 'msg': msg, 'data': data}
