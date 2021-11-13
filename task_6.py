def int_func(word):
    """
    Функция принимает строку слов, каждую первую букву слова переводит в верхний регистр
    :param word: str
    :return: str
    """
    counter = str(word)
    result = counter[0].upper()
    for index, elem in enumerate(counter):
        if counter[index-1] == ' ':
            continue
        if elem != counter[0]:
            result += elem
        if elem == ' ':
            helper = counter[index+1].upper()
            result += helper
    return result

user_word = input('Write a number: ')
print(int_func(user_word))
