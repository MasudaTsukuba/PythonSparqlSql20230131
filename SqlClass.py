import re


class SqlClass:
    def __init__(self):
        pass

    def convert(self, var_list, sql_query):
        select_var = ''
        for var in var_list:
            select_var += var+', '
        select_var = re.sub(', $', '', select_var)  # remove comma at the end
        exe_query = 'SELECT '+select_var+' FROM '
        for item in sql_query:
            exe_query += ' ('+item+') NATURAL JOIN '
        exe_query = re.sub('NATURAL JOIN $', '', exe_query)  # remove NATURAL JOIN at the end
        exe_query = exe_query.replace(';', '')+';'
        return exe_query
