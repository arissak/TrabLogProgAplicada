import sqlite3


class DB:
    def __init__(self, db_name:str):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.connection.execute('''
                                CREATE TABLE IF NOT EXISTS dados(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL, 
                                gender TEXT NOT NULL)
                                ''')

    def save(self,name, gender):
        self.connection.execute('INSERT INTO dados(name, gender) VALUES(:name,:gender)', {'name': name, 'gender': gender})
        self.connection.commit()

    def show(self):
        cursor = self.connection.execute('SELECT name,gender FROM dados ORDER BY id DESC LIMIT 1')
        return cursor.fetchone()

    def close(self):
        return self.connection.close()

