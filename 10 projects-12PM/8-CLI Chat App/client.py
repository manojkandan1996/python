import socket
import threading

def handle_client(conn, addr):
    print(f"✅ New connection from {addr}")
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            msg = data.decode()
            print(f"<{addr}> {msg}")
            conn.send(f"Server echo: {msg}".encode())
        except ConnectionResetError:
            break
    conn.close()
    print(f"❌ Connection closed for {addr}")

def main():
    HOST = ''       # Listen on all interfaces
    PORT = 5000
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"🌐 Server listening on port {PORT}")

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    main()
