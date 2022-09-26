import socket

HOST = "127.0.0.1"
PORT = 1

RECEIVER_TYPE = socket.AF_INET

server_socket = socket.socket(RECEIVER_TYPE, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

server_socket.listen()


def receive_data():
    while True:
        data, adr = server_socket.recv(12)
        print(data, adr)

