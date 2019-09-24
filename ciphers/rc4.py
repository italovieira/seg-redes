BLOCK_LENGTH = 256

def swap(S):
    def step(i, j):
        S[i], S[j] = S[j], S[i]
        return S
    return step


def ksa(key):
    keylen = len(key)

    S = list(range(BLOCK_LENGTH))  # [0,1,2, ... , 255]
    j = 0
    for i in range(BLOCK_LENGTH):
        j = (j + S[i] + key[i % keylen]) % BLOCK_LENGTH
        S[i], S[j] = S[j], S[i]  # swap values

    return S


def prga(S):
    # Stream generating
    i = 0
    j = 0

    while True:
        i = (i + 1) % BLOCK_LENGTH
        j = (j + S[i]) % BLOCK_LENGTH

        S[i], S[j] = S[j], S[i]  # swap values
        K = S[(S[i] + S[j]) % BLOCK_LENGTH]
        yield K


def gen_keystream(key):
    S = ksa(key)
    return prga(S)


class Rc4:

    def __init__(self, key : bytes):
        self.key = key


    def encrypt(self, plain_text : bytes) -> bytes:
        keystream = gen_keystream(self.key)
        return bytes([x ^ y for x, y in zip(plain_text, keystream)])


    decrypt = encrypt
