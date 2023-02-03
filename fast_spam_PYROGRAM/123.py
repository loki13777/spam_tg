import datetime
import random

number_user = 869
time_1 = datetime.datetime.now()
with open('../Петр Реалити в онлайн бизнесе.txt', 'r') as f:
    string_users = f.read()
    list_users = string_users.split('\n')
for i in range(130):

    time_1 = time_1 + datetime.timedelta(seconds=random.randint(3,6))
    time_2 = time_1.time().replace(microsecond=0)
    number_user += 1
    with open('../отчет.txt', 'a') as f:

        f.write(f'{number_user} {time_2} {list_users[number_user]}\n')

