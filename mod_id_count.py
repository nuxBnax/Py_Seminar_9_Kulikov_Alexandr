
def id_count():
    
    upload_list = []
    with open('dict.txt', 'r', encoding='utf-8') as data:
        upload_list = (data.readlines())[-1]
        new_list = (upload_list.split())[0]
        new_list = int(new_list)
        return new_list
