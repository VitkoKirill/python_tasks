# 3) Чтение файлов асинхронно: функция, которая читает содержимое трех текстовых файлов
# с помощью asyncio. Нужна задержка чтения файла с использованием await asyncio.sleep


import asyncio


async def read_file(filename: str):
    with open(filename, 'r') as f:
        for line in f:
            print(line)
            await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(read_file('FirstTxt'))
    task2 = asyncio.create_task(read_file('SecondTxt'))
    task3 = asyncio.create_task(read_file('ThirdTxt'))

    await asyncio.gather(task1, task2, task3)

asyncio.run(main())