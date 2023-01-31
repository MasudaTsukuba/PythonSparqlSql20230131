from DataBaseClass import DataBase
from MappingClass import Mapping
from SparqlClass import Sparql
from UriClass import Uri
from SparqlQueryClass import SparqlQueryClass

db = DataBase()
db_name = 'db/data1.db'
db.connect(db_name)

results = db.execute('SELECT * FROM movie')

db.close()

sparql_query_instance = SparqlQueryClass()
sparql_query_instance.read_csv()
