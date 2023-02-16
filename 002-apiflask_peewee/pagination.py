from flask import request
from peewee import SelectQuery


class PaginatedQuery(object):
    def __init__(self, query_or_model, per_page_var='size', per_page=None, page_var='current', page=None):
        self.per_page = per_page
        self.page_var = page_var
        self.per_page_var = per_page_var
        self.page = page

        if isinstance(query_or_model, SelectQuery):
            self.query = query_or_model
            self.model = self.query.model
        else:
            self.model = query_or_model
            self.query = self.model.select()

    def get_per_page(self):
        if self.per_page is not None:
            return self.per_page

        per_page = request.args.get(self.per_page_var)
        if per_page and per_page.isdigit():
            return max(1, int(per_page))
        return None

    def get_page(self):
        if self.page is not None:
            return self.page

        curr_page = request.args.get(self.page_var)
        if curr_page and curr_page.isdigit():
            return max(1, int(curr_page))
        return 1

    def get_object_list(self):
        per_page=self.get_per_page()
        page=self.get_page()
        if per_page and page:
            return self.query.paginate(page, per_page)
        return self.query

    def get_object_total(self):
        return self.query.count()
