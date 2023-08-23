from mod_id_count import *

def add_data():
	contact = input('Введите Фамилию Имя Отчество Номер, используя пробел: ')
	with open('dict.txt', 'a', encoding='utf-8') as data:
		data.write(f'\n{id_count() + 1} {contact}')