def shift(n):
    first_bit = n >> 4
    return ((n & 0b1111) << 1) + first_bit

def get_bit(i, n):
    return n >> (10 - i) & 1

def transform(p, n):
    list_p = [(get_bit(i, n) << (len(p) - index - 1)) for index, i in enumerate(p)]
    return sum(list_p)

def p10(n):
    P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    return transform(P10, n)

def p8(n):
    P8 = [6, 3, 7, 4, 8, 5, 10, 9]
    return transform(P8, n)

def split10(n):
    return (n >> 5, n & 0b11111)


def split8(n):
    return (n >> 4, n & 0b1111)

def join(n1, n2):
    return (n1 << 5) + n2


def gen_keys(key):
    print(bin(p10(key)))
    (a, b) = split10(p10(key))
    print(bin(a), bin(b))
    shifted1_a = shift(a)
    shifted1_b = shift(b)
    print(bin(shifted1_a), bin(shifted1_b))
    rejoin = join(shifted1_a, shifted1_b)
    print(bin(rejoin))
    k1 = p8(join(shifted1_a, shifted1_b))



    shifted3_a = shift(shift1(shifted1_a))
    shifted3_b = shift(shift1(shifted1_b))

    k2 = p8(join(shifted3_a, shifted3_b))

    print(k1, k2)
    return (k1, k2)


def ep(key):
    EP = [4, 1, 2, 3, 2, 3, 4, 1]
    return transform(EP, key)

def encrypt(text):
    (_, right) = split8(p8(text))
    return ep(right)
