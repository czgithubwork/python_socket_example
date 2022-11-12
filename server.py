import socket
import threading

server_addr = socket.gethostbyname(socket.gethostname())
port = 5050
encoding_format = 'UTF-8'
disconnect = "exit"
conn_list = []

def broadcast(message):
    message = message.encode(encoding_format)
    for conn in conn_list:
        conn.send(message)
    

def handle(conn, addr):
    print(f"[SERVER] Active connections: { threading.activeCount() - 1}")

    connected = True
    while connected:
        msg = conn.recv(1024).decode(encoding_format)
        print(f"[INFO] Received msg from {addr} : {msg} ")

        if msg == disconnect:
            print(f"[SERVER] client disconnected.")
            connected = False
            break
        else:
            msg = "Hello".encode(encoding_format)
            conn.send(msg)


def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_addr, port))
    server.listen()

    while True:
        conn, addr = server.accept()
        conn_list.append(conn)
        thread = threading.Thread(target=handle, args=(conn, addr))
        thread.start()     


print(f"[SERVER] Server {server_addr} is running on port: {port}")
start()