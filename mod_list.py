
def full_list_print():
    data = open('dict.txt', 'r', encoding='utf-8')
    
    while True:
        line = data.readline()
        if not line:
            break
        print(line.strip())
        data.close