from apiflask import HTTPTokenAuth
from app.logger import logger
from apiflask import HTTPError

from app.service.token import is_expire_token, get_token_by_key
from app.service.user import get_user_by_id

auth = HTTPTokenAuth()


@auth.verify_token
def verify_token(token: str):
    """
        Bearer cb7dfb8fee4bed45bae267abf1ca519365407636
    """
    try:
        if ' ' in token:
            token_type, token_value = token.split(' ')
        else:
            token_value = token
    except ValueError as e:
        logger.error(f'{e}:token={token}')
        return None
    token = get_token_by_key(token_value)
    if token:
        if is_expire_token(token):
            logger.info(f'{token} is expired')
            token.delete_instance()
            msg = '登录已经过期，请重新登录'
            raise HTTPError(401, msg)
        user = get_user_by_id(token.user_id)
        if not user.is_active:
            msg = '该帐号已经被禁用'
            raise HTTPError(401, msg)
        return user
    return None


@auth.error_processor
def auth_error_processor(error):
    body = {
        'code': 1,
        # 'msg': '认证失败！',
        'msg': error.message,
        'data': {}
        # 'error_detail': error.detail,
        # 'status_code': error.status_code
    }
    # return body, 200, error.headers
    return body, error.status_code, error.headers


def get_current_user():
    return auth.current_user
