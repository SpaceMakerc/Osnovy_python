def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        yield result

n = 10
for el in fact(n):
    print(el)
