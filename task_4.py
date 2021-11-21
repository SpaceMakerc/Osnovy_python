dict_1 = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
with open('text_4.txt', 'r') as obj_3:
    result = []
    helper = []
    for i in obj_3:
        result.append(i.split())
    for dict in result:
        dict[0] = dict_1.get(dict[0])
        helper.append(' '.join(dict))
    with open('text_4_4.txt', 'w') as obj_4:
        for i in helper:
            print(i)
            obj_4.write(i)
