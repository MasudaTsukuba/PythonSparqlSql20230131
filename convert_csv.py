# convert_csv.py
# convert csv file by replacing each item with its uri
# 2023/2/2, T. Masuda

# import OS module
import os
import pandas as pd
from MappingClass import Mapping
from UriClass import Uri

conversion_table = {}
mapping_class = Mapping('mapping/mapping.json')
uri = Uri()
uri.read_dictionaries()


def check_uri():
    for mapping in mapping_class.mappings:
        extract_variable(mapping, 'subject')
        extract_variable(mapping, 'object')
        pass
    pass


def extract_variable(mapping, target):
    conversion = mapping[target+'_uri']
    if conversion != '-':
        variable_name = mapping[target]
        sql = mapping['SQL']
        variables_dict, tables_list = decompose_sql(sql)
        for table in tables_list:
            variable = variables_dict[variable_name]
            try:
                conversion_table[table][variable] = conversion
            except KeyError:
                conversion_table[table] = {}
                conversion_table[table][variable] = conversion
        pass
    pass


def decompose_sql(sql: str):
    after_select = sql.split('SELECT ')[1]
    temp = after_select.split(' FROM ')
    variables_part = temp[0]
    tables_part = temp[1].split(';')[0].split(' WHERE')[0]
    variables_list = variables_part.split(',')
    variables_dict = {}
    for variable in variables_list:
        temp = variable.split(' AS ')
        temp_var_name = temp[0].replace(' ', '')
        if temp_var_name.find('.') >= 0:
            temp_var_name = temp_var_name.split('.')[1]
        variables_dict[temp[1].replace(' ', '')] = temp_var_name
    tables_list = tables_part.replace(' ', '').split(',')
    pass
    return variables_dict, tables_list


def convert_table():
    for (root, dirs, file) in os.walk('db/csv/'):
        for f in file:
            if '.csv' in f:
                # print(f)
                df = pd.read_csv(root+'/'+f)
                table = f.replace('.csv', '')
                columns = conversion_table[table]
                for key, value in columns.items():
                    if value != 'plain':
                        try:
                            data = df[key]
                            data_converted = [uri.dictionaries[value][element] for element in data]
                            df[key+'_uri'] = data_converted
                        except KeyError:
                            pass
                    pass
                pass
                path = 'db/csv_converted/'
                if not os.path.exists(path):
                    os.makedirs(path)
                df.to_csv(path+f.replace('.csv', '_uri.csv'))
    pass


check_uri()
convert_table()
