class SpellingBeeSolver:
    """
    A class to represent a spelling bee solver.

    ...

    Attributes
    ----------
    word_list_file : str
        filename of the word list to use
    
    Methods
    -------
    solve(letters : tuple) -> tuple:
        Finds all the words using the given letters and word list.
    find_pangrams(found_words : tuple, letters : tuple) -> tuple:
        Finds the pangrams in the found words using the given letters.
    pprint_words(found_words: tuple):
        Prints the found words by length and alphabetical order.
    """
    def __init__(self, word_list_file: str) -> None:
        """
        Initializes the word list for the spelling bee solver.

        :param word_list_file: the filename of the word list to use
        """
        with open(word_list_file, 'r') as word_file:
            self._word_list = tuple(word.strip() for word in word_file)

    def solve(self, letters: tuple) -> tuple:
        """
        solve finds all the words from `self._word_list` that are only made up of the specified letters.

        :param letters: the letters of the day's spelling bee (first letter is the must include letter)
        :return: a tuple of words matching the specified letters
        """
        found_words = []
  
        for word in self._word_list:
            valid_word = True
            if len(word) < 4 or letters[0] not in word:
                continue
            else:
                for letter in word:
                    if letter not in letters:
                        valid_word = False
                        break
            
            if valid_word:
                found_words.append(word)

        return tuple(found_words)

    def find_pangrams(self, found_words: tuple, letters: tuple) -> tuple:
        """
        find_pangrams returns the pangrams in `found_words` with the specified `letters`. 

        :param found_words: the words found by the spelling bee solver
        :param letters: the letters of the day's spelling bee
        :return: a tuple of the pangrams
        """
        pangrams = []

        for word in found_words:
            letters_needed = set(letters)
            for letter in word:
                letters_needed.discard(letter)

            if len(letters_needed) == 0:
                pangrams.append(word)

        return tuple(pangrams)

    def _organize_words_by_length(self, found_words: tuple) -> dict:
        """
        _organize_words_by_length organizes a given tuple of found words into a dictionary keyed by length.

        :param found_words: the tuple of words to organize
        :return: a dict with keys of word length paired to a value of a list of words at that length
        """
        words_by_length = {}
        
        for word in found_words:
            length = len(word)
            if length in words_by_length:
                words_by_length[length].append(word)
            else:
                words_by_length[length] = [word]
        
        return words_by_length 

    def pprint_words(self, found_words: tuple) -> None:
        """
        pprint_words prints the words found by length first, and alphabetical order second.

        :param found_words: the list of words found by the solver
        """
        words_by_length = self._organize_words_by_length(found_words)
        
        for length in sorted(words_by_length):
            words = words_by_length[length]
            words.sort()
            joined_words = ' '.join(words)
            print(f'Words of length {length}:'.ljust(19), f'{joined_words}')