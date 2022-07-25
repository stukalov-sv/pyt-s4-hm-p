# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
import os

def random_int_fill_list(size: int) -> list:
    result_list = []
    for i in range(size):
        result_list.append(random.randrange(0, 101))
    return result_list

polynom_degree = int(input('Enter polynom degree: '))
polynom_degree += 1
random_rates = random_int_fill_list(polynom_degree)

path = os.path.join('folder', 'file4hm.txt')

with open(path, 'w') as writer:
    for i in range(polynom_degree):
        if i < polynom_degree - 2:
            if random_rates[i] > 1:
                writer.write(f'{random_rates[i]}*x^{polynom_degree - 1 - i} + ')
            elif random_rates[i] == 1:
                writer.write(f'x^{polynom_degree - 1 - i} + ')
        elif i == polynom_degree - 2:
            if random_rates[i] > 1:
                writer.write(f'{random_rates[i]}*x')
            elif random_rates[i] == 1:
                writer.write(f'x')
        else:
            if random_rates[i] > 0:
                writer.write(f' + {random_rates[i]}')

    writer.write(' = 0')

with open(path, 'r') as reader:
    print(reader.readline())



