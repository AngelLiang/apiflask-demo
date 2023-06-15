from apiflask.views import MethodView
from app import app
from app.auth import auth
from app.serializer.role import RoleAddIn, RoleOut, RoleUpdateIn, RoleListOut
from app.service.role import RoleService
from app.util.pagination import PageQueryIn, get_page_query_in
from app.util.response import make_response, make_page_response
from app.error.common import NotFoundError

TAGS = ['基础模块/角色管理']


class RoleListApi(MethodView):

    @app.input(PageQueryIn, location='query')
    @app.output(RoleListOut)
    @app.doc(tags=TAGS, summary='获取角色列表')
    @app.auth_required(auth)
    def get(self, page_query, search=None, filter=None):
        serv = RoleService()
        query = serv.get_query()
        object_list, total = serv.get_list_and_total(query)
        return make_page_response(records=object_list, total=total)

    @app.input(RoleAddIn, example={'code': 'super', 'name': '超级管理员', 'isActive': True})
    @app.output(RoleOut)
    @app.doc(tags=TAGS, summary='创建角色')
    @app.auth_required(auth)
    def post(self, data):
        serv = RoleService()
        instance = serv.create(data)
        return make_response(data=instance)


class RoleDetailApi(MethodView):

    @app.output(RoleOut)
    @app.doc(tags=TAGS, summary='获取角色详情')
    @app.auth_required(auth)
    def get(self, pk):
        serv = RoleService()
        instance = serv.get_or_none(pk)
        if instance is None:
            raise NotFoundError()
        return make_response(data=instance)

    @app.input(RoleUpdateIn(partial=True))
    @app.output(RoleOut)
    @app.doc(tags=TAGS, summary='更新角色详情')
    @app.auth_required(auth)
    def put(self, pk, data):
        serv = RoleService()
        serv.update(pk, data)
        return make_response()

    @app.doc(tags=TAGS, summary='删除角色')
    @app.auth_required(auth)
    def delete(self, pk):
        serv = RoleService()
        serv.delete_by_id(pk)
        return make_response()


app.add_url_rule('/api/v1/role', view_func=RoleListApi.as_view('role_list'))
app.add_url_rule('/api/v1/role/<int:roleId>', view_func=RoleDetailApi.as_view('role_detail'))
