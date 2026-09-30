import time


class Timer:
    def __enter__(self):
        self._start = time.time()
        return self._start

    def __exit__(self, exc_type, exc, tb):
        print(f"Took {(time.time() - self._start):.2f} seconds")


with Timer() as start_time:
    data = list(range(100_000_000))
    print(start_time)
