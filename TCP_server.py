import socket  #calling socket library

HOST = "0.0.0.0" # It will allow the server to accept every connection
PORT = 5000

def start_server():

    #create a TCP socket
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #Allow quick reuse of socket even if it is in TIME WAIT state


    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


    #allocating ip and port to the socket

    server_socket.bind((HOST,PORT))

    #the server listens for the connection and creates a queue of size 1
    server_socket.listen(1)
    print(f"[INFO] Server listening on {HOST}:{PORT}")


    # 5. Accept client, creates a new socket conn and the address of the client
    conn, addr = server_socket.accept()
    print(f"[INFO] Connected by {addr}")

    total_bytes = 0

    try:
        while True:
            # 6. Receive data (stream-safe)
            data = conn.recv(1024)

            # 7. If empty bytes -> client closed connection
            if not data:
                print("[INFO] Client closed connection.")
                break

            total_bytes += len(data)
            print(f"[RECEIVED] {len(data)} bytes | Total: {total_bytes}")

    except Exception as e:
        print(f"[ERROR] {e}")

    finally:
        conn.close()
        server_socket.close()
        print("[INFO] Server closed.")


if __name__ == "__main__":
    start_server()    



