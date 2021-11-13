def my_func(x, y):
    """
    Функция возводит x в степень y при помощи **
    :param x: int
    :param y: int
    :return: int
    """
    result = x ** y
    return result
number_1 = int(input('write a number: '))
number_2 = int(input('write a number: '))

print(my_func(number_1, number_2))

def my_func2(x, y):
    """
    Функия возводит x в степень y при помощи цикла while
    :param x: int
    :param y: int
    :return: int
    """
    number = 1
    result = 1 / x
    while number != abs(y):
        result = result / x
        number += 1
        return result

number_3 = int(input('write a number: '))
number_4 = int(input('write a number: '))
print(my_func2(number_3, number_4))