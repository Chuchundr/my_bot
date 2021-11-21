import json
from module_for_db import DBExecutor


db_executor = DBExecutor()


# def get_admins_data():
#     admins = db_executor.selector('admins', ['name', 'chat_id'])
#     admins_list = []
#     for row in admins:
#         admins_list.append({'name': row[0], 'chat_id': row[1]})
#     data = {'admins': admins_list}
#     return data
#
# def get_general_data():
#     general_data = db_executor.selector('general_info', ['name', 'text'])


class Data:
    def __init__(self, table: str, columns: list):
        self.db_executor = DBExecutor()
        self.table = table
        self.columns = columns

    def getter_func(self):
        data = self.db_executor.selector(self.table, self.columns)
        data = [row for row in data]
        return data

    def to_dict(self):
        data = self.getter_func()
        data_dict = dict()
        for row in data:
            data_dict.update({row[0]: row[1]})
        return data_dict

