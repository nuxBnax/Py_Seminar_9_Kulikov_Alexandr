from mod_del import *
from mod_id_count import *

def edit_cont():
	delete_cont()
	contact = input('Введите Фамилию Имя Отчество Номер, используя пробел: ')
	with open('dict.txt', 'a', encoding='utf-8') as data:
		data.write(f'\n{id_count() + 1} {contact}')