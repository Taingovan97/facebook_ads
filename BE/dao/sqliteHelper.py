import sqlite3

from BE.constants import SQLITE3_PATH


class SqliteHelper:
    def __init__(self,
                 name=None,
                 ):
        self.connection = None
        self.cursor = None

        if name:
            self.open(name)

    def open(self, name):
        try:
            self.connection = sqlite3.connect(name)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            print("Failed connecting to the database ...")

    def create_table(self):
        self.cursor.execute("""CREATE TABLE users(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            year INTEGER,
                            admin INTEGER
                        )""")

    # INSERT & UPDATE
    def edit(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    # SELECT
    def select(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

test = SqliteHelper(SQLITE3_PATH)
#test.create_table()

#test.edit("INSERT INTO users (name, year, admin) VALUES ('John', 1992, 0)")
#print(test.select("SELECT * FROM users")[0][1])
test.edit("UPDATE users SET name = 'Jack' WHERE name = 'John'")
print(test.select("SELECT * FROM users"))

