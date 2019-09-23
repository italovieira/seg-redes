#!/usr/bin/env python3

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

from sdes import Sdes
from rc4 import Rc4


crypt = Sdes(0b1100011110)

def receive():
    '''Handles receiving of messages.'''
    while True:
        try:
            # Receiving messages
            recv_msg = crypt.decrypt(client_socket.recv(BUFSIZ)).decode('utf8')
            print(recv_msg)

        except OSError:  # Possibly client has left the chat.
            break


def send():  # event is passed by binders.
    while True:
        try:
            # Sending messages
            msg = input('Me > ')

            '''Handles sending of messages.'''
            client_socket.send(crypt.encrypt(bytes(msg, 'utf8')))
            if msg == '/quit':
                client_socket.close()

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
print('Enter /quit to exit.')

# Enter name
#recv_msg = client_socket.recv(BUFSIZ).decode('utf8')
#print(recv_msg)
name = input('Enter your name: ')

Thread(target=send).start()
Thread(target=receive).start()
