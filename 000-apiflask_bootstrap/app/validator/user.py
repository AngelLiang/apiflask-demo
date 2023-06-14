import re
from marshmallow import ValidationError


def validate_username(value):
    """用户名只能包含大小写字母和数字"""
    if not re.match('^[a-zA-Z0-9]{3,20}$', value):
        raise ValidationError('用户名不合法')
