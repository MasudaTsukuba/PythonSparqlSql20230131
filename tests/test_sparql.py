from SparqlClass import Sparql
from rdflib import URIRef, Variable
import numpy as np


def test():
    my_sparql = Sparql()
    my_sparql.read_turtle('rdf/sample.ttl')
    results = my_sparql.graph.query('select * where {?s ?p ?o.}')
    assert len(results.bindings) == 7
    assert np.logical_or(
        results.bindings[0][Variable('s')] == URIRef('http://example.org/#spiderman'),
        results.bindings[0][Variable('s')] == URIRef('http://example.org/#green-goblin'))
