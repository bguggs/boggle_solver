from bisect import bisect_left, bisect_right


class Board:
    def __init__(self, board_str):
        word_lst = []
        with open("words.txt", mode='r') as all_words_file:
            for line in all_words_file.readlines():
                word_lst.append(line.strip())
        self.board = self.create_board(board_str)
        word_lst.sort()
        self.dictionary = word_lst

    @staticmethod
    def create_board(board_str):
        all_rows = board_str.split(',')
        board = []
        for row in all_rows:
            board += [[c for c in row]]
        return board

    def find_words_starting_with(self, partial_word):
        pass

    def is_word(self, word):
        'Locate the leftmost value exactly equal to word'
        index = bisect_left(self.dictionary, word)
        if index != len(self.dictionary) and self.dictionary[index] == word:
            return True, index
        else:
            return False, -1

    def is_prefix(self, word_fragment):
        try:
            return self.dictionary[bisect_right(self.dictionary, word_fragment.lower())].startswith(word_fragment.lower())
        except IndexError:
            return False  # word_fragment is greater than all entries in wordlist

    def find_words(self, word_frag, full_list):
        if self.is_word(word_frag) and not word_frag in full_list:
            full_list.append(word_frag)
        if not self.is_prefix(word_frag):
            return full_list
        try:
            return

    def __repr__(self):
        output_str = ""
        for row in self.board:
            for char in row:
                output_str += char + " "
            output_str = output_str[:-1] + "\n"
        return output_str

my_board = Board("WTKB,OEAY,CRMT,SAEH")
print(my_board.is_word("xenon"))
