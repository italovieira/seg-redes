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


def join(n1, n2):
    return (n1 << 5) + n2


def gen_keys(key):
    #print(bin(p10(key)))
    (a, b) = split10(p10(key))
    #print(bin(a), bin(b))
    shifted1_a = shift(a)
    shifted1_b = shift(b)
    #print(bin(shifted1_a), bin(shifted1_b))
    rejoin = join(shifted1_a, shifted1_b)
    #print(bin(rejoin))
    k1 = p8(join(shifted1_a, shifted1_b))

    shifted3_a = shift(shift(shifted1_a))
    shifted3_b = shift(shift(shifted1_b))

    k2 = p8(join(shifted3_a, shifted3_b))

    #print(bin(k1), bin(k2))
    return (k1, k2)


def s_box(box, n):
    first_bit = get_bit(0, n, 4)
    second_bit = get_bit(1, n, 4)
    third_bit = get_bit(2, n, 4)
    last_bit = get_bit(3, n, 4)

    row = join(first_bit, last_bit)
    col = join(second_bit, third_bit)
    print("first ", first_bit)
    print("second ", second_bit)
    print("third ", third_bit)
    print("last ", last_bit)
    print("row ", row, " | col ", col)

    return box[row - 1][col - 1]


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


def encrypt(plain_text):
    def step(block, key, table):
        print(bin(ip(plain_text)))
        (left, right) = split8(ip(plain_text))
        print(bin(right))
        print(bin(ep(right)))

        xor = ep(right) ^ key
        print(bin(xor))

        (a1, b1) = split8(xor)

        step7 = join(s0(a1), s1(b1))

        step8 = p4(step7)

        step9 = step8 ^ left

        step10 = join(step9, right)

        (a2, b2) = split8(step10)
        return join(b2, a2)

####################################################################################################
    (k1, k2) = gen_keys(0b1010000010)
    return step(step(plain_text, k1, ip), k2, inverse_ip)
