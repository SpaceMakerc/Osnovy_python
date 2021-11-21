with open('text_2.txt', 'r' ) as obj_2:
    result = obj_2.readlines()
    print(result)
    print(len(result))
    count = 1
    for str in result:
        if str != result[-1]:
            print(f'Длина строки № {count} - ', len(str) - 1)
            count += 1
        else:
            print(f'Длина строки № {count} - ', len(str))
