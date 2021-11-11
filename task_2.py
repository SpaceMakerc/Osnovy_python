user_number = list(input('write a number: '))
a = user_number
i = 0
number = len(a)

if number % 2 != 0:
    while a[i] != a[-1]:
        if a[i] != a[i+1]:
            a[i], a[i + 1] = a[i + 1], a[i]
        i += 2
else:
    while i < len(a):
        if a[i] != a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
        i += 2
print(a)
