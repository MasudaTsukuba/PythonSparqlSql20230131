import csv
import os
import pandas as pd


class Uri:
    def __init__(self):
        self.dictionary = {}
        self.inverse_dictionary = None
        self.dictionaries = {}  # bundle of dictionaries
        self.inverse_dictionaries = {}
        pass

    def read_dictionaries(self):
        path = 'URI/'
        files = os.listdir(path)
        for file in files:
            table = file.replace('.csv', '')
            df = pd.read_csv(path+file, header=None)
            for pair in df.iterrows():
                key = pair[1][0]
                value = pair[1][1]
                try:
                    self.dictionaries[table][key] = value
                except KeyError:
                    self.dictionaries[table] = {}
                    self.dictionaries[table][key] = value
                    pass
                try:
                    self.inverse_dictionaries[table][value] = key
                except KeyError:
                    self.inverse_dictionaries[table] = {}
                    self.inverse_dictionaries[table][value] = key
                    pass
                pass
            pass

    def invert_dictionary(self):
        self.inverse_dictionary = {}
        for item in self.dictionary:
            try:
                key = self.dictionary[item]
                self.inverse_dictionary[key] = item
            except KeyError:
                pass

    def uri(self, input_string):
        pass

    def iru(self, input_uri):
        pass

    def translate_sql(self, sql: str, triple, mapping, filter_list):  # uri translation
        trans_uri = []
        # subject
        subject_value = triple['subject']['value']
        if triple['subject']['termType'] == 'Variable':
            sql = sql.replace(mapping['subject'], subject_value)  # VAR0 -> s_id
            trans_uri.append([subject_value, mapping['subject_uri']])  # s_id: wikidata_title
        elif triple['subject']['termType'] == 'NamedNode':
            uri_function = mapping['subject_uri']
            with open('URI/'+uri_function+'.csv') as g:
                reader = csv.reader(g)
                for row in reader:
                    if subject_value == row[1]:  # URI
                        sql_value = row[0]  # Label
                        break
                sql = self.rewrite_where_sql(sql, sql_value, mapping['subject'])
        # object
        object_value = triple['object']['value']
        if triple['object']['termType'] == 'Variable':
            sql = sql.replace(mapping['object'], object_value)
            trans_uri.append([object_value, mapping['object_uri']])
            for filter_item in filter_list:
                if filter_item[0] == object_value:
                    sql = self.rewrite_where_sql(sql, filter_item[1])
        elif triple['object']['termType'] == 'NamedNode':
            if mapping['object_uri'] == '-':
                if object_value != mapping['object']:
                    return ['No', []]
            else:
                uri_function = mapping['object_uri']
                with open('URI/'+uri_function+'.csv') as g:
                    reader = csv.reader(g)
                    for row in reader:
                        if object_value == row[1]:
                            sql_value = '"'+row[0]+'"'
                            break
                sql = self.rewrite_where_sql(sql, sql_value, mapping['object'])
        else:
            object_value = triple['object']['value']
            uri_function = mapping['object_uri']
            if uri_function == 'plain':
                sql = self.rewrite_where_sql(sql, object_value, mapping['object'])
                sql = sql.replace(mapping['object'], object_value)
        return [sql, trans_uri]

    def rewrite_where_sql(self, sql, sql_value, mapping):
        index = sql.find(';')
        if 'WHERE' in sql:
            re_sql = sql[:index] +' AND ' + mapping + '=' + sql_value + ';'
        else:
            re_sql = sql[:index] +' WHERE ' + mapping + '=' + sql_value + ';'
        return re_sql

    def rewrite_where_sql_filter(self, sql: str, filter):
        index = sql.find(';')
        if 'WHERE' in sql:
            re_sql = sql[:index]+' AND '+filter+';'
        else:
            re_sql = sql[:index]+' WHERE '+filter+';'
        return re_sql
