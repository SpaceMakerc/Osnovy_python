def counter(str=()):
    """
    Функция принимает строку чисел, разделяет строку по элементам, каждый элемент переводит из типа строка в тип число и суммирует числа.
    Всё это в цикле.
    :param str: str
    :return: int
    """
    numbers = []
    numb = str
    count = numb.split()
    for i in count:
        i = int(i)
        numbers.append(i)
    result = sum(numbers)
    return result


strok = input('write a numbers: ')
dictory = []

while strok != '%':
    strok.split()
    if strok[-1] != '%':
            counter(strok)
            dictory.append(counter(strok))
            itog = sum(dictory)
            print(itog)
            strok = input('write a numbers: ')
    elif strok == '%':
        break
    else:
        for index, elem in enumerate(strok):
            if elem == '%':
                strok = strok[0:index]
                counter(strok)
                dictory.append(counter(strok))
                itog = sum(dictory)
                print(itog)
        break
