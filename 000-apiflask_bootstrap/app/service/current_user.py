from typing import List, Dict
from app.service.menu import MenuService
from app.model import Menu
from app.model import MenuRole
from app.model import RbacUser, RbacRole, RbacUserRole

from app import const


def get_user_children_menu(user: RbacUser, parent_menu: Dict) -> List:
    """递归获取用户可用的菜单"""
    parent_id = parent_menu['id']
    query = MenuService().get_query()
    query = query.join(MenuRole).join(RbacRole).join(RbacUserRole).where(
        Menu.id == MenuRole.menu_id,
        MenuRole.role_id == RbacRole.id,
        RbacRole.id == RbacUserRole.role_id,
        RbacUserRole.user_id == user.id,
    ).distinct()
    children = query.where(
        Menu.parent_id == parent_id,
        Menu.is_active == True
    ).order_by(Menu.sort).dicts()
    for child in children:
        # 递归获取子菜单
        child['children'] = get_user_children_menu(user, child)
    return children

def get_user_cen_use_menu_list(user: RbacUser, is_root=True) -> List:
    """
    获取用户的菜单列表，只返回启用的菜单
    """
    query = MenuService().get_query()
    query = query.join(MenuRole).join(RbacRole).join(RbacUserRole).where(
        Menu.id == MenuRole.menu_id,
        MenuRole.role_id == RbacRole.id,
        RbacRole.id == RbacUserRole.role_id,
        RbacUserRole.user_id == user.id,
    ).distinct()
    if is_root:
        query = query.where(Menu.parent == const.ROOT_MENU)
    query = query.where(Menu.is_active == True).order_by(Menu.sort)

    data = query.dicts()
    for item in data:
        item['children'] = get_user_children_menu(user, item)
    return data


def get_user_can_use_permission_code_list(user: RbacUser) -> List:
    """获取用户可用的权限code列表"""
    query = MenuService().get_query()
    query = query.join(MenuRole).join(RbacRole).join(RbacUserRole).where(
        Menu.id == MenuRole.menu_id,
        MenuRole.role_id == RbacRole.id,
        RbacRole.id == RbacUserRole.role_id,
        RbacUserRole.user_id == user.id,
        Menu.is_active == True,
    )
    result = []
    for row in query:
        if row.permission_code:
            result.append(row.permission_code)
    return result
