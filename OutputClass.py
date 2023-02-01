import csv


class Output:
    def __init__(self, results, headers, trans_uri_list):
        for index, item in enumerate(headers):
            for trans_uri in trans_uri_list:
                if (item == trans_uri[0]) & (trans_uri[1] != 'plain'):
                    with open('URI/' + trans_uri[1] + '.csv') as g:
                        reader = csv.reader(g)
                        for row in reader:
                            for result in results:
                                if result[index] == row[0]:
                                    result[index] = row[1]
        with open('result/output.csv', 'w') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(headers)
            writer.writerows(results)

        pass
