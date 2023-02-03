from pyrogram import Client


# Target channel/supergroup
chat_id = '@tvoivibor_surgut'

app = Client("333333333333",12816097,'272c6106b75e4247db091a6e8d8e2b09')


async def get_members():
    async with app:
        # async for dialog  in app.get_dialogs() :
        # #     print(dialog.chat.first_name, dialog.chat.id)
        # # a = await app.get_chat(chat_id)
        # # print(a)
        async for member in app.get_chat_members(chat_id, limit=1000):
            print(member.user.id)
            with open('ТВОЙ ВЫБОР.txt', 'a') as file:
                file.write(f'{member.user.id}\n')

app.run(get_members())