from typing import Dict
from app.model import RbacUser
from app.util.password_hasher import make_password, check_password
from app.service.base import BaseService
from app.error import UsernameExistError


class UserService(BaseService):
    model_class = RbacUser

    def is_username_exists(self, username: str) -> bool:
        return self.get_query().where(self.model_class.username == username)

    # @db_wrapper.database.atomic()
    def create(self, data: Dict):
        username = data['username']
        # 判断是否存在相同用户名
        if self.is_username_exists(username):
            raise UsernameExistError()

        role_ids = data.pop('role_ids', None)
        user = RbacUser(**data)
        return user.save()
        # created_by = auth.current_user.username
        # updated_by = auth.current_user.username
        # with database.atomic():
        #     user = create_user(**data, created_by=created_by, updated_by=updated_by)
        #     set_user_roles(user, role_ids)
        #     set_user_organs(user, organ_ids)
        #     add_user_creation_log(user, created_by)

    def get_user_by_username(self, username):
        return RbacUser.get_or_none(RbacUser.username == username)

    def verify_password(self, user: RbacUser, raw_password) -> bool:
        """验证密码"""
        return check_password(raw_password, user.password_hash)

    def change_password(self, user: RbacUser, new_password):
        """修改密码"""
        user.password_hash = make_password(new_password)
        return user.save()
