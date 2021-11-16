from sys import argv

if len(argv) > 3:
    print(f'Salary is - {int(argv[1]) * int(argv[2]) + int(argv[3])}')
else:
    print('Required 3 arguments!')
