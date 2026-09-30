import time
import asyncio
import itertools


# In CPython, time.sleep() is explicitly implemented to release the GIL
# If no sleep exists CPython periodically gives another waiting thread a chance to acquire the GIL every ~ 5ms


async def _thinking(stop_event):
    for char in itertools.cycle([".", "..", "...", "....", "....."]):
        status = f'\r\033[2KThinking{char}'
        await asyncio.sleep(0.2)
        print(status, end='', flush=True)
        if stop_event.is_set():
            print("\r\033[2K", end='', flush=True)
            break


# A coroutine is a function whose execution can pause and resume, allowing other work to run while it waits.
# Calling _slow() creates a coroutine object
async def _slow():
    await asyncio.sleep(3.0)


async def program():
    stop_event = asyncio.Event()

    thinking_task = asyncio.create_task(_thinking(stop_event))
    slow_task = asyncio.create_task(_slow())

    await slow_task
    stop_event.set()
    await thinking_task

    print("t2 is done")


if __name__ == "__main__":
    asyncio.run(program())
