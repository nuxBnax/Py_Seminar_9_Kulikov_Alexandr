
def find_cont():
    find_info = input('Уточните параметры поиска (Фамилия, Имя или номер телефона)? ')
    with open('dict.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if find_info.upper() in line.upper().split():
                print(line, end = '')        