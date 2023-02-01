from SparqlQueryClass import SparqlQueryClass


def test():
    sparql_query = SparqlQueryClass('sparql/query.json')
    assert len(sparql_query.query) == 5
