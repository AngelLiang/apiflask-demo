from flask import current_app
from apiflask import APIFlask, HTTPTokenAuth, Schema, abort
from apiflask.fields import String, Field
from apiflask.validators import Length


app = APIFlask(__name__)
# auth = HTTPTokenAuth()
app.config['SECRET_KEY'] = 'secret-key'


# @auth.verify_token
# def verify_token(token: str):
#     try:
#         token_type, token_value = token.split(' ')
#     except ValueError:
#         pass


def decrypt_password(encrypt_password):
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_v1_5
    import base64
    from urllib import parse
    import binascii

    # URLDecode
    encrypt_password = parse.unquote(encrypt_password)
    # base64decode
    try:
        encrypt_password = base64.b64decode(encrypt_password)
    except binascii.Error:
        abort(401)
    # 读取密钥
    private_key = RSA.import_key(open("rsa_key.bin").read())
    cipher_rsa = PKCS1_v1_5.new(private_key)
    data = cipher_rsa.decrypt(encrypt_password, None)
    return data.decode()


class LoginSchema(Schema):
    username = String(required=True, validate=[Length(max=80)])
    password = String(required=True)


class TokenOut(Schema):
    token = String()
    data = Field()


@app.post('/login')
@app.input(LoginSchema)
@app.output(TokenOut)
@app.doc(summary='用户登录', tags=['登录认证'])
def login(data):
    username = data['username']
    password = data['password']
    password = decrypt_password(password)
    print(f'{username}密码解密成功：{password}')
    return {
        'data': {
            'username': username,
            'password': password
        },
        'token': f'Bearer <token>',
    }
