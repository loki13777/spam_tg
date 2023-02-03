from pyrogram import Client
from function_DB import BotDB

# Target channel/supergroup
chat_id = '@concentratcertain9'
# app = Client("333333333333",12816097,'272c6106b75e4247db091a6e8d8e2b09')
db = BotDB('database_1.db')
db.update_accounts()
accaunts = db.read_users()
a = 0
for el in accaunts[27:57]:
    if el[4] == None:
        name = el[1]
        api_id = el[2]
        api_hash = el[3]
        print(el[0])
        app = Client(name, api_id, api_hash, workdir='C:\\PycharmProjects\\PYROGRAM\\sessions')
        async def get_members():
            async with app:
                # await app.join_chat('https://t.me/joinchat/cqnJi82VJpQ5Y2Fi')
                # async for dialog in app.get_dialogs(limit=5):
                #     print(dialog)
                try:
                    async for i in app.get_chat_members(chat_id, limit=1000):
                        print(i.user.id)
                except Exception as e:
                    print(e)

        app.run(get_members())
