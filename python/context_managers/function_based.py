import time
import contextlib


@contextlib.contextmanager
def timer():
    start = time.time()
    yield start
    print(f"Took {(time.time() - start):.2f} seconds")


with timer() as start_time:
    data = list(range(100_000_000))
    print(start_time)
