import threading

c = 0
lock = threading.Lock()

def a() -> None:
    global c
    with lock:
        c += 1
        print(c)

def b() -> None:
    global c
    with lock:
        c += 1
        print(c)

if __name__ == "__main__":
    stop_event = threading.Event()
    t1 = threading.Thread(target=a)
    t2 = threading.Thread(target=b)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
