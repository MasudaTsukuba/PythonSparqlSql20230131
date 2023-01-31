from MappingClass import Mapping


def test():
    mapping = Mapping()
    mapping.load('mapping/sample.json')
    assert mapping.mapping['book1']['year'] == 2005
