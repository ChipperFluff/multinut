import socket

class Clamamus:
    pass

def client():
    HOST = 'localhost'
    PORT = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"Hello, server! This is client speaking.")
