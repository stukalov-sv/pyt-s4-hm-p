# Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности

import random

def random_int_fill_list(size: int) -> list:
    result_list = []
    for i in range(size):
        result_list.append(random.randrange(-10, 11))
    return result_list

def get_unique_number_list(int_list: list) -> list:
    result_list = []

    for item in int_list:
        if item not in result_list:
            result_list.append(item)

    return result_list

random_list = random_int_fill_list(int(input('Enter list length: ')))
print(f'Random list:\n{random_list}')

print(f'Result unique list numbers:\n{get_unique_number_list(random_list)}')
