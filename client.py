import socket
import threading

server_addr = socket.gethostbyname(socket.gethostname())
port = 5050
encoding_format = 'UTF-8'


def send_msg(conn, message):
    message = message.encode(encoding_format)
    conn.send(message)
    # response_msg = conn.recv(1024).decode(encoding_format)
    # print(f"[INFO] Response from server : {response_msg}")


def recv_msg(conn):
    pass


def start():
    connected = True
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((server_addr, port))

    while connected:
        message = input("Enter your message...:")
        if message != "exit":
            send_msg(conn, message)
            # recv_msg(conn)
        else:
            connected = False
            send_msg(conn, message)
            conn.close()
            print(f"[CLIENT] exit...")


start()



