from rdflib import Graph


class Sparql:
    def __init__(self):
        self.graph = Graph()
        pass

    def read_turtle(self, file_name):
        self.graph.parse(file_name)
        pass
