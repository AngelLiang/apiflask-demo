from peewee import *

from .db import BaseModel


class UnknownField(object):
    def __init__(self, *_, **__): pass


class RbacUser(BaseModel):
    username = CharField()
    name = CharField(null=True)
    password_hash = CharField(null=True)
    deleted_at = DateTimeField(null=True)
    is_active = IntegerField(constraints=[SQL("DEFAULT 1")])
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    created_by = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    updated_by = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    
    class Meta:
        table_name = 'rbac_user'


class RbacToken(BaseModel):
    created_at = DateTimeField()
    key = CharField(primary_key=True)
    user_id = IntegerField()
    user = ForeignKeyField(RbacUser, column_name='user_id', backref='tokens')


    class Meta:
        table_name = 'rbac_token'
