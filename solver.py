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
        """
        :param array:
        :return:
        """
        array.sort()
        return "".join(array).lower()

    def generate_all_possible_alphas(self, recursive_run=False, characters=[]):
        """
        :param recursive_run:
        :param characters:
        :return:
        """
        char_array = list(self.char_array)
        if recursive_run:
            char_array = list(characters)
        char_array.sort()
        first_alpha = self.make_alpha_from_array(char_array)
        alphas = {first_alpha: first_alpha}
        count_char = len(char_array)
        for i, char in enumerate(char_array):
            alphas = alphas.update(self.generate_alphas(char_array, i))
        if not recursive_run:
            next_iteration_char_array = list(char_array)
            while 0 in next_iteration_char_array and len(next_iteration_char_array) > 1:
                del next_iteration_char_array[0]
                next_iteration_char_array = list(next_iteration_char_array)
                alphas = alphas.update(self.generate_all_possible_alphas(True, next_iteration_char_array))
        return alphas

    def generate_alphas(self, char_array, pos_from=0, delete=1):
        """
        This methods generate all possible alphas for given array of characters
        :param char_array:
        :param pos_from:
        :param delete:
        :return:
        """
        count_char = len(char_array)
        alphas = self.generate_alpha_loop(char_array, pos_from, delete, True)
        alphas = alphas.update(self.generate_alpha_loop(char_array, pos_from, delete, False))
        while (count_char - delete) > 0:
            delete += 1
            alphas = alphas.update(self.generate_alpha_loop(char_array, pos_from, delete, True))
            alphas = alphas.update(self.generate_alpha_loop(char_array, pos_from, delete, False))
        return alphas

    def generate_alpha_loop(self, char_array, pos_from=0, delete=1, delete_double=True):
        """
        :param char_array:
        :param pos_from:
        :param delete:
        :param delete_double:
        :return:
        """
        alphas = {}
        count_char = len(char_array)
        last_index = count_char - 1
        if pos_from in char_array and delete_double:
            del char_array[int(pos_from)]
        for offset in range(0, count_char):
            char_array_copy = list(char_array)
            for u in range(0, delete):
                del_index = pos_from + u + offset
                if del_index > last_index:
                    del_index = del_index - last_index
                if del_index in char_array_copy:
                    del char_array_copy[del_index]
                    if len(char_array_copy) > 1:
                        alpha = "".join(char_array_copy).lower()
                        alphas[alpha] = alpha
        return alphas

