def shift(n, key):
    return key << n

def shift1(n):
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

def split(n):
    return (n >> 5, n & 0b11111)

def join(n1, n2):
    return (n1 << 5) + n2


def k1(key):
    (a, b) = split(p10(key))
    print(bin(p10(key)))
    print(bin(a), bin(b))
    print(bin(shift1(a)), bin(shift1(b)))
    rejoin = join(shift1(a), shift1(b))
    print(bin(rejoin))
    return p8(join(shift1(a), shift1(b)))
