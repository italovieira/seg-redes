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


def gen_stream(S, plain_text):
    # Stream generating
    i = 0
    j = 0

    cypher_text = []
    for block in plain_text:
        i = (i + 1) % BLOCK_LENGTH
        j = (j + S[i]) % BLOCK_LENGTH
        S = swap(S)(i, j)
        t = (S[i] + S[j]) % BLOCK_LENGTH
        k = S[t]
        cypher_text.append(k ^ block)

    return cypher_text


def encrypt(key):
    S = permutation(*initialize(key))

    def steps(plain_text):
        return gen_stream(S, plain_text)

    return steps


def decrypt(key):
    return encrypt(key)
