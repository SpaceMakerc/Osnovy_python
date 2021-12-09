class Data:
    result = str()
    months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

    def __init__(self, data):
        self.data = data
        for i in self.data:
            if i.isdigit():
                Data.result += i
            else:
                Data.result += '-'

    @classmethod
    def transformation(clc):
        return clc.result
    @staticmethod
    def validation(data):
        result = []
        counter = data.split('-')
        if counter[0].isdigit():
            result.append('First number is right ')
        else:
            result.append('First number is wrong')
        if counter[1] in Data.months:
            result.append('Second number is right ')
        else:
            result.append('Second number is wrong ')
        if counter[2].isdigit():
            result.append('Third number is right')
        else:
            result.append('Third number is wrong')
        return result


my_str = input('Write a date like "13-3-1333: ')
counter = Data(my_str)
print(Data.result)
print(Data.validation(my_str))
