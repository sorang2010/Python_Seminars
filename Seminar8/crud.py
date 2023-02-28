def init_db_txt(file_name = 'db.txt'):
    with open(file_name,'w+', encoding='utf-8') as data:
        # data.write()
        data.close()


def row_create():
    info = []
    
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    mid_name = input('Введите отчество: ')
    info.append(mid_name)
    phone_number = input('Введите номер телефона: ')
    info.append(phone_number)

    with open('db.txt', 'a', encoding='utf-8') as data:
        data.write(f'{info[0]} {info[1]} {info[2]} {info[3]}\n')
        data.close()


def row_read():
    with open('db.txt','r') as file:
        lines = file.readlines()
        for line in lines:
            print(line)
        file.close()


def row_find(str_search):
    with open('db.txt','r') as file:
        lines = file.readlines()
        for line in lines:
            if str_search in line:
                print(line)
        file.close()


def row_replace(str_search, str_replace):
    with open('db.txt','r') as file:
        lines = file.readlines()
        file.close()
    with open('db.txt','w') as file1:    
        for line in lines:
            # print(line)
            if str_search not in line:
                file1.write(line)
                # print(line)
            else:
                file1.write(line.replace(str_search, str_replace))
                # print(line)
        file1.close()


def row_delete(str_search):
    with open('db.txt','r') as file:
        lines = file.readlines()
        file.close()
    with open('db.txt','w') as file1:    
        for line in lines:
            # print(line)
            if str_search not in line:
                file1.write(line)
                # print(line)
        file1.close()