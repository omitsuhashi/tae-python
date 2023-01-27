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
            # below link is reason why
            # https://qiita.com/everylittle/items/57da997d9e0507050085#:~:text=asyncio.sleep()%20%E3%82%92,%E3%81%97%E3%81%9D%E3%81%86%E3%81%AA%E4%BE%8B%E3%80%82
            # val = tg.create_task(async_square_with_sleep(i))
            task = tg.create_task(async_square_with_io_sleep(i))
            tasks.append(task)
    results = [task.result() for task in tasks]
    print(results)


if __name__ == '__main__':
    asyncio.run(main())
