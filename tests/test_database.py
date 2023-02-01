from DataBaseClass import DataBase


def test():
    db = DataBase('db/data1.db')

    # results = db.execute('SELECT * FROM movie')
    # results_list = []
    # for row in results:
    #     results_list.append(row)
    results, headers = db.execute('SELECT * FROM movie')

    assert len(results) == 3
    assert results[0][2] == 'action film'
    assert results[0][3] == 'マックG'

    results, headers = db.execute('SELECT * FROM theater')
    assert len(results) == 3

    db.close()
