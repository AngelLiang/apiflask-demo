from marshmallow import EXCLUDE

from apiflask import Schema
from apiflask.fields import Integer, String, Boolean, DateTime
from apiflask.fields import List, Nested
from apiflask.validators import Length, OneOf
from apiflask.validators import Range

from app.validator.user import validate_username
from app.util.pagination import PaginationSchemaMixin


class UserAddIn(Schema):
    username = String(title='用户名', required=True, validate=[
        Length(max=80), validate_username
    ])
    password = String(title='密码', required=True)
    name = String(title='名称', validate=[Length(max=80)])
    is_active = Boolean(title='启用/禁用', data_key='isActive')

    role_ids = List(Integer, title='设置角色id集合', data_key='roleIds')
    # organ_ids = List(Integer, title='设置组织id集合', data_key='organIds')

    class Meta:
        ordered = True


class UserOut(Schema):
    id = Integer()
    username = String(title='用户名')
    name = String(title='名称')
    is_active = Boolean(title='启用/禁用', data_key='isActive')
    created_at = DateTime(data_key='createdAt')
    updated_at = DateTime(data_key='updatedAt')
    created_by = String(data_key='createdBy')
    updated_by = String(data_key='updatedBy')

    # role_set = List(Nested(RoleOut), title='所属角色集合', data_key='roleSet')
    # organ_set = List(Nested(OrganOut), title='所属组织集合', data_key='organSet')

    class Meta:
        ordered = True


class UserUpdateIn(Schema):
    name = String(title='名称')
    is_active = Boolean(title='启用/禁用', data_key='isActive')

    role_ids = List(Integer, title='设置角色id集合', data_key='roleIds')
    # organ_ids = List(Integer, title='设置组织id集合', data_key='organIds')

    class Meta:
        ordered = True
        unknown = EXCLUDE


class UserListOut(Schema, PaginationSchemaMixin):
    records = List(Nested(UserOut))


def make_user_list_out(object_list, total):
    return {
        'records': object_list,
        'total': total,
    }
