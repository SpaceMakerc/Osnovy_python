user_month_1 = int(input('Write a month: '))

months_1 = ['такого месяца нет', 'зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
result = months_1[user_month_1]

print(f'Время года - {result}')

user_month_2 = int(input('Write a month: '))

months_2 = {1 : 'зима', 2 : 'зима', 3 : 'весна', 4 : 'весна', 5 : 'весна', 6 : 'лето', 7 : 'лето', 8 : 'лето', 9 : 'осень', 10 : 'осень', 11 : 'осень', 12 : 'зима'}
result_1 = months_2[user_month_2]

print(f'Время года - {result_1}')
