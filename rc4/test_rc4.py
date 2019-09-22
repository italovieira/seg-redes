from rc4 import *

def test_encrypt():
    assert encrypt([1, 2, 3, 6])([1, 2, 2, 2]) == [4, 3, 2, 3]

def test_decrypt():
    assert decrypt([1, 2, 3, 6])([4, 3, 2, 3]) == [1, 2, 2, 2]
