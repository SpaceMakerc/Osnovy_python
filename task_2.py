from abc import ABC, abstractmethod

class Clothes(ABC):
    a = 0

    def __init__(self, name, parameter):
        self.name = name
        self.parameter = parameter

    @abstractmethod
    def count_sum(self):
        pass

class Coat(Clothes):
    @property
    def count_sum(self):
        self.result = self.parameter / 6.5 + 0.5
        return self.result

    def sum_coat(self, clothes):
        for i in clothes:
            Clothes.a += i.count_sum
        return f'{Clothes.a} for all coats'

class Suit(Clothes):
    @property
    def count_sum(self):
        self.result = 2 * self.parameter + 0.3
        return f'Fabric consumption for {self.name} is {self.result}'


my_coat = Coat('Coat', 3)
my_coat_2 = Coat('Coat', 2)
print(my_coat.count_sum)
my_suit = Suit('Suit', 3)
print(my_suit.count_sum)
all_coat = [my_coat, my_coat_2]
print(my_coat.sum_coat(all_coat))
