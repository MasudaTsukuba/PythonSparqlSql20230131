# build a rdf graph from csv files
# execute a sparql query against the built graph
# 2023/1/26, T. Masuda

from rdflib import Graph
import pandas as pd
import os


class SparqlDirectQueryClass:
    def __init__(self):
        self.graph = Graph()

    def read_csv(self):
        files = os.listdir('db/csv/data1')
        for file in files:
            try:
                with open('db/csv/data1/'+file) as f:
                    df = pd.read_csv(file)  # , header=True)
                    pass
            except:
                pass
        pass

    def execute_query(self, query):
        results = self.graph.query(query)
