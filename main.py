import csv

from DataBaseClass import DataBase
from MappingClass import Mapping
from SparqlClass import Sparql
from UriClass import Uri
from SparqlQueryClass import SparqlQueryClass
from SqlClass import SqlClass
from SparqlDirectQueryClass import SparqlDirectQueryClass
from OutputClass import Output

# set up mapping data
map_class = Mapping('mapping/mapping.json')

# set up database
db = DataBase('db/data1.db')

sparql_query = SparqlQueryClass('sparql/query.json')  # set up sparql query
sparql_query.convert_to_sql(map_class)  # convert uri to literals

sql = SqlClass()
exe_query = sql.convert(sparql_query.var_list, sparql_query.sql_query)  # sparql to sql
results, headers = db.execute(exe_query)  # execute sql query

output = Output(results, headers, sparql_query.trans_uri_list)
