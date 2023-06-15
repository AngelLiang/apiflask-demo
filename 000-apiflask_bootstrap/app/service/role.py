from typing import Dict
from app.model import RbacRole
from app.service.base import BaseService
from app.util.datetime import get_now
from app.error.common import NotFoundError
from app.error.role import RoleCodeExistError

from app.auth import get_current_user


class RoleService(BaseService):
    model_class = RbacRole

    def is_code_exists(self, code: str) -> bool:
        return self.get_query().where(RbacRole.code == code).first()

    def create(self, data: Dict):
        code = data['code']
        if self.is_code_exists(code):
            raise RoleCodeExistError()
        data['created_at'] = get_now()
        data['updated_at'] = get_now()

        from app.auth import get_current_user
        current_user = get_current_user()
        if current_user:
            data['created_by'] = get_current_user().username
            data['updated_by'] = get_current_user().username

        instance = self.model_class(**data)
        instance.save()
        return instance
