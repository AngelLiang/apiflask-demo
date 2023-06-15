
from app.auth import auth
from app.util.response import make_response
from app.service.menu import MenuService
from app.service.current_user import get_user_cen_use_menu_list, get_user_can_use_permission_code_list

from app import app
from app.serializer.current_user import CurrentUserOut

from .user import TAGS


@app.get('/api/v1/currentUser')
@app.doc(summary='获取当前用户信息和可用菜单按钮集合', tags=TAGS)
@app.output(CurrentUserOut)
@app.auth_required(auth)
def get_current_user_api():
    data = {
        'user_id': auth.current_user.id,
        'username': auth.current_user.username,
        'name': auth.current_user.name,
        'is_active': auth.current_user.is_active,
    }
    data['can_use_menu_set'] = get_user_cen_use_menu_list(auth.current_user, is_root=True)
    data['can_use_permission_code_set'] = get_user_can_use_permission_code_list(auth.current_user)
    # data['organ_set'] = get_user_organ_list(auth.current_user)
    data['role_set'] = auth.current_user.role_set
    return make_response(0, '操作成功！', data)
