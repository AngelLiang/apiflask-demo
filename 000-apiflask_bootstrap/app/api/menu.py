from apiflask.views import MethodView
from app.error.common import NotFoundError

from app.service.menu import MenuService
from app.serializer.menu import MenuAddIn, MenuWithChildrenOut, MenuOut, MenuUpdateIn

from app import app
from app.util.pagination import PageQueryIn, get_page_query_in
from app.auth import auth
from app.util.response import make_response

TAGS = ['基础模块/菜单按钮管理']


class MenuListApi(MethodView):

    #     @app.input(PageQueryIn, location='query')
    #     @app.output(MenuListOut)
    #     @app.doc(tags=TAGS, summary='获取菜单列表')
    #     @app.auth_required(auth)
    #     def get(self, query):
    #         page, per_page = get_page_input(query)
    #         records = get_menu_list(page, per_page)
    #         total = get_total_menu()
    #         pagination = pagination_builder(page, per_page, total)
    #         # data = {'records': records, 'pagination': pagination}
    #         data = {'records': records}
    #         data.update(pagination)
    #         return make_response(data=data)

    @app.input(MenuAddIn)
    @app.output(MenuOut)
    @app.doc(tags=TAGS, summary='创建菜单或按钮')
    @app.auth_required(auth)
    def post(self, data):
        # 校验
        serv = MenuService()
        serv.create(data)
        return make_response()


class MenuDetailApi(MethodView):

    @app.output(MenuOut)
    @app.doc(tags=TAGS, summary='获取菜单或按钮详情')
    @app.auth_required(auth)
    def get(self, pk):
        serv = MenuService()
        instance = serv.get_or_none(pk)
        if instance is None:
            raise NotFoundError()
        return make_response(data=instance)

    @app.input(MenuUpdateIn(partial=True))
    @app.output(MenuOut)
    @app.doc(tags=TAGS, summary='更新菜单或按钮详情')
    @app.auth_required(auth)
    def put(self, pk, data):
        serv = MenuService()
        serv.update(pk, data)
        return make_response()

    @app.doc(tags=TAGS, summary='删除菜单或按钮')
    @app.auth_required(auth)
    def delete(self, pk):
        serv = MenuService()
        serv.delete_by_id(pk)
        return make_response()


@app.get('/api/v1/menu/tree')
@app.output(MenuWithChildrenOut(many=True))
@app.doc(tags=TAGS, summary='获取菜单树形列表')
@app.auth_required(auth)
def get_menu_tree_api():
    serv = MenuService()
    root_menu_list = serv.get_menu_tree_list()
    return make_response(data=root_menu_list)


app.add_url_rule('/api/v1/menu', view_func=MenuListApi.as_view('menu_list'))
app.add_url_rule('/api/v1/menu/<int:menuId>', view_func=MenuDetailApi.as_view('menu_detail'))
