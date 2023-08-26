
def input_cmd():
    return input('Введите желаемую команду: ')


def add_data():
	contact = input('Введите Фамилию Имя Отчество Номер, используя пробел: ')
	with open('dict.txt', 'a', encoding='utf-8') as data:
		data.write(f'\n{id_count() + 1} {contact}')


def delete_cont():
    del_info = input('Введите данные контакта (Фамилия, Имя или номер): ')
    upload_list = []
    with open('dict.txt', 'r', encoding='utf-8') as data:
        upload_list = data.readlines()
        for line in range(len(upload_list)):
            if del_info.upper() in upload_list[line].upper().split():
                upload_list[line] = ''
                
    with open('dict.txt', 'w', encoding='utf-8') as data:
        for i in upload_list:
            data.write(i)


def edit_cont():
	delete_cont()
	contact = input('Введите Фамилию Имя Отчество Номер, используя пробел: ')
	with open('dict.txt', 'a', encoding='utf-8') as data:
		data.write(f'\n{id_count() + 1} {contact}')
                

def find_cont():
    find_info = input('Уточните параметры поиска (Фамилия, Имя или номер телефона)? ')
    with open('dict.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if find_info.upper() in line.upper().split():
                print(line, end = '')        


def id_count():
    
    upload_list = []
    with open('dict.txt', 'r', encoding='utf-8') as data:
        upload_list = (data.readlines())[-1]
        new_list = (upload_list.split())[0]
        new_list = int(new_list)
        return new_list


def full_list_print():
    data = open('dict.txt', 'r', encoding='utf-8')
    
    while True:
        line = data.readline()
        if not line:
            break
        print(line.strip())
        data.close


def edit_fam_cont():
    find_info = input('Введите Фамилию контакта которую хотите заменить:')
    new_info = input('Введите новую Фамилию контакта: ')
    
    
    with open('dict.txt', 'r', encoding='utf-8') as data:
        upload_list = "".join(data.readlines())
        print(upload_list)
        new_list = upload_list.replace(find_info, new_info)

    with open('dict.txt', 'w', encoding='utf-8') as data:
        for i in new_list:
            data.write(i)