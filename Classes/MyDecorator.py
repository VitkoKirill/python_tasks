# Создайте декоратор execution_time, который измеряет время выполнения функции и выводит его в консоль.
# Примените этот декоратор к функции, которая:
# Генерирует список из миллиона случайных чисел.
# Сортирует его.
# Проверьте, сколько времени занимает выполнение этой функции.
import time
from random import randint
from functools import wraps


def execution_time(func):
    @wraps(func)
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
    """
    Sorts random million numbers.
    :return:
    """
    million_list = [randint(1, 100) for _ in range(1000000)]
    million_list.sort()

print(sort_million.__doc__)
sort_million()
