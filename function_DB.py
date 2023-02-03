import sqlite3

class BotDB:
    def __init__(self, db_file):
        """инициализайция соединения с БД"""
        self.db = sqlite3.connect(db_file)
        self.cursor = self.db.cursor()

    def number_exist(self, number):
        '''проверяем есть ли юззер в БД'''
        result = self.cursor.execute('SELECT number FROM accounts WHERE number = ?', [number])
        return bool(len(result.fetchall()))

    def add_number(self, user_name, number, api_id, api_hash, sex):
        '''добавляем юзера в БД'''
        self.cursor.execute("INSERT INTO accounts VALUES (?, ?, ?, ?, ?, ?, ?)", [None, user_name, number, api_id, api_hash, None, sex])
        return self.db.commit()

    def add_lock_date(self, number, lock_date):

        self.cursor.execute('UPDATE accounts SET lock_date=? WHERE number=?', [lock_date, number])
        return self.db.commit()

    def select_unlock_accounts(self):

        result = self.cursor.execute('SELECT * FROM accounts WHERE lock_date is null')
        return result.fetchall()

    def update_accounts(self):

        self.cursor.execute('UPDATE accounts SET lock_date = ? WHERE lock_date <= CURRENT_TIMESTAMP', [None])
        return self.db.commit()

    def read_users(self):

        spisok = []
        for el in self.cursor.execute("SELECT user_name, number, api_id, api_hash, lock_date, sex FROM accounts"):
            a = (el[0], el[1], el[2], el[3], el[4], el[5])
            spisok.append(a)
        return spisok



    def delete_number(self, number):

        self.cursor.execute(f'DELETE FROM accounts WHERE number = ?', [number])
        return self.db.commit()

    def update_sex(self):
        self.cursor.execute(f"update accounts set sex = ? WHERE user_name  in ('Хадича', 'АняСафарова','АллаНекрасова','Лариса','КристинаКошелева','Алина','Вика','Вероника','Любовь','МашаКошелева')", ['Woman'])
        self.cursor.execute("update accounts set sex = ? WHERE user_name not  in ('Хадича', 'АняСафарова','АллаНекрасова','Лариса','КристинаКошелева','Алина','Вика','Вероника','Любовь','МашаКошелева')", ['Man'])
        return self.db.commit()
    def close(self):
        self.db.close()

    def update_TABLE(self):
        self.cursor.execute(f'ALTER TABLE accounts ADD COLUMN serial_number INTEGER AUTO_INCREMENT')
        return self.db.commit()
