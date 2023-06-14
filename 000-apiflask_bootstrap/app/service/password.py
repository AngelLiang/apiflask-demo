import binascii
import base64
from urllib import parse

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

from apiflask import abort


def decrypt_password(encrypt_password):

    # URLDecode
    encrypt_password = parse.unquote(encrypt_password)
    # base64decode
    try:
        encrypt_password = base64.b64decode(encrypt_password)
    except binascii.Error:
        abort(401)
    # 读取密钥
    private_key = RSA.import_key(open("rsa_key/rsa_key.bin").read())
    cipher_rsa = PKCS1_v1_5.new(private_key)
    data = cipher_rsa.decrypt(encrypt_password, None)
    return data.decode()
