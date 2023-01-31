from UriClass import Uri


def test():
    uri = Uri()
    uri.invert_dictionary()
    assert uri.dictionary['Q191543'] == 'ターミネーター4'
    assert uri.inverse_dictionary['ターミネーター4'] == 'Q191543'
