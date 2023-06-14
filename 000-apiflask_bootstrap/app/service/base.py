from typing import List, Tuple, Dict
from app.util.datetime import get_now
from app.util.pagination import PaginatedQuery


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

    def update(self, pk, data: Dict):
        instance = self.get_or_none(pk)
        if not instance:
            return None
        # data['updated_at'] = get_now()
        return instance.set_by_id(pk, data)

    def delete(self, instance):
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
