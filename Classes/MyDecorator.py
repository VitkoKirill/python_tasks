# Создайте декоратор execution_time, который измеряет время выполнения функции и выводит его в консоль.
# Примените этот декоратор к функции, которая:
# Генерирует список из миллиона случайных чисел.
# Сортирует его.
# Проверьте, сколько времени занимает выполнение этой функции.
import time
from random import randint


def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        exec_time = end - start
        print(f'Execution time {exec_time}')
        return result

    return wrapper


@execution_time
def sort_million():
    million_list = [randint(1, 100) for _ in range(1000000)]
    million_list.sort()


sort_million()
