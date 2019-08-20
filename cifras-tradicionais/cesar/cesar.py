import sys


CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ?,'


def rotate(n, c):
    try:
        i = CHARS.index(c)
        return CHARS[(i + n) % len(CHARS)]
    except ValueError:
        return c


def transform(n, msg):
    return [rotate(n, c) for c in msg]


def main():
    msg = sys.stdin.readlines()

    for i in range(1, len(CHARS)):
        print()
        print("#" + str(i))
        print()
        print()
        for line in msg:
            print(''.join(transform(i, line)), end='')
        print()
        print('############################################################')


if __name__ == '__main__':
    main()
