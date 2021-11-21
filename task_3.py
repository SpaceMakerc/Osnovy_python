with open('text_3.txt') as obj_3:
    first = obj_3.readlines()
    result = []
    counter = 0
    a = 0
    for i in first:
        result.append(i.split())
    for i in result:
        i[1] = int(i[1])
        counter += i[1]
        if i[1] > 0:
            a += 1
        if i[1] > 20000:
            print(i[1])
medium_income = counter / a
print(f'Medium income - {medium_income}')
