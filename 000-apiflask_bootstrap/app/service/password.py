import binascii
import base64
from urllib import parse

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

from app.error.login import DecryptPasswordError


def encrypt_password(raw_password):
    recipient_key = RSA.import_key(open("rsa_key/rsa_pub.pem").read())
    cipher_rsa = PKCS1_v1_5.new(recipient_key)

    en_data = cipher_rsa.encrypt(raw_password.encode())
    return en_data


def decrypt_password(encrypt_password):
    # URLDecode
    encrypt_password = parse.unquote(encrypt_password)
    # base64decode
    try:
        encrypt_password = base64.b64decode(encrypt_password)
    except binascii.Error:
        raise DecryptPasswordError()
    # 读取密钥
    private_key = RSA.import_key(open("rsa_key/rsa_key.bin").read())
    cipher_rsa = PKCS1_v1_5.new(private_key)
    data = cipher_rsa.decrypt(encrypt_password, None)
    return data.decode()
