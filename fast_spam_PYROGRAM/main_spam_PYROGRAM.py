from pyrogram import Client, errors
from function_DB import BotDB
import datetime
import asyncio
import time
from fast_spam_config import str_time_send_message, name_file_users, name_file_number, message1, message2
from fast_spam_function import txt_to_list, str_to_datetime, read_number_txt,\
    write_number_txt, chek_spam_block

db = BotDB('../database_1.db')

numbers = txt_to_list(name_file_users)
time_send_message = str_to_datetime(str_time_send_message)
print(numbers)

while True:
    db.update_accounts()
    accaunts = db.read_users()
    for el in accaunts[27:57]:
        if el[4] == None:
            number_user = read_number_txt(name_file_number)
            if number_user < 500:
                message = message1
            else:
                message = message2
            name = el[1]
            api_id = el[2]
            api_hash = el[3]
            print(el[0])
            app = Client(name, api_id, api_hash,
                         workdir='C:\\PycharmProjects\\PYROGRAM\\sessions',
                         app_version="1.2.3",
                         device_model="Unknown browser",
                         system_version="Unknown browser")

            async def send_():
                async with app:
                    try:
                        await app.send_message(numbers[number_user],
                                               message1,
                                               disable_notification=True
                                               )
                        print(f'отправлено юзеру {number_user}')
                        await asyncio.sleep(3)
                        write_number_txt(name_file_number, number_user+1)
                        with open('../отчет.txt', 'a') as f:
                            time_1 = datetime.datetime.now().time().replace(microsecond=0)
                            f.write(f'{number_user} {time_1} {numbers[number_user]}\n')
                    except errors.PeerFlood as e:
                        print('error', e)
                        time_1 = await chek_spam_block(app)
                        db.add_lock_date(el[1], time_1)
                        await asyncio.sleep(3)
                    except Exception as e:
                        print(e)
                        write_number_txt(name_file_number, number_user+1)
                        await asyncio.sleep(3)
            app.run(send_())
    # time_send_message += datetime.timedelta(seconds=10)

    time.sleep(30)