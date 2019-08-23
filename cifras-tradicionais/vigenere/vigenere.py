import sys

CHARS = 'abcdefghijklmnopqrstuvwxyz'

# data: possible keys
FILENAME = sys.argv[1]


def rotate(n, c):
    try:
        i = CHARS.index(c)
        return CHARS[(i - n) % len(CHARS)]
    except ValueError:
        return c


def index(i, key):
    try:
        return CHARS.index(key[i % len(key)])
    except ValueError:
        return 0


def transform(key, msg):
    return [rotate(index(i, key), c) for i, c in enumerate(msg)]


def main():
    msg = sys.stdin.readlines()

    with open(FILENAME) as file:
        data = file.read().split()
    file.close()


    print('############################################################')
    for key in data:
        print("key: " + key)
        print()
        for line in msg:
            print(''.join(transform(key, line)))
        print()
        print('############################################################')


if __name__ == '__main__':
    main()
