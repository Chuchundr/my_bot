import os
import sqlite3


def get_db(file: str):
    if file.split('.')[-1] == 'db':
        return file


class DBExecutor:
    def __init__(self):
        dbname = list(filter(get_db, os.listdir()))[0]
        self.conn = sqlite3.connect(dbname, check_same_thread=False)
        # self.cursor = self.conn.cursor()

    def selector(self, table: str, *cols):
        columns = '*' if not cols else ', '.join(cols[0])
        command = f'select {columns} from {table}'
        with self.conn as conn:
            cur = conn.cursor()
            cur.execute(command)
            data = cur.fetchall()
        return data

    # def inserter(self, table: str, **kwargs):
    #     cols = [str(key) for key in kwargs.keys()]
    #     values = [str(val) for val in kwargs.values()]
    #     print(cols, values)
    #     command = f'insert into {table} ({", ".join(cols)}) values ({(", ".join(values))})'
    #     self.cursor.execute(command)
    #     self.conn.commit()
    #     return
