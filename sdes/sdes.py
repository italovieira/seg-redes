def shift(n, byte):
    return byte << n

def get_bit(i, byte):
    return byte >> (i - 1) & 1

def transform(p, byte):
    return [get_bit(i, byte) for i in p]

def p10(byte):
    P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    return transform(P10, byte)

def p8(byte):
    P8 = [6, 3, 7, 4, 8, 5, 10, 9]
    return transform(P8, byte)

def split(byte):
    return [(byte & (15 << 4)) >> 4, byte & 15]
