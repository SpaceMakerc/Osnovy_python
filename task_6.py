from itertools import count, cycle

print('write only one number')
optin_1 = int(input('write a number: '))

def counter(num):
    for i in count(num):
        print(i)
        if i == num + 20:
            break
result = counter(optin_1)
print(result)

def twist(nimb_2):
    for i in cycle(nimb_2):
        print(i)
        if i == nimb_2[-1]:
            break
optin_2 = list(input('Write a list: '))
result_2 = twist(optin_2)
print(result_2)
