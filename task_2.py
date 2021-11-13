def information_person(name,surname, age, city, email, phone):
    """
    Функция принимает данные о пользователе и выводит их одной строкой
    :param name: str
    :param surname: str
    :param age: int
    :param city: str
    :param email: str
    :param phone: int
    :return: tuple
    """
    result = name, surname, age, city, email, phone
    return result

name = input('Write your name: ')
surname = input('Write your surname: ')
age = int(input('Write your age: '))
city = input('Write your city: ')
email = input('Write your email: ')
phone = int(input('Write your phone: '))


print(information_person(name= name, surname= surname, age= age, city= city, email=email, phone= phone))
