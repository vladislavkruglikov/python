import functools
import tracemalloc


LRU_CACHE_MAX_SIZE = 4


class Worker:
    # The cache is shared across instances. Max size defaults to 128
    # so memory leak is bounded
    @functools.lru_cache(maxsize=LRU_CACHE_MAX_SIZE)
    def length(self, a):
        return len(a)


tracemalloc.start()
prev, _ = tracemalloc.get_traced_memory()


for i in range(1024):
    data = tuple(i for i in range(1024))
    Worker().length(data)

    curr, _ = tracemalloc.get_traced_memory()
    
    if i < LRU_CACHE_MAX_SIZE:
        # Untill cache is saturated memory will leak by atleast argument size
        # of 1024 integers where each integer is 4 bytes
        assert curr - prev >= 1024 * 4
        last_i_mem = curr

    if i > LRU_CACHE_MAX_SIZE:
        # Any further allocations remain bounded but volatile due to cache invalidation 
        # for example
        assert curr - last_i_mem <= 512

    prev = curr

tracemalloc.stop()
