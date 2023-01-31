import json


class Mapping:
    def __init__(self):
        self.mapping = None
        pass

    def load(self, file_name):
        file = open(file_name, 'r')
        self.mapping = json.load(file)
        pass
