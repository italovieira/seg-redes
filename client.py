#!/usr/bin/env python3

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

from ciphers.sdes import Sdes
from ciphers.rc4 import Rc4
from ciphers.nocrypt import Nocrypt


#CRYPT = Sdes(0b1100011110)
CRYPT = Rc4(bytes('segredo', 'utf8'))


def set_crypt(crypt_str, key):
    global CRYPT

    if crypt_str.lower() == 'sdes':
        CRYPT = Sdes(int(key, 2))
        print('# Now using SDES #')

    elif crypt_str.lower() == 'rc4':
        CRYPT = Rc4(bytes(key, 'utf8'))
        print('###test: key:', key, 'bytes', bytes(key, 'utf8'))
        print('# Now using RC4 #')

    elif crypt_str.lower() == 'none':
        CRYPT = Nocrypt()

    else:
        print("Invalid command. Nothing done.")


def receive():
    global CRYPT

    '''Handles receiving of messages.'''
    while True:
        try:
            # Receiving messages
            recv_msg = CRYPT.decrypt(client_socket.recv(BUFSIZ)).decode('utf8')
            print(recv_msg)

        except UnicodeDecodeError:  # Possibly client has left the chat.
            print('# Warning: Could not understand message. Is the chosen cipher correct? #')
        except OSError:  # Possibly client has left the chat.
            break


def send():
    global CRYPT

    while True:
        try:
            # Sending messages
            print()
            msg = input('Me > ')

            '''Handles sending of messages.'''
            if not msg.startswith('/'):
                client_socket.send(CRYPT.encrypt(bytes(msg, 'utf8')))

            if msg.startswith('/crypt '):
                try:
                    [cipher, key] = msg.split()[1:]
                    set_crypt(cipher, key)
                except:
                    print("Invalid command. Nothing done.")

            elif msg == '/quit':
                print('bye!')
                client_socket.close()
                break

        except OSError:
            break


# ----Now comes the sockets part----
HOST = input('Enter host: ')
PORT = 5354


BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

print('Connected to ... chat...\n')

# Enter name
#recv_msg = client_socket.recv(BUFSIZ).decode('utf8')
#print(recv_msg)

name = input('Enter your name: ')
print('Enter /quit to exit.')

Thread(target=send).start()
Thread(target=receive).start()

