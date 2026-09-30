import socket
import threading
from recieve import _recieve


def worker(connection_socket) -> None:
    number = _recieve(connection_socket)
    print(f"Recieved {number}")

    # Emulate work
    for _ in range(1_00_000_000):
        pass

    print("End work for", number)
    connection_socket.sendall((str(number * 2) + "\n").encode("utf-8"))
    connection_socket.close()

s = socket.socket()
s.bind(("localhost", 8082))
s.listen()
while True:
    conn, address = s.accept()
    print("received connection from", address)
    threading.Thread(target=worker, args=(conn,)).start()
