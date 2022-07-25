# Вычислить число Пи с заданной точностью d

import math

def get_pi_chudnovsky(iterations = 10) -> float:
    number_pi = 3
    i = 1
    sign = -1
    sum = 13591409 / (640320 ** (3 / 2))
    while i < iterations:
        temp = (sign * math.factorial(6 * i) * (13591409 + 545140134 * i)) / \
               (math.factorial(3 * i) * (math.factorial(i) ** 3) * (640320 ** 3/2) * (640320 ** (3 * i)))
        sum += temp
        sign *= -1
        i += 1
        number_pi = 1 / (12 * sum)
    return number_pi

user_accuracy = int(input('Enter accuracy as number of signs before comma (1 to 10): '))
user_pi = get_pi_chudnovsky()
user_pi = int(user_pi * 10 ** user_accuracy) / 10 ** user_accuracy
print(f'Result pi: {user_pi}')

