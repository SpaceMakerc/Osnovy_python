user_list = input('write a phrase: ')
result = user_list.split()
number = 0
for i in result:
    number += 1
    print(f'{number} - строка', i[0:10])
