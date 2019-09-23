BLOCK_LENGTH = 256

def swap(S):
    def step(i, j):
        S[i], S[j] = S[j], S[i]
        return S
    return step


def initialize(key):
    S = list(range(BLOCK_LENGTH))
    keylen = len(key)
    T = [key[i % keylen] for i in S]
    return (S, T)


def permutation(S, T):
    j = 0
    for i in range(BLOCK_LENGTH):
        j = (j + S[i] + T[i]) % BLOCK_LENGTH
        S = swap(S)(i, j)

    return S


def gen_stream(S):
    # Stream generating
    i = 0
    j = 0

    while True:
        i = (i + 1) % BLOCK_LENGTH
        j = (j + S[i]) % BLOCK_LENGTH
        S = swap(S)(i, j)
        t = (S[i] + S[j]) % BLOCK_LENGTH
        k = S[t]
        yield k



class Rc4:

    def __init__(self, key : bytes):
        self.S = permutation(*initialize(list(key)))


    def encrypt(self, plain_text : bytes) -> bytes:
        stream = gen_stream(self.S)
        return bytes([x ^ y for x, y in zip(plain_text, stream)])


    decrypt = encrypt
