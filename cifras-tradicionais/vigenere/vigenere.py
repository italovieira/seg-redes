import sys

CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ?,'

# data: possible keys
FILENAME = sys.argv[1]


def rotate(n, c):
    try:
        i = CHARS.index(c)
        return CHARS[(i + n) % len(CHARS)]
    except ValueError:
        return c


def transform(key, msg):
    return [rotate(CHARS.index(key[i % len(key)]), c) for i, c in enumerate(msg)]


def main():
    msg = sys.stdin.readlines()

    with open(FILENAME) as file:
        data = file.read().split()
    file.close()


    print(msg)
    print('############################################################')
    print(''.join(transform('abab', msg)))
   # for key in data:
   #     print("key: " + key)
   #     print()
   #     print(''.join(transform(key, msg)))
   #     print()
   #     print('############################################################')


if __name__ == '__main__':
    main()
