class Error(Exception):

    def __init__(self, text):
        self.text = text

try:
    numerator = int(input('write a numerator: '))
    denominator = int(input('write a denominator: '))
    if denominator == 0 or numerator == 0:
        raise Error('there is a mistake here, you can"t use zero ')
except Error as e:
    print(e)
else:
    result = numerator / denominator
    print(result)

print("Do it again!")
