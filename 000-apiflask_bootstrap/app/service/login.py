from app.util.datetime import get_now
from app.model import RbacUser, RbacToken
from app.service.user import UserService
from app.service.password import decrypt_password
from app.error.login import UsernameOrPasswordError, DecryptPasswordError
from app.error.user import UserDenyError


def generate_key():
    import os
    import binascii
    return binascii.hexlify(os.urandom(20)).decode()


def generate_token(user_id) -> str:
    """生成token"""
    token = RbacToken.create(
        key=generate_key(),
        user_id=user_id,
        created_at=get_now(),
    )
    return token.key


def delete_all_token(user_id):
    """删除所有token"""
    query = RbacToken.delete().where(RbacToken.user_id == user_id)
    return query.execute()


def user_login(username, encrypt_password):
    """用户登录服务"""
    # try:
    #     raw_password = decrypt_password(encrypt_password)
    # except ValueError:
    #     raise DecryptPasswordError()
    raw_password = encrypt_password

    serv = UserService()
    user = serv.get_user_by_username(username)
    if not user:
        raise UsernameOrPasswordError()
    if not serv.verify_password(user, raw_password):
        # create_failure_login_log(data, exception_info='密码不正确')
        raise UsernameOrPasswordError()

    if not user.is_active:
        raise UserDenyError()

    # 删除旧的token
    delete_all_token(user.id)
    token = generate_token(user.id)
    out = {
        'token': f'Bearer {token}',
        'user_id': user.id,
    }
    # create_success_login_log(data)
    return out
