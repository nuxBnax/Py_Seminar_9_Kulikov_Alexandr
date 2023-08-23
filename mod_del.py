
def delete_cont():
    del_info = input('Введите данные контакта (Фамилия, Имя или номер): ')
    upload_list = []
    with open('dict.txt', 'r', encoding='utf-8') as data:
        upload_list = data.readlines()
        for line in range(len(upload_list)):
            if del_info.upper() in upload_list[line].upper().split():
                upload_list[line] = ''
                
            # else:
            #     print('Такого контакта или данных в справочнике нет')
            #     exit()
    with open('dict.txt', 'w', encoding='utf-8') as data:
        for i in upload_list:
            data.write(i)