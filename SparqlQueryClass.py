import json
from UriClass import Uri
import re


class SparqlQueryClass:
    def __init__(self, file_name):
        self.query = None
        self.uri = Uri()
        self.var_list = None
        self.trans_uri_list = None
        self.sql_query = None
        self.read_query(file_name)
        pass

    def read_query(self, file_name):
        file = open(file_name, 'r')
        self.query = json.load(file)

    def convert_to_sql(self, map_class):  # sparql to sql conversion
        self.var_list = []  # set up variables list
        for var in self.query['variables']:
            self.var_list.append(var['value'])
        filter_list = []  # set up filter list
        for filter_item in self.query['where']:
            if filter_item['type'] == 'filter':
                prefix = self.query['expression']['args']
                filter_list.append(
                    prefix[0]['value'],
                    prefix[0]['value']+' '+filter_item['expression']['operator']+' "'+
                    prefix[1]['value']+'"')
        self.sql_query = []  # start building sql
        self.trans_uri_list = []
        for triple in self.query['where'][0]['triples']:
            sql_subquery = []
            q_predicate = triple['predicate']['value']
            for mapping in map_class.mappings:  # find a match
                predicate = mapping['predicate']
                if q_predicate == predicate:
                    sql = mapping['SQL']
                    query = triple
                    answer = self.uri.translate_sql(sql, query, mapping, filter_list)
                    re_sql = answer[0]  # revised sql
                    if answer[1]:
                        for ans in answer[1]:
                            self.trans_uri_list.append(ans)  # ans = ['s_id', 'wikidata_title']
                    if re_sql != 'No':
                        sql_subquery.append(re_sql)
            insert_sql = ''
            if len(sql_subquery) != 0:
                for subq in sql_subquery:
                    insert_sql += subq + ' UNION '
                insert_sql = re.sub(r' UNION $', '', insert_sql)
                insert_sql = insert_sql.replace(';', '')+';'
            self.sql_query.append(insert_sql)
        trans_uri_list = list(set(tuple(i) for i in self.trans_uri_list))
        self.trans_uri_list = [list(i) for i in trans_uri_list]
        pass
