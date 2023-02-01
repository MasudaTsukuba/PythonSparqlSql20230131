import json


class Mapping:
    def __init__(self, file_name):
        self.mappings = None
        self.load(file_name)
        pass

    def load(self, file_name):
        file = open(file_name, 'r')
        self.mappings = json.load(file)
        pass
