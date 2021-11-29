class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage' : wage, 'bonus' : bonus}

class Position(Worker):

    def get_full_name (self):
        full_name = self.name + ' ' + self.surname
        return full_name
    def get_total_income (self):
        total_income = self._income['wage'] + (self._income['bonus'] / 100 * self._income['wage'])
        return total_income
diman = Position('Diman', 'Kotov', 'ingener', 37000, 10)
kolyan = Position('Nikolay', 'Petrov', 'builder', 40000, 15)
dasha = Position('Dasha', 'Seryabkina', 'translator', 35000, 20)

name_1 = Position.get_full_name(diman)
money_1 = Position.get_total_income(diman)
print(name_1, money_1)
name_2 = Position.get_full_name(kolyan)
money_2 = Position.get_total_income(kolyan)
print(name_2, money_2)
name_3 = Position.get_full_name(dasha)
money_3 = Position.get_total_income(dasha)
print(name_3, money_3)
