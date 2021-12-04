class Cell:
    i = 3

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        result = self.value + other.value
        return Cell(result)
    def __sub__(self, other):
        result = self.value - other.value
        if result < 0:
            return 'NO'
        else:
            return Cell(result)
    def __mul__(self, other):
        result = self.value * other.value
        return Cell(result)
    def __truediv__(self, other):
        result = self.value // other.value
        return Cell(result)
    def __str__(self):
        return f'{self.value}'

    def make_order(self, number):
        self.result = str()
        while self.value > 0:
            if self.value - number > 0:
                self.result += '*' * number
                self.result += '\n'
                self.value -= number
            else:
                self.result += '*' * self.value
                self.value -= number
        return self.result

cell_1 = Cell(20)
cell_2 = Cell(3)
result = cell_1 / cell_2
print(result)
print(cell_1 + cell_2)
print(cell_1 * cell_2)
print(cell_1 - cell_2)
print(cell_1.make_order(3))
