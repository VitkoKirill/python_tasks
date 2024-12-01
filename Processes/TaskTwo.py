# 2) Суммирование частей списка: разделить длинный список чисел на три части и
# посчитать сумму каждой части в отдельных процессах.


import multiprocessing
import time


def sum_list(my_list: list):
    time.sleep(1)
    process_name = multiprocessing.current_process().name
    sum = 0
    for i in my_list:
        sum += i
    print(f'Result: {process_name}: {sum}')
    return sum

def end_func(response):
    total_sum = sum(response)
    print(f'Total sum: {total_sum}')


if __name__ == '__main__':
    test_list = [5, 16, -7, 9, 17, 3, 8]
    num_processes = 3
    part_size = len(test_list) // num_processes
    part_list = [test_list[i * part_size:(i + 1) * part_size] for i in range(num_processes)]

    remainder = test_list[num_processes * part_size:]
    if remainder:
        part_list[-1].extend(remainder)

    with multiprocessing.Pool(num_processes) as p:
        p.map_async(sum_list, [part for part in part_list], callback=end_func)
        p.close()
        p.join()

    print('Process Done!')
    # num_processes = 3
    # part_size = len(test_list) // num_processes
    # part_list = [test_list[i * part_size:(i + 1) * part_size] for i in range(num_processes)]
    #
    # if len(test_list) % num_processes != 0:
    #     part_list[-1].extend(test_list[(num_processes - 1) * part_size:])
    #
    # processes = []
    # queue = multiprocessing.Queue()
    #
    # for i, part in enumerate(part_list):
    #     p = multiprocessing.Process(target=sum_list, args=(part, f'Process - {i + 1}', queue))
    #     processes.append(p)
    #     p.start()
    #
    # for p in processes:
    #     p.join()
    #
    # total_sum = 0
    # while not queue.empty():
    #     total_sum += queue.get()
    #
    # print(f'Total sum: {total_sum}')