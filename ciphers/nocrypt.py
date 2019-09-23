from .crypt_base import CryptBase


class Nocrypt(CryptBase):

    def encrypt(self, x):
        return x

    decrypt = encrypt
