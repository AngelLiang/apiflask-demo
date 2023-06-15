from marshmallow import EXCLUDE

from apiflask import Schema
from apiflask.fields import Integer, String, Boolean, DateTime
from apiflask.fields import List, Nested
from apiflask.validators import Length, OneOf
from apiflask.validators import Range

from app.util.pagination import PaginationSchemaMixin


class RoleAddIn(Schema):
    code = String(title='角色编码', required=True, validate=Length(max=40), data_key='code')
    name = String(title='角色名称', required=True, validate=Length(max=40), data_key='name')
    is_active = Boolean(title='启用/禁用', data_key='isActive')


class RoleUpdateIn(Schema):
    name = String(title='角色名称', required=True, validate=Length(max=40), data_key='name')
    is_active = Boolean(title='启用/禁用', data_key='isActive')

    class Meta:
        unknown = EXCLUDE


class RoleOut(Schema):
    id = Integer()
    code = String(title='角色编码', data_key='code')
    name = String(title='角色名称', data_key='name')
    is_active = Boolean(title='启用/禁用', data_key='isActive')
    created_at = DateTime(data_key='createdAt')
    updated_at = DateTime(data_key='updatedAt')
    created_by = String(data_key='createdBy')
    updated_by = String(data_key='updatedBy')
    # permission_set = List(Nested(PermissionOut))


class RoleListOut(Schema, PaginationSchemaMixin):
    records = List(Nested(RoleOut))
