class ComplexNumber:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        result_1 = self.real + other.real
        result_2 = self.imaginary + other.imaginary
        if result_1 == 0:
            return f'{result_2}i'
        elif result_2 == 0:
            return f'{result_1}'
        elif result_2 > 0:
            return f'{result_1} + {result_2}i'
        else:
            return f'{result_1}{result_2}i'
    def __str__(self):
        return f'{self.real}'
    def __mul__(self, other):
        result_1 = (self.real * other.real) + (self.imaginary * other.imaginary) * (-1)
        result_2 = (self.real * other.imaginary) + (self.imaginary * other.real)
        if result_1 == 0 and result_2 == 0:
            return 0
        elif result_2 < 0:
            return f'{result_1} {result_2}i'
        elif result_1 == 0:
            return f'{result_2}i'
        elif result_2 == 0:
            return f'{result_1}'
        else:
            return f'{result_1} + {result_2}i'


user_number = ComplexNumber(1, 2)
comp_number = ComplexNumber(3, 4)
print(user_number + comp_number)
print(user_number * comp_number)
