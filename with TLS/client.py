import socket
import ssl
import os

PATH = os.path.dirname(__file__)
HEADER = 64
PORT = 3000
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations(PATH + "/certs/certificate.crt")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(ADDR)
client = context.wrap_socket(sock, server_hostname="server.net")

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(len(message) + 6).decode(FORMAT))

send("Nguyễn Hữu Long")