from mod_functions_join import *

def logic(text):
    if text == 'lst':
        full_list_print()
    elif text == 'add':
        add_data()
    elif text =='find':
        find_cont()
    elif text == 'del':
        delete_cont()
    elif text == 'num':
        id_count()
    elif text == 'edit':
        print('Введите:\n fam - для изминения Фамилии, \n all - для изменения всей информации о контакте')
        text_1 = input_cmd()
        if text_1 == 'fam':
            edit_fam_cont()
        else:
            text_1 == 'all'
            edit_cont()
    else:
        text ==  'exit'
        exit()