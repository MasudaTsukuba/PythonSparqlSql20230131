from DataBaseClass import DataBase


def test():
    db = DataBase()
    db_name = 'db/data1.db'
    db.connect(db_name)

    # results = db.execute('SELECT * FROM movie')
    # results_list = []
    # for row in results:
    #     results_list.append(row)
    results_list = db.execute('SELECT * FROM movie')

    assert len(results_list) == 4
    assert results_list[1][2] == 'action film'
    assert results_list[1][3] == 'マックG'

    results = db.execute('SELECT * FROM theater')
    results_list = []
    for row in results:
        results_list.append(row)
    assert len(results_list) == 4

    db.close()
