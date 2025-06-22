import socket
import threading

def handle_client(conn, addr):
    print(f"📥 Connected by {addr}")
    while True:
        try:
            msg = conn.recv(1024).decode()
            if msg:
                print(f"<{addr}> {msg}")
            else:
                break
        except:
            break
    conn.close()

host = '127.0.0.1'  # Use your LAN IP for real network
port = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

print(f"🟢 Server listening on {host}:{port}")
conn, addr = server.accept()
threading.Thread(target=handle_client, args=(conn, addr)).start()

while True:
    msg = input()
    conn.send(msg.encode())