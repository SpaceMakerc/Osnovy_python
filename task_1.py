with open('text_1.txt', 'w') as file_1:
    content = []
    inform = input('write something, if you want to begin: ')
    while inform != '':
        inform = input(f'write information about yourself: ')
        if inform == '':
            continue
        content.append(inform)
    file_1.writelines(content)
