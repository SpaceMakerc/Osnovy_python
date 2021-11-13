def division_number(numb_1, numb_2):
    """
    Деление двух чисел друг на друга
    :param numb_1: int
    :param numb_2: int
    :return: int
    """
    result = numb_1 / numb_2
    if result == 0:
        print('Делить на ноль нельзя:)')
    return result

numb_1 = int(input('Write a number: '))
numb_2 = int(input('Write another number: '))

print(division_number(numb_1, numb_2))
