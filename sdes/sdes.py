def shift(n):
    first_bit = n >> 4
    return ((n & 0b1111) << 1) + first_bit


def get_bit(i, n, block_length):
    return n >> (block_length - i) & 1


def permute(p, n, block_length=None):
    len_p = len(p)

    if block_length is None:
        block_length = len_p

    list_p = [(get_bit(i, n, block_length) << (len_p - index - 1)) for index, i in enumerate(p)]
    return sum(list_p)


def p10(n):
    P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    return permute(P10, n)


def p8(n):
    P8 = [6, 3, 7, 4, 8, 5, 10, 9]
    return permute(P8, n, 10)


def split(n, block_length):
    # Generate n-binary with the bits set
    gen_bin = lambda n : (1 << n - 1) * 2 - 1

    half_size = block_length // 2
    return (n >> half_size, n & gen_bin(half_size))


def split10(n):
    return split(n, 10)


def split8(n):
    return split(n, 8)


def ip(n):
    IP = [2, 6, 3, 1, 4, 8, 5, 7]
    return permute(IP, n)


def inverse_ip(n):
    INVERSE_IP = [4, 1, 3, 5, 7, 2, 8, 6]
    return permute(INVERSE_IP, n)


def join(half_length):
    return lambda n1, n2 : (n1 << half_length) + n2


join2 = join(1)
join4 = join(2)
join8 = join(4)
join10 = join(5)


def gen_keys(key):
    #print(bin(p10(key)))
    (a, b) = split10(p10(key))
    #print(bin(a), bin(b))
    shifted1_a = shift(a)
    shifted1_b = shift(b)
    #print(bin(shifted1_a), bin(shifted1_b))
    k1 = p8(join10(shifted1_a, shifted1_b))

    shifted3_a = shift(shift(shifted1_a))
    shifted3_b = shift(shift(shifted1_b))

    k2 = p8(join10(shifted3_a, shifted3_b))

    #print(bin(k1), bin(k2))
    return (k1, k2)


def s_box(box, n):
    first_bit = get_bit(1, n, 4)
    second_bit = get_bit(2, n, 4)
    third_bit = get_bit(3, n, 4)
    last_bit = get_bit(4, n, 4)

    row = join2(first_bit, last_bit)
    col = join2(second_bit, third_bit)
    print("first ", first_bit)
    print("second ", second_bit)
    print("third ", third_bit)
    print("last ", last_bit)
    print("row ", row, " | col ", col)

    return box[row][col]


def s0(n):
    S0 = [[0b01, 0b00, 0b11, 0b10],
          [0b11, 0b10, 0b01, 0b00],
          [0b00, 0b10, 0b01, 0b11],
          [0b11, 0b01, 0b11, 0b10]]

    return s_box(S0, n)


def s1(n):
    S1 = [[0b00, 0b01, 0b10, 0b11],
          [0b10, 0b00, 0b01, 0b11],
          [0b11, 0b00, 0b01, 0b00],
          [0b10, 0b01, 0b00, 0b11]]

    return s_box(S1, n)


def ep(key):
    EP = [4, 1, 2, 3, 2, 3, 4, 1]
    return permute(EP, key, 4)


def p4(n):
    P4 = [2, 4, 3, 1]
    return permute(P4, n, 4)


def F(p, key):
    xor = ep(p) ^ key
    (a, b) = split8(xor)

    step7 = join4(s0(a), s1(b))

    return p4(step7)


def fk(k):
    return lambda left, right : (left ^ F(right, k), right)


def encrypt(key):
    def steps(plain_text):
        (k1, k2) = gen_keys(key)
        (left, right) = split8(ip(plain_text))

        (fk1_left, fk1_right) = fk(k1)(left, right)

        (fk2_left, fk2_right) = fk(k2)(fk1_right, fk1_left)

        return inverse_ip(join8(fk2_left, fk2_right))

    return steps


def decrypt(key):
    def steps(cipher_text):
        (k1, k2) = gen_keys(key)

        (left, right) = split8(ip(cipher_text))

        (fk2_left, fk2_right) = fk(k2)(left, right)

        (fk1_left, fk1_right) = fk(k1)(fk2_right, fk2_left)

        return inverse_ip(join8(fk1_left, fk1_right))

    return steps
