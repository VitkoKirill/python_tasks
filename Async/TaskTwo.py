# Асинхронный счетчик: асинхронный счетчик, который выводит числа от 1 до 10,
#  делая паузу в 0.5 секунды между выводами


import asyncio


async def counter():
    for i in range(1, 11):
        print(i)
        await asyncio.sleep(0.5)


async def main():
    await counter()


asyncio.run(main())
