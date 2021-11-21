import json
with open('text_7.txt', 'r', encoding='utf-8') as obj_7:
    counter = []
    names = []
    profits = []
    a = 0
    b = 0
    dict_1 = {}
    dict_2 = {}
    result = []
    average_profit = 0
    for i in obj_7:  # Numbers were shown line by line
        print(i)
        counter.append(i.split())
    for lists in counter:
        for elem in lists:  # List was splitted on numbers and names
            names.append(lists[0])
            lists.remove(lists[0])
        for elem in lists:  # Now all numbers are int
            elem = int(elem)
            a += elem
        profits.append(a - elem * 2)  # Profit of all numbers
        a = 0
    for i in profits:  # Average profit
        if i > 0:
            b += 1
            a += i
        average_profit = a / b
        dict_2['average_profit'] = average_profit
    a = 0
    for name in names:  # Extra numbers with profit were written in first dict
        if len(name) > 3:
            dict_1[name] = profits[a]
            a += 1
    result.append(dict_1)  # Add all dicts in result
    result.append(dict_2)
    print(result)

with open('test.json', 'w') as obj_8:
    content = json.dumps(result)
    obj_8.write(content)

with open ('test.json', 'r') as obj_8:
    content_2 = obj_8.read()
    reader = json.loads(content_2)
    print(type(reader))
    print(reader)
