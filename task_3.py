class Exept(Exception):

    def __init__(self, text):
        self.text = text

result = []
user_number = str
while user_number != 'stop':
    try:
        user_number = input('wtite a number: ')
        if user_number == 'stop':
            continue
        elif user_number.isdigit():
            result.append(user_number)
        else:
            raise Exept("It's not a number!!!")
    except Exept as e:
        print(e)
print(result)
