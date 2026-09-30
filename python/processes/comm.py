import multiprocessing as mp

def sender(conn):
    conn.send_bytes(b"hello")
    conn.close()

def receiver(conn):
    data = conn.recv_bytes()
    print(data)
    conn.close()

if __name__ == "__main__":
    recv_conn, send_conn = mp.Pipe(duplex=False)
    p1 = mp.Process(target=sender, args=(send_conn,))
    p2 = mp.Process(target=receiver, args=(recv_conn,))
    p1.start()
    p2.start()
    recv_conn.close()
    send_conn.close()
    p1.join()
    p2.join()
