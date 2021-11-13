def sum_max_numbers(numb_1, numb_2, numb_3):
    """
    Функция принимает три числа и суммирует два наибольших из них
    :param numb_1: int
    :param numb_2: int
    :param numb_3: int
    :return: int
    """
    counter = [numb_1, numb_2, numb_3]
    result = []
    counter_1 = max(counter)
    result.append(counter_1)
    counter.remove(counter_1)
    counter_2 = max(counter)
    result.append(counter_2)
    sum_up = sum(result)
    return sum_up

numb_1 = int(input('write a number: '))
numb_2 = int(input('write another number: '))
numb_3 = int(input('write another number: '))

print(sum_max_numbers(numb_1, numb_2, numb_3))
