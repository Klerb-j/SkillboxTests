
# Проверка на правильный выбор в Меню

def choice_fixer():
    try:
        choice = int(input('Введите номер пункта меню: '))
    except ValueError:
        print('\nВведите число!')
        choice = False
    return choice

# Проверка Индекса в personal_information_check

def postcode_func():
    index_letter_checker = 0
    index = input('Введите почтовый Индекс: ')
    number = ''
    for index_checker in index:
        if index_checker.isdigit():
            index_letter_checker += 1
            number += index_checker
        else:
            continue
    if index_letter_checker == 0:
        print('В индексе должна быть хоть одна Цифра.')
        return postcode_func()
    return number

# Отвечает за проверку на "ничего" в personal_information_updated

def check_nothing(new_value, old_value):
    return new_value.strip() if new_value.strip() else old_value

# Главное Меню

def main_menu(personal_info=None, personal_information_check=False, enterpreneur_information_check=False, enterpreneur_info=None):
    filler_string = '--------------------------------------------'
    while True:
        print(filler_string, '\nГЛАВНОЕ МЕНЮ')
        print('1 - Ввести или обновить информацию')
        print('2 - Вывести информацию')
        print('0 - Завершить Работу')

        menu_choice = choice_fixer()
        if menu_choice == 0:
            exit('Завершение Программы...')
        elif menu_choice == 1:
            while True:
                print(filler_string, '\nВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
                print('1 - Личная информация')
                print('2 - Информация о предпринимателе')
                print('0 - Назад')
                menu_choice = choice_fixer()
                if menu_choice == 0:
                    break
                elif menu_choice == 1:
                    personal_info, personal_information_check = personal_information_func(
                        personal_information_check, personal_info, filler_string
                    )
                elif menu_choice == 2:
                    enterpreneur_information_check, enterpreneur_info = enterpreneur_information_func(
                        enterpreneur_information_check, enterpreneur_info, filler_string
                    )
                elif menu_choice is False:
                    continue
                else:
                    print('Выбран Некорректный Пункт меню.')
        elif menu_choice == 2:
            view_information(
                personal_information_check, personal_info,
                enterpreneur_information_check, enterpreneur_info, filler_string
            )
        elif menu_choice is False:
            continue
        else:
            print('Выберите подходящее из списка.')

# Запрос Персон. Информации

def personal_information_func(personal_information_check, personal_info, filler_string):
    print(filler_string)
    if personal_information_check == True:
        personal_information_update(personal_info, filler_string)
        return personal_info, personal_information_check  #
    else:
        name = input('Введите Имя: ')
        age = input('Введите Возраст: ')
        while True:
            user_phone = input('Введите Номер Телефона(+7XXXXXXXXXX): ')
            cleared_user_phone = ''.join(filter(str.isdigit, user_phone))
            if len(cleared_user_phone) != 11:
                print('Номер телефона должен состоять из 11 цифр')
                continue
            break

        while True:
            email = input('Введите Электронную почту: ')
            if '.' not in email or '@' not in email:
                print('Электронная почта должна содержать и точку, и @')
            else:
                break

        postcode = postcode_func()
        address = input('Введите Адрес: ')
        add_info = input('Введите Доп. Информацию (нажмите Enter чтобы пропустить): ')

        personal_info_data = [name, age, cleared_user_phone, email, postcode, address, add_info]
        personal_information_check = True
        return personal_info_data, personal_information_check

# Обновление Персональной Информации

def personal_information_update(personal_info, filler_string):
    name_updated = input(f'Введите Имя (Enter - чтобы оставить прежние данные ({personal_info[0]})): ')
    personal_info[0] = check_nothing(name_updated, personal_info[0])

    age_updated = input(f'Введите Возраст (Enter - чтобы оставить прежние данные ({personal_info[1]})): ')
    personal_info[1] = check_nothing(age_updated, personal_info[1])
    while True:
        user_phone_updated = input(f'Введите Номер Телефона (+7XXXXXXXXXX) (Enter - чтобы оставить прежние данные ({personal_info[2]})): ')
        if user_phone_updated.strip() == "":
            break
        cleared_user_phone = ''.join(filter(str.isdigit, user_phone_updated))
        if len(cleared_user_phone) != 11:
            print('Номер телефона должен состоять из 11 цифр')
            continue
        personal_info[2] = cleared_user_phone
        break
    while True:
        email_updated = input(f'Введите Электронную почту (Enter - чтобы оставить прежние данные ({personal_info[3]})): ')
        if email_updated.strip() == "":
            break
        if '.' not in email_updated or '@' not in email_updated:
            print('Электронная почта должна содержать "." и "@"')
        else:
            personal_info[3] = email_updated
            break
    postcode_updated = input(f'Введите Почтовый индекс (Enter - чтобы оставить прежние данные ({personal_info[4]})): ')
    personal_info[4] = check_nothing(postcode_updated, personal_info[4])
    address_updated = input(f'Введите Адрес (Enter - чтобы оставить прежние данные ({personal_info[5]})): ')
    personal_info[5] = check_nothing(address_updated, personal_info[5])
    add_info_updated = input(f'Введите Доп. Информацию (Enter - чтобы оставить прежнюю ({personal_info[6]})): ')
    personal_info[6] = check_nothing(add_info_updated, personal_info[6])


# Вывод персон. Информации

def view_personal_info(personal_information_check, personal_info, filler_string):
    personal_info_understanding = ['Имя', 'Возраст', 'Номер телефона', 'Электронная почта', 'Индекс', 'Адрес', 'Доп. Информация']
    word_count = 0
    print(filler_string)
    if personal_information_check == True:
       while word_count != len(personal_info):
           if word_count == 0:
               print('Ваше Имя: ', personal_info[word_count])
               word_count += 1
               continue
           elif word_count == 3:
               print('Ваша Электронная почта: ', personal_info[word_count])
               word_count += 1
               continue
           elif word_count == 6 and personal_info[6] != '':
               print('Ваша Доп. Информация: ', personal_info[6])
               word_count += 1
               continue
           elif word_count == 6 and not personal_info [6] != '':
               print('Нету Доп. Информации.')
               word_count += 1
               continue
           else:
               print(f'Ваш {personal_info_understanding[word_count]}: ', personal_info[word_count])
               word_count += 1
               continue
    else:
        print('Нету Персональной Информации.')

# Запрос Предпринимательской Информации

def enterpreneur_information_func(enterpreneur_information_check, enterpreneur_info, filler_string):
    print(filler_string)
    if enterpreneur_information_check == True:
        enterpreneur_information_update(enterpreneur_info)
        return enterpreneur_information_check, enterpreneur_info
    else:
        while True:
            ogrnip = input('Введите ОГРНИП: ')
            if ogrnip.isalpha():
                print('ОГРНИП должен состоять из цифр.')
                continue
            elif int(len(ogrnip)) != 15:
                print('ОГРНИП должен иметь 15 цифр.')
                continue
            else:
                break
        while True:
            inn = input('Введите ИНН: ')
            if inn.isalpha():
                print('ИНН должен состоять из цифр.')
            elif int(len(inn)) != 15:
                print('ИНН должен иметь 15 цифр.')
                continue
            else:
                break
        while True:
            current_account = input('Введите расчетный счет: ')
            if current_account.isalpha():
                print('Расчетный счет должен состоять из цифр.')
                continue
            elif int(len(current_account)) != 20:
                print('Расчетный счет должен содержать 20 цифр.')
                continue
            else:
                break
        bank_name = input('Введите название банка: ')
        bik = input('Введите БИК: ')
        correspondent_account = input('Введите корреспондентский счет: ')
        enterpreneur_information_check = True
        enterpreneur_info_data = [ogrnip, inn, current_account, bank_name, bik, correspondent_account]
        return enterpreneur_information_check, enterpreneur_info_data

def enterpreneur_information_update(enterpreneur_info):
    ogrnip_updated = input(f'Введите ОГРНИП (Enter - чтобы оставить прежние данные ({enterpreneur_info[0]})): ')
    if ogrnip_updated.strip().isdigit() and len(ogrnip_updated) == 15:
        enterpreneur_info[0] = ogrnip_updated

    inn_updated = input(f'Введите ИНН (Enter - чтобы оставить прежние данные ({enterpreneur_info[1]})): ')
    if inn_updated.strip().isdigit() and len(inn_updated) == 15:
        enterpreneur_info[1] = inn_updated

    current_account_updated = input(f'Введите расчетный счет (Enter - чтобы оставить прежние данные ({enterpreneur_info[2]})): ')
    if current_account_updated.strip().isdigit() and len(current_account_updated) == 20:
        enterpreneur_info[2] = current_account_updated

    bank_name_updated = input(f'Введите название банка (Enter - чтобы оставить прежние данные ({enterpreneur_info[3]})): ')
    enterpreneur_info[3] = check_nothing(bank_name_updated, enterpreneur_info[3])

    bik_updated = input(f'Введите БИК (Enter - чтобы оставить прежние данные ({enterpreneur_info[4]})): ')
    enterpreneur_info[4] = check_nothing(bik_updated, enterpreneur_info[4])

    correspondent_account_updated = input(f'Введите корреспондентский счет (Enter - чтобы оставить прежние данные ({enterpreneur_info[5]})): ')
    enterpreneur_info[5] = check_nothing(correspondent_account_updated, enterpreneur_info[5])

# Вывод Предпринимательской Информации

def view_enterpreneur_info(enterpreneur_information_check, enterpreneur_info, filler_string):
    enterpreneur_info_understand = ['ОГРНИП', 'ИНН', 'Р/с', 'Банк', 'БИК', 'Корреспондентский счет']
    word_count = 0
    print(filler_string)
    if enterpreneur_information_check == True:
        while word_count != len(enterpreneur_info):
            print(f'Ваш {enterpreneur_info_understand[word_count]}: ', enterpreneur_info[word_count])
            word_count += 1
    else:
        print('Нету информации о предпринимателе.')

# Вывод Информации

def view_information(personal_information_check, personal_info, enterpreneur_information_check, enterpreneur_info, filler_string):
    print(filler_string, '\nВЫВЕСТИ ИНФОРМАЦИЮ')
    print('1 - Общая информация')
    print('2 - Вся информация')
    print('0 - Назад')
    menu_choice = choice_fixer()

    if menu_choice == 0:
        return
    elif menu_choice == 1:
        view_personal_info(personal_information_check, personal_info, filler_string)
    elif menu_choice == 2:
        view_personal_info(personal_information_check, personal_info, filler_string)
        view_enterpreneur_info(enterpreneur_information_check, enterpreneur_info, filler_string)
    else:
        print('Выбран Некорректный Пункт меню.')
print('Приложение MyProfile')
print('Сохраняй Информацию о себе и выводи её в разных форматах')
main_menu()