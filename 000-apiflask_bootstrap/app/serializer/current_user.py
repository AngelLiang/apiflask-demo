from apiflask import Schema
from apiflask.fields import String, Integer, Boolean
from apiflask.fields import List, Nested

from app.serializer.menu import MenuWithChildrenOut
from app.serializer.role import RoleOut


class CurrentUserOut(Schema):
    user_id = Integer(title='用户id', data_key='userId')
    username = String(title='用户名')
    name = String(title='名称')
    is_active = Boolean(title='启用/禁用', data_key='isActive')
    can_use_menu_set = List(Nested(MenuWithChildrenOut), title='可用菜单集合', data_key='canUseMenuSet')
    can_use_permission_code_set = List(String, title='可用权限编码集合', data_key='canUsePermissionCodeSet')
    role_set = List(Nested(RoleOut), title='分配的角色', data_key='roleSet')
    # organ_set = List(Nested(OrganOut), title='所属组织', data_key='organSet')
