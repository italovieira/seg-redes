from sdes import *


def test_p10():
    assert p10(0b1010000010) == 0b1000001100


def test_split10():
    assert split10(0b1000001100) == (0b10000, 0b01100)


def test_shift():
    assert shift(0b10000) == 0b00001


def test_join():
    assert join(0b00001, 0b11000) == 0b0000111000


def test_p8():
    assert p8(0b0000111000) == 0b10100100


def test_ip():
    assert ip(0b01110010) == 0b10101001


def test_split8():
    assert split8(0b10101001) == (0b1010, 0b1001)


def test_ep():
    assert ep(0b1000) == 0b01000001


def test_s0():
    assert s0(0b1110) == 0b00


def test_s1():
    assert s1(0b0101) == 0b11


def test_join_half_length4():
    assert join(0b10, 0b11) == 0b1011


def test_join_half_length8():
    assert join(0b1010, 0b1001) == 0b10101001


def test_p4():
    assert p4(0b0011) == 0b0110

