import hmac
import hashlib
import base64
import lzstring
from Crypto.Cipher import AES


def generate_signature(secret, message):
    sign = hmac.new(key=secret.encode(), msg=message.encode(), digestmod=hashlib.sha256).digest()
    encode_sign = base64.encodebytes(sign).replace(b'\n', b'').decode()
    return encode_sign


def decrypt_data(
        cons_id,
        secret_key,
        timestamp,
        data
):
    key_hash = f'{cons_id}{secret_key}{timestamp}'
    key_hash = hashlib.sha256(key_hash.encode()).digest()

    lz = lzstring.LZString()

    decrypt = AES.new(key_hash[0:32], AES.MODE_CBC, IV=key_hash[0:16])
    plain = decrypt.decrypt(base64.b64decode(data))
    decompress = lz.decompressFromEncodedURIComponent(plain.decode())
    return decompress

