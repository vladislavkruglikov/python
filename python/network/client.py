import socket
import argparse
from recieve import _recieve


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--digit", required=True, type=int)
    args = parser.parse_args()

    s = socket.socket()
    s.connect(("localhost", 8082))
    s.sendall((str(args.digit) + "\n").encode("utf-8"))

    number = _recieve(s)
    print("Server returned", number)
    s.close()
