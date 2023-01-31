class Uri:
    def __init__(self):
        self.dictionary = {'Q191543': 'ターミネーター4'}
        self.inverse_dictionary = None
        pass

    def invert_dictionary(self):
        self.inverse_dictionary = {}
        for item in self.dictionary:
            try:
                key = self.dictionary[item]
                self.inverse_dictionary[key] = item
            except KeyError:
                pass

    def uri(self, input_string):
        pass

    def iru(self, input_uri):
        pass
