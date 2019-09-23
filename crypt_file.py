#!/usr/bin/python

import sys, getopt

def help():
    print('python3 crypt_file.py -c sdes -k <key> -e -i <inputfile> -o <outputfile>')
    print('python3 crypt_file.py -c sdes -k <key> -d -i <inputfile> -o <outputfile>')
    print('python3 crypt_file.py -c rc4  -k <key> -e -i <inputfile> -o <outputfile>')
    print('python3 crypt_file.py -c rc4  -k <key> -d -i <inputfile> -o <outputfile>')


def crypt_action(crypt_str, mode, key):
    if crypt_str.lower() == 'sdes':
        from ciphers.sdes import Sdes
        crypt = Sdes(int(key, 2))

    elif crypt_str.lower() == 'rc4':
        from ciphers.rc4 import Rc4
        crypt = Rc4(bytes(key, 'utf8'))

    if mode == '-e':
        return crypt.encrypt
    else:
        return crypt.decrypt


def write_data(inputfile, outputfile, crypt_action):
    print('Starting reading data from', inputfile, '...')
    with open(inputfile, 'rb') as in_file, open(outputfile, 'wb') as out_file:
        data = in_file.read()
        out_file.write(crypt_action(data))

    print('File', outputfile, 'writed!')


def main(argv):
    mode = ''
    crypt_str = ''
    key = ''
    inputfile = ''
    outputfile = ''

    try:
        opts, args = getopt.getopt(argv,'hc:k:edi:o:', ['cypher=', 'key=', 'ifile=', 'ofile='])
    except getopt.GetoptError:
        help()
        sys.exit()

    for opt, arg in opts:

        if opt == '-h':
            help()
            sys.exit()

        elif opt in ('-c', '--cypher'):
            crypt_str = arg

        elif opt in ('-e', '-d'):
            mode = opt

        elif opt in ('-k', '--key'):
            key = arg

        elif opt in ('-i', '--ifile'):
            inputfile = arg

        elif opt in ('-o', '--ofile'):
            outputfile = arg


    action = crypt_action(crypt_str, mode, key)
    write_data(inputfile, outputfile, action)


if __name__ == '__main__':
    main(sys.argv[1:])
