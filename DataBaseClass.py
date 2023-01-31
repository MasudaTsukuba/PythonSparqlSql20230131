import sqlite3


class DataBase:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connect(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    def close(self):
        self.conn.close()

    def execute(self, sql):
        self.cur.execute(sql)
        return_list = []
        for row in self.cur:
            return_list.append(row)
        return return_list
