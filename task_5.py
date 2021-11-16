from functools import reduce

user_list = [i for i in range(100, 1001) if i % 2 == 0]
print(user_list)

def mul_numbers(numb_1, numb_2):
    return numb_1 * numb_2

result = reduce(mul_numbers, user_list)

print(result)

# or
user_list_2 = [i for i in range(100, 1001) if i % 2 == 0]

result_2 = reduce(lambda num_1, num_2 : num_1 * num_2, user_list_2)
print(result_2)
