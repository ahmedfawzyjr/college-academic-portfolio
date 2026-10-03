# 01_tcp_echo_server.py

import socket

def run_echo_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8888))
    server.listen(1)
    print("Echo Server running on 127.0.0.1:8888...")
    server.close()

if __name__ == "__main__":
    run_echo_server()
