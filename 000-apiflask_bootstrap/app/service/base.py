from typing import List, Tuple, Dict
from app.util.datetime import get_now
from app.util.pagination import PaginatedQuery
from app.error.common import NotFoundError


class BaseService:
    model_class = None

    def __init__(self) -> None:
        pass

    def get_list_and_total(self, query_or_model=None, page=None, per_page=None):
        if query_or_model is None:
            query_or_model = self.get_query()
        paginated_query = PaginatedQuery(query_or_model, per_page=per_page, page=page)
        object_list = paginated_query.get_object_list()
        total = paginated_query.get_object_total()
        return object_list, total

    def get_or_none(self, pk):
        query = self.get_query()
        return query.where(self.model_class.id == pk).first()

    def create(self, data: Dict):
        from app.auth import get_current_user
        data['created_at'] = get_now()
        data['updated_at'] = get_now()
        current_user = get_current_user()
        if current_user:
            data['created_by'] = get_current_user().username
            data['updated_by'] = get_current_user().username
        instance = self.model_class(**data)
        instance.save()
        return instance

    def update(self, pk, data: Dict):
        from app.auth import get_current_user
        instance = self.get_or_none(pk)
        if not instance:
            raise NotFoundError()
        data['updated_at'] = get_now()
        current_user = get_current_user()
        if current_user:
            data['updated_by'] = get_current_user().username
        instance.set_by_id(pk, data)
        return instance

    def delete(self, instance):
        instance.deleted_at = get_now()
        return instance.save()

    def delete_by_id(self, pk):
        instance = self.get_or_none(pk)
        if not instance:
            raise NotFoundError()
        instance.deleted_at = get_now()
        return instance.save()

    def search_by_keys(self, term, keys: List, query=None):
        if query is None:
            query = self.get_query()
        if len(keys) == 1:
            attr = getattr(self.model_class, keys[0])
            query = query.where(attr.contains(term))
        else:
            condition_list = getattr(self.model_class, keys[0]).contains(term)
            for key in keys[1:]:
                attr = getattr(self.model_class, key)
                condition_list |= attr.contains(term)
            query = query.where(condition_list)
        return query

    def get_total(self, query=None):
        if query is None:
            query = self.get_query()
        return query.count()

    def get_query(self):
        if hasattr(self.model_class, 'deleted_at'):
            return self.model_class.select().where(self.model_class.deleted_at == None)
        else:
            return self.model_class.select()
