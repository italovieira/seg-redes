from sdes import *


def test_p10():
    assert p10(0b1010000010) == 0b1000001100


def test_split10():
    assert split10(0b1000001100) == (0b10000, 0b01100)


def test_shift():
    assert shift(0b10000) == 0b00001


def test_join4():
    assert join4(0b10, 0b11) == 0b1011


def test_join8():
    assert join8(0b1010, 0b1001) == 0b10101001


def test_join10():
    assert join10(0b00001, 0b11000) == 0b0000111000


def test_p8():
    assert p8(0b0000111000) == 0b10100100


def test_ip():
    assert ip(0b01110010) == 0b10101001


def test_split8():
    assert split8(0b10101001) == (0b1010, 0b1001)


def test_ep():
    assert ep(0b1000) == 0b01000001


def test_s0():
    assert s0(0b1111) == 0b10


def test_s1():
    assert s1(0b1110) == 0b00


def test_p4():
    assert p4(0b0011) == 0b0110


def test_F():
    assert F(0b0010, 0b11101001) == 0b0001


def test_fk():
    assert fk(0b10100111)(0b0010, 0b0011) == (0b0001, 0b0011)


def test_inverse_ip():
    assert inverse_ip(0b00010011) == 0b10001010


def test_k1():
    (k1, _) = gen_keys(0b1100011110)
    assert k1 == 0b11101001


def test_k2():
    (_, k2) = gen_keys(0b1100011110)
    assert k2 == 0b10100111


def test_encrypt_block():
    assert Sdes(0b1100011110).encrypt_block(0b00101000) == 0b10001010


def test_decrypt_block():
    assert Sdes(0b1100011110).decrypt_block(0b10001010) == 0b00101000
