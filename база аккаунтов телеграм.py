from function_DB import BotDB

db = BotDB('database_1.db')
db.update_accounts()
while True:
    answer = input('1-добавить номер\n2-добавить блокировку\n3-удалить номер\n4-вывести список аккаунтов\n5-выход\n')
    if answer == '1':
        number = input('Введите номер\n')
        if db.number_exist(number):
            print('Такой номер уже существует\n')
        else:
            user_name = input('Введите имя пользователя\n')
            api_id = input('Введите api_id\n')
            api_hash = input('Введите api_hash\n')
            sex = input('Введите пол (Man, Woman)\n')
            db.add_number(user_name, number, api_id, api_hash, sex)
            print('готово\n')
    elif answer == '2':
        number = input('Введите номер\n')
        if db.number_exist(number):
            lock_date = input('Введите дату разблокировки в формате ГГГГ-ММ-ДД ЧЧ:ММ\n')
            db.add_lock_date(number, lock_date)
        else:
            print('Такого номера не существует\n')
    elif answer == '3':
        number = input('Введите номер аккаунта для удаления\n')
        try:
            db.delete_number(number)
            print('готово\n')
        except Exception as e:
            print('Такого номера не существует\n', e)
    elif answer == '4':
        users = db.read_users()
        for el in users:
            print(el)
    elif answer == '5':
        break

a = db.select_unlock_accounts()


print(a)
db.close()
