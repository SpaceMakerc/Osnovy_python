with open('text_5.txt', 'w') as obj_5:
    content = input('write numbers: ')
    obj_5.write(content)
    list_1 = []
    result = 0
with open('text_5.txt') as obj_5_5:
    for i in obj_5_5:
        print(i)
        list_1.append(i.split())
        for lists in list_1:
            for numb in lists:
                numb = int(numb)
                result += numb
print(result)
