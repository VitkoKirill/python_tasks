# Асинхронность
# 1) Таймеры с задержкой:  программа, которая создает три асинхронные задачи.
# Каждая задача должна выводить сообщение через разное время (например, 1, 2 и 3 секунды)

import asyncio


async def message_task(seconds: int, message: str):
    await asyncio.sleep(seconds)
    print(message)


async def main():
    task1 = asyncio.create_task(message_task(seconds=2, message='First message'))
    task2 = asyncio.create_task(message_task(seconds=10, message='Second message'))
    task3 = asyncio.create_task(message_task(seconds=5, message='Third message'))

    await asyncio.gather(task1, task2, task3)


asyncio.run(main())
