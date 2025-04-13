import sqlite3


class DB:
    def __init__(self, db_name:str):
        self.db_name: db_name
        self.connection = sqlite3.connect(db_name)
        self.connection.execute('''
                                CREATE TABLE IF NOT EXISTS dados(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL, 
                                gender TEXT NOT NULL, 
                                date TEXT NOT NULL
                                ''')

    def save(self):
        self.connection.execute('INSERT INTO dados(name, gender, date) VALUES(:name,:gender,:date)')
        self.connection.commit()

    def show(self):
        return self.connection.execute('SELECT nome FROM dados ORDER BY id DESC LIMIT 1').fetchall()

    def close(self):
        return self.connection.close()

