# 1) Параллельное возведение в квадрат: программа, которая берет список чисел
#  и возводит их в квадрат параллельно, используя три процесса.

import multiprocessing
import time


def square_list(my_list: list):
    new_list = []
    process_name = multiprocessing.current_process().name
    for i in my_list:
        new_list.append(i * i)
        time.sleep(1)
    print(f'Result in {process_name}: {new_list}')


if __name__ == '__main__':
    test_list = [1, 2, 3, 4, 5, 6]

    with multiprocessing.Pool(processes=3) as p:
        p.map_async(square_list, [[x] for x in test_list])
        p.close()
        p.join()
