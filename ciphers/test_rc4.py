from rc4 import *


def test_encrypt():
    key = bytes([1, 2, 3, 6])
    plaintext = bytes([1, 2, 2, 2])
    cyphertext = bytes([4, 3, 2, 3])

    assert list(Rc4(key).encrypt(plaintext)) == list(cyphertext)


def test_decrypt():
    key = bytes([1, 2, 3, 6])
    cyphertext = bytes([4, 3, 2, 3])
    plaintext = bytes([1, 2, 2, 2])

    assert list(Rc4(key).decrypt(cyphertext)) == list(plaintext)
