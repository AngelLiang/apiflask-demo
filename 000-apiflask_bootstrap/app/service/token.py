import datetime
from app.model import RbacToken, RbacUser
from app import setting

TOKEN_EXPIRED_SECONDS = getattr(setting, 'TOKEN_EXPIRED_SECONDS', 7*24*60*60)

def get_token_by_key(key) -> RbacToken:
    return RbacToken.get_or_none(RbacToken.key == key)


def is_expire_token(token: RbacToken, seconds=TOKEN_EXPIRED_SECONDS) -> bool:
    now = datetime.datetime.now()
    expire_time = now - datetime.timedelta(seconds=seconds)
    # expire_day = today-datetime.timedelta(hours=24)
    return token.created_at < expire_time


def clean_expire_token(seconds=TOKEN_EXPIRED_SECONDS):
    """清除过期的token"""
    now = datetime.datetime.now()
    expire_time = now - datetime.timedelta(seconds=seconds)
    query = RbacToken.delete().where(RbacToken.created_at < expire_time)
    query.execute()


def get_user_by_token(key: str):
    token = RbacToken.get_or_none(RbacToken.key == key)
    if token:
        return token.user
