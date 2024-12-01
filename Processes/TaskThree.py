# Проверка четности
# 3)  Создай три процесса, каждый из которых проверяет свою часть списка чисел
# на четность и выводит четные числа в консоль.

import multiprocessing


def even_numbers(my_list: list, process_name: str):
    for i in my_list:
        if i % 2 == 0:
            print(f"{process_name}: {i}")


if __name__ == '__main__':
    test_list = [8, 16, -4, 9, 14, 3]

    num_processes = 3
    part_size = len(test_list) // num_processes
    part_list = [test_list[i * part_size:(i + 1) * part_size] for i in range(num_processes)]

    if len(test_list) % num_processes != 0:
        part_list[-1].extend(test_list[(num_processes - 1) * part_size:])

    processes = []

    for i, part in enumerate(part_list):
        p = multiprocessing.Process(target=even_numbers, args=(part, f'Process: {i + 1}'))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print('Processes are completed!')