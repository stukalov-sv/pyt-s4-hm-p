# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import random
import os

def random_int_fill_list(size: int) -> list:
    result_list = []
    for i in range(size):
        result_list.append(random.randrange(1, 101))
    return result_list

polynom_degree1 = int(input('Enter polynoms degree: '))
polynom_degree1 += 1
random_rates1 = random_int_fill_list(polynom_degree1)

polynom_degree2 = polynom_degree1
random_rates2 = random_int_fill_list(polynom_degree2)

path1 = os.path.join('folder', 'file5hm_1.txt')
path2 = os.path.join('folder', 'file5hm_2.txt')

with open(path1, 'w') as writer1:
    for i in range(polynom_degree1):
        if i < polynom_degree1 - 2:
            if random_rates1[i] > 1:
                writer1.write(f'{random_rates1[i]}*x^{polynom_degree1 - 1 - i} + ')
            elif random_rates1[i] == 1:
                writer1.write(f'x^{polynom_degree1 - 1 - i} + ')
        elif i == polynom_degree1 - 2:
            if random_rates1[i] > 1:
                writer1.write(f'{random_rates1[i]}*x')
            elif random_rates1[i] == 1:
                writer1.write(f'x')
        else:
            if random_rates1[i] > 0:
                writer1.write(f' + {random_rates1[i]}')

    writer1.write(' = 0')

with open(path2, 'w') as writer2:
    for i in range(polynom_degree2):
        if i < polynom_degree2 - 2:
            if random_rates2[i] > 1:
                writer2.write(f'{random_rates2[i]}*x^{polynom_degree2 - 1 - i} + ')
            elif random_rates2[i] == 1:
                writer2.write(f'x^{polynom_degree2 - 1 - i} + ')
        elif i == polynom_degree2 - 2:
            if random_rates2[i] > 1:
                writer2.write(f'{random_rates2[i]}*x')
            elif random_rates2[i] == 1:
                writer2.write(f'x')
        else:
            if random_rates2[i] > 0:
                writer2.write(f' + {random_rates2[i]}')

    writer2.write(' = 0')

rates1 = []
rates2 = []
degrees1 = []
degrees2 = []

with open(path1, 'r') as writer3:
    text1 = writer3.readline()
    print(f'First polynom: {text1}')
    str_list = [str(x) for x in text1.split(' ')]
    for i in range(len(str_list)):
        if (str_list[i].startswith('+') or str_list[i].startswith('0') or str_list[i].startswith('=')):
            i += 1
        elif str_list[i].startswith('x'):
            rates1.append(int(0))
            temp_list = [str(x) for x in str_list[i].split('^')]
            if len(temp_list) < 2:
                temp_list.append(1)
            for j in range(len(temp_list)):
                if j == 1:
                    degrees1.append(int(temp_list[j]))
        elif str_list[i].isdigit():
            rates1.append(int(str_list[i]))
            degrees1.append(int(0))
        else:
            temp_list = [str(x) for x in str_list[i].split('^')]
            if len(temp_list) < 2:
                temp_list.append(0)
            for j in range(len(temp_list)):
                if j == 1:
                    if str(temp_list[j]) != '0':
                        degrees1.append(int(temp_list[j]))
                    elif str(temp_list[j]) == '0':
                        degrees1.append(int(1))
                else:
                    num1 = ''
                    for char in temp_list[j]:
                        if char.isdigit():
                            num1 = num1 + char
                        else:
                            if num1 != '':
                                rates1.append(int(num1))
                                num1 = ''

with open(path2, 'r') as writer4:
    text2 = writer4.readline()
    print(f'Second polynom: {text2}')
    str_list = [str(x) for x in text2.split(' ')]
    for i in range(len(str_list)):
        if (str_list[i].startswith('+') or str_list[i].startswith('0') or str_list[i].startswith('=')):
            i += 1
        elif str_list[i].startswith('x'):
            rates2.append(int(0))
            temp_list = [str(x) for x in str_list[i].split('^')]
            if len(temp_list) < 2:
                temp_list.append(1)
            for j in range(len(temp_list)):
                if j == 1:
                    degrees2.append(int(temp_list[j]))
        elif str_list[i].isdigit():
            rates2.append(int(str_list[i]))
            degrees2.append(int(0))
        else:
            temp_list = [str(x) for x in str_list[i].split('^')]
            if len(temp_list) < 2:
                temp_list.append(0)
            for j in range(len(temp_list)):
                if j == 1:
                    if str(temp_list[j]) != '0':
                        degrees2.append(int(temp_list[j]))
                    elif str(temp_list[j]) == '0':
                        degrees2.append(int(1))
                else:
                    num1 = ''
                    for char in temp_list[j]:
                        if char.isdigit():
                            num1 = num1 + char
                        else:
                            if num1 != '':
                                rates2.append(int(num1))
                                num1 = ''

sum_rates = []

for i in range(len(rates1)):
    sum_rates.append(rates1[i] + rates2[i])

path3 = os.path.join('folder', 'file5hm_3.txt')

with open(path3, 'w') as writer5:
    size = len(sum_rates)
    for i in range(size):
        if i < size - 2:
            if sum_rates[i] > 1:
                writer5.write(f'{sum_rates[i]}*x^{size - 1 - i} + ')
            elif sum_rates[i] == 1:
                writer5.write(f'x^{size - 1 - i} + ')
        elif i == size - 2:
            if sum_rates[i] > 1:
                writer5.write(f'{sum_rates[i]}*x')
            elif sum_rates[i] == 1:
                writer5.write(f'x')
        else:
            if sum_rates[i] > 0:
                writer5.write(f' + {sum_rates[i]}')

    writer5.write(' = 0')

with open(path3, 'r') as reader:
    text3 = reader.readline()
    print(f'Result polynom: {text3}')
