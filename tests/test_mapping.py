from MappingClass import Mapping


def test():
    mapping = Mapping('mapping/sample.json')
    assert mapping.mappings['book1']['year'] == 2005


def test2():
    mapping = Mapping('mapping/mapping.json')
    assert mapping.mappings[0]['mappingID'] == 1
