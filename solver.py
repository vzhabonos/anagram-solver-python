import re


class Solver:

    def __init__(self, query):
        self.query = re.search(r'[a-zA-Z]+', query);
        print(self.query)
