basic_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = [i for i in basic_list if basic_list.count(i) == 1]
print(result)
