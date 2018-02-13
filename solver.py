import re


class Solver:

    def __init__(self, query):
        self.query = re.sub(r'[^a-zA-Z]+', '', query)
        if self.is_query_valid():
            self.char_array = list(self.query)
        else:
            self.char_array = None

    def is_query_valid(self):
        return self.query and len(self.query) > 1

    def make_alpha_from_array(self, array):
        array.sort()
        return "".join(array).lower()

    def generate_all_possible_alphas(self, recursive_run=False, characters=[]):
        char_array = list(self.char_array)
        if recursive_run:
            char_array = list(characters)
        char_array.sort()
        first_alpha = self.make_alpha_from_array(char_array)
        alphas = {first_alpha: first_alpha}
        count_char = len(char_array)
        for char, i in char_array:
            alphas = alphas + self.generate_alphas(char_array, i)
        if not recursive_run:
            next_iteration_char_array = list(char_array)
            while 0 in next_iteration_char_array and len(next_iteration_char_array) > 1:
                del next_iteration_char_array[0]
                

