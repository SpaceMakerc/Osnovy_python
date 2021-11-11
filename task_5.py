a = [8, 7, 5, 2, 1, 0]
i = 0
user_number = int(input('write a number: '))

while a[i] != a[-1]:
    if user_number == a[i]:
        a.insert(i, user_number)
        break
    if user_number > a[0]:
        a.insert(0, user_number)
        break
    if user_number != a[i] and user_number < a[i]:
        i += 1
        if user_number > a[i] or user_number == a[i]:
            a.insert(i, user_number)
            break
print(a)
