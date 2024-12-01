# 1) Параллельное возведение в квадрат: программа, которая берет список чисел
#  и возводит их в квадрат параллельно, используя три процесса.

import multiprocessing
import time


def square_list(my_list: list, process_name: str):
    new_list = []
    for i in my_list:
        new_list.append(i * i)
        print(f'{process_name}: {i}')
        time.sleep(2)
    print(f'Result in {process_name}: {new_list}')


if __name__ == '__main__':

    processes = []
    test_list = [1, 2, 3, 4, 5]

    for p in range(3):
        p = multiprocessing.Process(target=square_list, args=(test_list, f'Process - {p + 1}'))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()