# Проверка четности
# 3)  Создай три процесса, каждый из которых проверяет свою часть списка чисел
# на четность и выводит четные числа в консоль.

import multiprocessing
import time


def even_numbers(my_list: list):
    time.sleep(1)
    process_name = multiprocessing.current_process().name
    for i in my_list:
        if i % 2 == 0:
            print(f"{process_name}: {i}")


if __name__ == '__main__':
    test_list = [8, 16, -4, 9, 14, 3, 10]
    num_processes = 3
    part_size = len(test_list) // num_processes
    part_list = [test_list[i * part_size:(i + 1) * part_size] for i in range(num_processes)]

    remainder = test_list[num_processes * part_size:]
    if remainder:
        part_list[-1].extend(remainder)

    with multiprocessing.Pool(num_processes) as p:
        p.map_async(even_numbers, part_list)
        p.close()
        p.join()

    print('Processes are completed!')