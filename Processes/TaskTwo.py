# 2) Суммирование частей списка: разделить длинный список чисел на три части и
# посчитать сумму каждой части в отдельных процессах.


import multiprocessing


def sum_list(my_list: list, process_name: str, result_queue: multiprocessing.Queue):
    sum = 0
    for i in my_list:
        sum += i
    print(f'Result: {process_name}: {sum}')
    result_queue.put(sum)


if __name__ == '__main__':
    test_list = [5, 16, -7, 9, 17, 3, 8]

    num_processes = 3
    part_size = len(test_list) // num_processes
    part_list = [test_list[i * part_size:(i + 1) * part_size] for i in range(num_processes)]

    if len(test_list) % num_processes != 0:
        part_list[-1].extend(test_list[(num_processes - 1) * part_size:])

    processes = []
    queue = multiprocessing.Queue()

    for i, part in enumerate(part_list):
        p = multiprocessing.Process(target=sum_list, args=(part, f'Process - {i + 1}', queue))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    total_sum = 0
    while not queue.empty():
        total_sum += queue.get()

    print(f'Total sum: {total_sum}')