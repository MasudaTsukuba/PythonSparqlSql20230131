import sqlite3


class DataBase:
    def __init__(self, db_name):
        self.conn = None
        self.cur = None
        self.connect(db_name)

    def connect(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    def close(self):
        self.conn.close()

    def execute(self, sql):
        return_list = self.cur.execute(sql).fetchall()
        # return_list = []
        # for row in self.cur:
        #     return_list.append(row)
        headers = [col[0] for col in self.cur.description]
        results = [list(i) for i in return_list[1:]]
        return results, headers
