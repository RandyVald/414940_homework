def creat_new_data():

    str_data = "Vanya 89991112222 Moskow"
    list_1 = str_data.split()

    str_data2 = "Petya 89991117777 StPeterburg"
    list_2 = str_data2.split()

    with open('file.txt', 'w') as data:
        data.write(' '.join(list_1)+'\n')
        data.write(' '.join(list_2)+'\n')

def print_data(file_name):
    print('')
    with open(file_name, 'r') as data:
        for line in data:
            print(line)

def add_line(file_name, input_line):
    with open(file_name, 'a') as data:
        data.write(input_line + '\n')

def find_for_name(file_name, input_line):
    res = ''
    with open(file_name, 'r') as data:
        for line in data:
            list_1 = line.split()
            if input_line in list_1:
                print("Нашлась запись:")
                print(line)

def copy_line(file_name, file_name_two, number_string ):
    list_1 = list()
    with open(file_name, 'r') as data:
        for line in data:
            list_1.append(line)
    with open(file_name_two, 'a') as data:
        data.write(list_1[number_string-1])

file_name = "file.txt"
file_name_two = "file2.txt"
selected_value = 1

while selected_value != 0:
    print(' ')
    print('Если хотите вывести справочник нажмите 1')
    print('Если добавить запись в справочник нажмите 2')
    print('Найти запись в справочнике нажмите 3')
    print('Скопировать строку из одного файла в другой нажмите 4')
    print('Завершить программу введите 0')
    print(' ')

    selected_value = int(input("введите команду: "))

    if selected_value == 1:
        print_data(file_name)
    elif selected_value == 2:
        print('Введите строку для добавления в справочник в формате ФИО Телефон Город') 
        input_line = input('Строка для добавления: ')
        add_line(file_name, input_line)
    elif selected_value == 3:
        print('Введите имя для поиска в базе: ')
        input_line = input("Введите имя: ")
        find_for_name(file_name, input_line)
    elif selected_value == 4:
        print('Введите номер строки из файла 1 для копирования в файл 2: ')
        number_string = int(input("Введите номер строки: "))
        copy_line(file_name, file_name_two, number_string)

print("Программа завершена!")
print(' ')