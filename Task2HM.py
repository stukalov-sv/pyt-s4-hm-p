# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N

def get_integer_base_factors(number: int) -> list:
    factors_list = []
    div = 2

    while div * div <= number:
        if number % div == 0:
            factors_list.append(div)
            number //= div
        else:
            div += 1

    factors_list.append(number)
    return factors_list

user_number = int(input('Enter number: '))
base_factors = get_integer_base_factors(user_number)

print(f'Base factors of number {user_number}: {base_factors}')
