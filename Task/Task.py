# Задача
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.


filename = "telephone_directory"
file = open(filename, 'a+')
file.close


def main_menu():
    print('Главное меню\n')
    print('1. Показать все Контакты')
    print('2. Добавить новый Контакт')
    print('3. Поиск по телефонному справочнику')
    print('4. Внести изменения в существующий контакт')
    print('5. Удалить существующий контакт')
    print('6. Выход')
    choice = input('Введите команду: ')
    if choice == '1':
        file = open(filename, 'r+')
        contacts = file.read()
        if len(contacts) == 0:
            print("Телефонный справочник пуст")
        else:
            print(contacts)
        file.close
        enter = input('Нажмите Enter для продолжения')
        main_menu()
    elif choice == '2':
        new_contact()
        enter = input('Нажмите Enter для продолжения')
        main_menu()
    elif choice == '3':
        seach_contact()
        enter = input('Нажмите Enter для продолжения')
        main_menu()
    elif choice == '4':
        update_contact()
        enter = input('Нажмите Enter для продолжения')
        main_menu()
    elif choice == '5':
        delete_contact()
        enter = input('Нажмите Enter для продолжения')
        main_menu()
    elif choice == '6':
        print('Завершение работы')


def seach_contact():  # Поиск контакта
    seach_name = input('Введите имя для поиска: ')
    first_char = seach_name[0:]
    seach_name = first_char.upper()
    file = open(filename, 'r+')
    contacts = file.readlines()

    found = False
    for line in contacts:
        if seach_name in line:
            print('Ваш контакт: ', end='')
            print(line)
            found = True
            break
    if found == False:
        print('Контакт отсутствует в телефонном справочнике')


def input_name():  # Ввод имени
    first = input('Введите имя: ')
    first_char = first[0:]
    return first_char.upper()


def input_surname():  # Ввод отчества
    second = input('Введите отчество: ')
    second_char = second[0:]
    return second_char.upper()


def input_surname_2():  # Ввод фамилии
    third = input('Введите фамилию: ')
    third_char = third[0:]
    return third_char.upper()


def new_contact():  # Добавление нового контакта
    name = input_name()
    surname = input_surname()
    surname_2 = input_surname_2()
    phone = input('Введите номер телефона: ')
    contact_det = ('[' + name + ' ' + surname + ' ' +
                   surname_2 + ', ' + phone + ']')
    file = open(filename, 'a')
    file.write(contact_det)
    print('Контакт:\n' + contact_det + '\nуспешно добавлен')


def input_update_name():  # Ввод нового имени
    first_up = input('Введите новое имя: ')
    first_char = first_up[0:]
    return first_char.upper()


def input_update_surname():  # Ввод нового отчества
    second_up = input('Введите новое отчество: ')
    first_char = second_up[0:]
    return first_char.upper()


def input_update_surname_2():  # Ввод новой фамилии
    third_up = input('Введите новую фамилию: ')
    first_char = third_up[0:]
    return first_char.upper()


def input_update_phone():  # Ввод нового номера
    third_up = input('Введите новоый номер: ')
    first_char = third_up[0:]
    return first_char.upper()


def update_contact():  # Обновление существующего контакта
    seach_name = input('Введите имя для поиска: ')
    first_char = seach_name[0:]
    seach_name = first_char.upper()
    file = open(filename, 'r+')
    contacts = file.readlines()

    found = False
    for line in contacts:
        if seach_name in line:
            found = True
            update_name = input_update_name()
            update_surname = input_update_surname()
            update_surname_2 = input_update_surname_2()
            update_phone = input_update_phone()
            contacts = ('[' + update_name + ' ' + update_surname + ' ' +
                        update_surname_2 + ', ' + update_phone + ']')
            file = open(filename, 'w')
            file.write(contacts)
            print('Контакт:\n' + contacts + '\nуспешно обновлен')
        else:
            print('Контакт отсутствует в телефонном справочнике')


def delete_contact():  # Удаление контакта
    seach_name = input('Введите имя для поиска: ')
    first_char = seach_name[0:]
    seach_name = first_char.upper()
    file = open(filename, 'r+')
    contacts = file.readlines()

    found = False
    for line in contacts:
        if seach_name in line:
            found = True
            print("Вы хотите удалить контакт %s (Да / Нет)?: " % seach_name)
            name_del = input('')
            if name_del == 'Да':
                contacts = ('')
                file = open(filename, 'w')
                file.write(contacts)
                print("Вы удалили контакт %s " % seach_name)
            else:
                print("Вы решили не удалять контакт %s " % seach_name)
    else:
            print('Контакт отсутствует в телефонном справочнике')

main_menu()
