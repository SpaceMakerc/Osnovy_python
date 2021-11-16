basic_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result_list = [elem for index, elem in enumerate(basic_list) if elem > basic_list[index-1] and elem != basic_list[0]]
print(result_list)
