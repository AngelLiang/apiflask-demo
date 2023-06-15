from marshmallow import EXCLUDE

from apiflask import Schema
from apiflask.fields import Integer, String, Boolean, DateTime
from apiflask.fields import List, Nested
from apiflask.validators import Length, OneOf
from apiflask.validators import Range
from app.util.pagination import PaginationSchemaMixin


class MenuAddIn(Schema):
    name = String(required=True, validate=Length(max=40))
    type = Integer(title='菜单类型 （0菜单 1按钮）', validate=OneOf([0, 1]))
    is_active = Boolean(title='启用/禁用', data_key='isActive')
    parent_id = Integer(title='父级菜单id', data_key='parentId', load_default=-1)
    permission_code = String(title='权限编码 （按钮特有）', required=False, validate=Length(max=40), data_key='permissionCode')
    url = String(title='url （菜单特有）', load_default='')
    icon = String(title='图标 （菜单特有）', load_default='')
    sort = Integer(title='排序', load_default=100)


class MenuUpdateIn(MenuAddIn):
    pass


class MenuOut(Schema):
    id = Integer(title='菜单id')
    name = String(title='菜单名称')
    is_active = Boolean(title='启用/禁用', data_key='isActive')
    sort = Integer(title='排序')
    parent_id = Integer(title='父级菜单id', data_key='parentId')
    type = Integer(title='菜单类型 （0菜单 1按钮）')
    permission_code = String(title='权限编码 （按钮特有）', data_key='permissionCode')
    url = String(title='url （菜单特有）')
    icon = String(title='图标 （菜单特有）')

    created_at = DateTime(data_key='createdAt')
    updated_at = DateTime(data_key='updatedAt')
    created_by = String(data_key='createdBy')
    updated_by = String(data_key='updatedBy')


class MenuListOut(Schema, PaginationSchemaMixin):
    records = List(Nested(MenuOut))


class MenuWithChildrenOut(MenuOut):
    children = List(Nested(lambda: MenuWithChildrenOut), title='子菜单')
