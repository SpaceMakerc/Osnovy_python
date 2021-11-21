with open('text_6.txt', 'r', encoding='utf-8') as obj:
    dict_1 = {}
    result = []
    key_for_dict_1 = []
    key_for_dict_2 = []
    checker = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    quantity = str()
    helper = []
    sum_1 = 0
    a = 0
    for i in obj:
        result.append(i.split())
    for lists in result:
        for elem in lists:
            if lists[0] in key_for_dict_1:
                continue
            key_for_dict_1.append(lists[0])
    for key in key_for_dict_1:
        key = key[: -1]
        key_for_dict_2.append(key)
    for lists in result:
        helper.append(' '.join(lists))
    for strs in helper:
        for elem in strs:
            if elem in checker:
                quantity += elem
            elif elem == '(':
                quantity += ' '
        if strs[-1] == ')' or strs[-1] == '-':
            quantity += '/ '
    helper_2 = quantity.split()
    for i in helper_2:
        if i != '/':
            i = int(i)
            sum_1 += i
        if i == '/':
            dict_1[key_for_dict_2[a]] = sum_1
            a += 1
            sum_1 = 0
print(dict_1)
