import asyncio
import time


async def async_square_with_io_sleep(val: int) -> int:
    print(f'start: {val}')
    await asyncio.sleep(5 / (val + 1))
    print(f'end: {val}')
    return val ** 2


async def async_sleep(sec: float):
    time.sleep(sec)


async def async_square_with_sleep(val: int) -> int:
    print(f'start: {val}')
    await async_sleep(5 / (val + 1))
    print(f'end: {val}')
    return val ** 2


async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i in range(10):
            # couldn't create my async procedure
            # val = tg.create_task(async_square_with_sleep(i))
            task = tg.create_task(async_square_with_io_sleep(i))
            tasks.append(task)
    results = [task.result() for task in tasks]
    print(results)


if __name__ == '__main__':
    asyncio.run(main())
