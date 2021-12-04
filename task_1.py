class Matrix:
    a = str()
    b = 0

    def __init__(self, value):
        self.lists = value
        self.count = self.lists.copy()
        for el in self.count:
            el = str(el)
            Matrix.a += el + '\n'

    def __str__(self):
        return f'{Matrix.a}'

    def __add__(self, other):
        self.result = []
        while Matrix.b < len(other.lists):
            draf =(list(map(lambda a, b: a + b, self.lists[Matrix.b], other.lists[Matrix.b])))
            Matrix.b += 1
            self.result.append(draf)
        return Matrix(self.result)


numbers_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lists_1 = Matrix(numbers_1)
numbers_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lists_2 = Matrix(numbers_2)
result = lists_1 + lists_2
print(result)
