import sqlite3


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
        except sqlite3.Error:
            print("Failed connecting to the database ...\nPlease check your database path")

    def create_table(self, query):
        self.cursor.execute(query)

    # INSERT & UPDATE
    def edit(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    # SELECT
    def select(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
