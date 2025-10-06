# Asynchronous code:

import asyncio

async def count():
    print("one")
    await asyncio.sleep(1)
    print("Two")
    await asyncio.sleep(1)

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    start =  time.perf_counter()
    asyncio.run(main()) # Noticed this works here..... and not in the jupyter notebook.
    elapsed = time.perf_counter() - start
    print(f"executed in {elapsed:0.2f} seconds")