from rc4 import *


def test_encrypt():
    assert Rc4([1, 2, 3, 6]).encrypt([1, 2, 2, 2]) == [4, 3, 2, 3]


def test_decrypt():
    assert Rc4([1, 2, 3, 6]).decrypt([4, 3, 2, 3]) == [1, 2, 2, 2]
