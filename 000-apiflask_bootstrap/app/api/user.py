from apiflask.views import MethodView
from app import app
from app.auth import auth
from app.service.user import UserService
from app.util.pagination import PageQueryIn, get_page_query_in
from app.util.response import make_response, make_page_response
from app.serializer.user import UserListOut, UserAddIn, UserUpdateIn, UserOut
from app.error.common import NotFoundError

TAGS = ['基础模块/用户管理']


class UserListApi(MethodView):

    @app.input(PageQueryIn, location='query')
    @app.output(UserListOut)
    @app.doc(tags=TAGS, summary='获取用户列表')
    @app.auth_required(auth)
    def get(self, page_query, search=None, filter=None):
        serv = UserService()
        query = serv.get_query()
        object_list, total = serv.get_list_and_total(query)
        return make_page_response(records=object_list, total=total)

    @app.input(UserAddIn)
    @app.output(UserOut)
    @app.doc(tags=TAGS, summary='创建用户')
    @app.auth_required(auth)
    def post(self, data):
        serv = UserService()
        serv.create(data)
        return make_response()


class UserDetailApi(MethodView):

    @app.output(UserOut)
    @app.doc(tags=TAGS, summary='获取用户详情')
    @app.auth_required(auth)
    def get(self, pk):
        serv = UserService()
        instance = serv.get_or_none(pk)
        if instance is None:
            raise NotFoundError()
        return make_response(data=instance)

    @app.input(UserUpdateIn(partial=True))
    @app.output(UserOut)
    @app.doc(tags=TAGS, summary='更新用户详情')
    @app.auth_required(auth)
    def put(self, pk, data):
        serv = UserService()
        serv.update(pk, data)
        return make_response()


app.add_url_rule('/api/v1/user', view_func=UserListApi.as_view('user_list'))
app.add_url_rule('/api/v1/user/<int:userId>', view_func=UserDetailApi.as_view('user_detail'))
