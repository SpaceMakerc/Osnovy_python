user_number = int(input('Write a number: '))
first_number = 0

while user_number > 0:
    first_number = user_number % 10
    user_number = user_number // 10
    while first_number > user_number % 10:
        user_number = user_number // 10
        if user_number == 0:
            break
print('The biggest number is -', first_number)
