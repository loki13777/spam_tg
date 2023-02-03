import datetime
from pyrogram import Client


def txt_to_list(name_file_txt: str):
    with open(name_file_txt, 'r') as file:
        string_users = file.read()
        list_users = string_users.split('\n')

    return list_users


def str_to_datetime(date_str: str):
    date_in_format = datetime.datetime.strptime(date_str, '%d.%m.%Y %H:%M')

    return date_in_format


def read_number_txt(name_file_txt: str):
    with open(name_file_txt, 'r') as f:
        number = int(f.read())

    return number


def write_number_txt(name_file_txt: str, input_number: int):
    with open(name_file_txt, 'w') as f:
        f.write(str(input_number))


async def chek_spam_block(app: Client):
    await app.send_message('@SpamBot', '/start')
    async for mess in app.get_chat_history('@SpamBot', limit=1):
        if mess.text[0] == 'D':
            b = mess.text.rfind('until ')
            text = mess.text[b + 6:b + 23]
            time_1 = datetime.datetime.strptime(text, '%d %b %Y, %H:%M')
            return time_1
        elif mess.text[0] == 'З':
            b = mess.text.rfind('сняты ')
            text = mess.text[b + 6:b + 23]
            time_1 = datetime.datetime.strptime(text, '%d %b %Y, %H:%M')
            return time_1
        else:
            return False
