import time
import itertools
import multiprocessing


# In CPython, time.sleep() is explicitly implemented to release the GIL
# If no sleep exists CPython periodically gives another waiting thread a chance to acquire the GIL every ~ 5ms


def _thinking(stop_event) -> None:
    for char in itertools.cycle([".", "..", "...", "....", "....."]):
        status = f'\r\033[2KThinking{char}'
        time.sleep(0.2)
        print(status, end='', flush=True)
        if stop_event.is_set():
            print("\r\033[2K", end='', flush=True)
            break


def _slow() -> None:
    time.sleep(3.0)


if __name__ == "__main__":
    stop_event = multiprocessing.Event()

    t1 = multiprocessing.Process(target=_thinking, args=(stop_event,))
    t2 = multiprocessing.Process(target=_slow)

    # Start spinner
    t1.start()
    # Start slow function
    t2.start()

    # Wait for slow function
    t2.join()
    # Schedule spinner to stop spinning
    stop_event.set()
    # Wait spinner to stop spinning and clear stdout
    t1.join()

    # Print to stdout
    print("t2 is done")
