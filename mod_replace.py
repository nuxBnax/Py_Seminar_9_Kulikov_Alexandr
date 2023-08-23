
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