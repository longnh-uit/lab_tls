import socket
import ssl
import os
import sys

PATH = os.path.dirname(__file__)
HEADER = 64
PORT = 3000
SERVER = sys.argv[1] # get server address from argument
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(PATH + "./certs/certificate.crt", PATH + "./certs/privateKey.key")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")


    msg_length = conn.recv(HEADER).decode(FORMAT)
    if msg_length:
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)

        print(f"[{addr}] {msg}")
        conn.send(f"Hello {msg}".encode(FORMAT))


def start():
    server.listen()
    ssock = context.wrap_socket(server, True)
    print(f"[LISTENING] Server is listening on {SERVER}")
    conn, addr = ssock.accept()
    handle_client(conn, addr)
    print(f"[TLS] TLS version: {ssock.version()}")
    conn.close()
    print("[CLOSING] Server is closing...")

print("[STARTING] Server is starting... ")
start()