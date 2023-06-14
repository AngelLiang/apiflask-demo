from apiflask.views import MethodView
from app import app

from app.service.user import UserService
from app.util.pagination import PageQueryIn, get_page_query_in
from app.util.response import make_response, make_page_response
from app.serializer.user import UserListOut, UserAddIn, UserUpdateIn, UserOut

TAGS = ['基础模块/用户管理']


class UserListApi(MethodView):

    @app.input(PageQueryIn, location='query')
    @app.output(UserListOut)
    @app.doc(tags=TAGS, summary='获取用户列表')
    # @app.auth_required(auth)
    def get(self, page_query, search=None, filter=None):
        serv = UserService()
        query = serv.get_query()
        object_list, total = serv.get_list_and_total(query)
        return make_page_response(records=object_list, total=total)

    @app.input(UserAddIn)
    @app.output(UserOut)
    @app.doc(tags=TAGS, summary='创建用户')
    # @app.auth_required(auth)
    def post(self, data):
        serv = UserService()
        serv.create(data)
        return make_response()


# class UserDetailApi(MethodView):

#     @app.output(UserOut)
#     @app.doc(tags=TAGS, summary='获取用户详情')
#     @app.auth_required(auth)
#     def get(self, user_id):
#         user = get_user_by_id(user_id)
#         if not user:
#             abort(404)
#         return make_response(data=user)

#     @app.input(UserUpdateIn(partial=True))
#     @app.output(UserOut)
#     @app.doc(tags=TAGS, summary='更新用户详情')
#     @app.auth_required(auth)
#     def put(self, user_id, data):
#         user = get_user_by_id(user_id)
#         if not user:
#             abort(404)

#         role_ids = data.pop('role_ids', [])
#         organ_ids = data.pop('organ_ids', [])

#         updated_by = auth.current_user.username

#         with database.atomic():
#             user, diff = update_user(user, **data, updated_by=updated_by)
#             set_user_roles(user, role_ids)
#             set_user_organs(user, organ_ids)
#             diff_dict = make_diff_json(diff[0], diff[1])
#             add_user_edition_log(user, updated_by, diff_dict=diff_dict)
#         return make_response(data=user)


app.add_url_rule('/api/v1/user', view_func=UserListApi.as_view('user_list'))
# app.add_url_rule('/api/v1/user/<int:userId>', view_func=UserDetailApi.as_view('user_detail'))
