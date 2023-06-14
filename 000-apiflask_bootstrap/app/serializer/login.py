from apiflask import Schema
from apiflask.fields import Integer, String, Boolean, DateTime
from apiflask.validators import Length


class LoginIn(Schema):
    username = String(required=True, validate=[Length(max=80)])
    password = String(required=True)

    class Meta:
        ordered = True


class TokenOut(Schema):
    token = String()
    user_id = Integer(data_key='userId')
