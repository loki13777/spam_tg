from function_DB import BotDB
db = BotDB('database_1.db')

with open('свеж.txt', 'r', encoding='UTF-8') as file:
    a = file.read().replace('App', '').replace('api_id:', '').replace('api_hash:', '')
    a = a.split()
    print(a)
for n, el in enumerate(a):
    if el.isalpha() and len(el)>5:
        print(el,n)
        print(a[n+1])
        print(a[n+2])
        print(a[n+3] )
        print(a[n+4], '\n\n')
        db.add_number(el, a[n+1], a[n+2], a[n+3], a[n+4])