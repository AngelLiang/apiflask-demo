from typing import Dict, List
from app.model import Menu, RbacUser, MenuRole, RbacRole, RbacUserRole
from app.service.base import BaseService
from app import const
from app.util.datetime import get_now


class MenuService(BaseService):
    model_class = Menu

    def create(self, data: Dict):
        # super().create(data)
        # if self.is_username_exists(username):
        #     raise UsernameExistError()
        data['created_at'] = get_now()
        data['updated_at'] = get_now()

        from app.auth import get_current_user
        current_user = get_current_user()
        if current_user:
            data['created_by'] = get_current_user().username
            data['updated_by'] = get_current_user().username

        instance = Menu(**data)
        return instance.save()

    def get_menu_tree_list(self) -> List:
        query = self.get_query().where(Menu.parent == const.ROOT_MENU)
        return [item for item in query]
