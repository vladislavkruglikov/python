import functools
import tracemalloc


LRU_CACHE_MAX_SIZE = 4


class Worker:
    def __init__(self):
        self._a_lot_of_storage = bytearray(8192)

    # The cache is shared across instances. Max size defaults to 128
    # so memory leak is bounded
    @functools.lru_cache(maxsize=LRU_CACHE_MAX_SIZE)
    def echo(self, a: int) -> int:
        return a


tracemalloc.start()
prev, _ = tracemalloc.get_traced_memory()


for i in range(16384):
    Worker().echo(1)

    curr, _ = tracemalloc.get_traced_memory()
    print(prev, curr)
    
    if i < LRU_CACHE_MAX_SIZE:
        # Untill cache is saturated memory will leak by atleast object size size of 1024 bytes
        assert curr - prev >= 8192
        last_i_mem = curr

    if i > LRU_CACHE_MAX_SIZE:
        # Any further allocations remain bounded but volatile due to cache invalidation 
        assert curr - last_i_mem <= 512

    prev = curr

tracemalloc.stop()
