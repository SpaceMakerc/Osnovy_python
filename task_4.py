class Warehouse:
    count_p = 'Printer'
    count_s = 'Scanner'
    count_x = 'Xerox'

    def __init__(self, name_company, dict_pr, dict_sc, dict_xer):
        self.name_company = name_company
        self.dict_pr = dict_pr
        self.dict_sc = dict_sc
        self.dict_xer = dict_xer


    def get_object(self, object):
        self.object = object
        if isinstance(self.object, Printer):
            self.dict_pr[Warehouse.count_p] = [self.object]
            Warehouse.count_p += '1'
        elif isinstance(self.object, Scanner):
            self.dict_sc[Warehouse.count_s] = [self.object]
            Warehouse.count_s += '1'
        else:
            self.dict_xer[Warehouse.count_x] = [self.object]
            Warehouse.count_x += '1'

class OfficeEquipment:

    def __init__(self, title, prise):
        self.title = title
        self.prise = prise

class Printer(OfficeEquipment):
    def __init__(self, title, prise, print_speed):
        super().__init__(title, prise)
        self.print_speed = print_speed

    def __repr__(self):
        return f'{self.title}, {self.prise}, {self.print_speed}'

class Scanner(OfficeEquipment):
    def __init__(self, title, prise, scanning_speed):
        super(Scanner, self).__init__(title, prise)
        self.scanning_speed = scanning_speed

    def __repr__(self):
        return f'{self.title},{self.prise}, {self.scanning_speed}'

class Xerox(OfficeEquipment):
    def __init__(self, title, prise, quantity_function):
        super().__init__(title, prise)
        self.quantity_function = quantity_function
    def __repr__(self):
        return f'{self.title},{self.prise}, {self.quantity_function}'

class Warehouseman:

    def __init__(self, name, wr_house):
        self.name = name
        self.wr_house = wr_house
    def fill_the_warehouse(self, object):
        self.wr_house.get_object(object)

class Exept(Exception):
    def __init__(self, text):
        self.text = text

first = str()
second = int()
third = int()
dict_pr = {}
dict_sc = {}
dict_xer = {}
ware_house = Warehouse('Enjoy', dict_pr, dict_sc, dict_xer)
ware_houser = Warehouseman('Vaska', ware_house)

add_sth = input('write something if you want to begin!')
while add_sth != '':
    add_sth = input('Write 1 if want do add printer, write 2 if want to add scanner, write 3 if want to add xerox: ')
    if add_sth == '1':
        while first != 'stop':
            first = input('Write name of good: ')
            if first == 'stop':
                break
            while second == 0:
                try:
                    second = int(input('write a prise: '))
                    if type(second) is int:
                        continue
                except ValueError:
                    print('Write number!')
            while third == 0:
                try:
                    third = int(input('write the other function: '))
                    if type(third) is int:
                        continue
                except ValueError:
                    print('Write number!')
            result = Printer(first, second, third)
            ware_houser.fill_the_warehouse(result)
    elif add_sth == '2':
        while first != 'stop':
            first = input('Write name of good: ')
            if first == 'stop':
                break
            while second == 0:
                try:
                    second = int(input('write a prise: '))
                    if type(second) is int:
                        continue
                except ValueError:
                    print('Write number!')
            while third == 0:
                try:
                    third = int(input('write the other function: '))
                    if type(third) is int:
                        continue
                except ValueError:
                    print('Write number!')
            result = Scanner(first, second, third)
            ware_houser.fill_the_warehouse(result)
    elif add_sth == '3':
        while first != 'stop':
            first = input('Write name of good: ')
            if first == 'stop':
                break
            while second == 0:
                try:
                    second = int(input('write a prise: '))
                    if type(second) is int:
                        continue
                except ValueError:
                    print('Write number!')
            while third == 0:
                try:
                    third = int(input('write the other function: '))
                    if type(third) is int:
                        continue
                except ValueError:
                    print('Write number!')
            result = Xerox(first, second, third)
            ware_houser.fill_the_warehouse(result)
print(ware_house.dict_pr, ware_house.dict_sc, ware_house.dict_xer)
