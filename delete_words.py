import argparse
from re import U

def parse_args() -> tuple:
    parser = argparse.ArgumentParser(description='Delete words from the word list.')
    parser.add_argument('words', nargs='*', help='The words to delete.')

    args = parser.parse_args()

    if len(args.words) < 1:
        raise ValueError('No words provided to delete')

    return tuple(args.words)

def delete_indices(word_list: list, indices_to_delete: set) -> None:
    """
    delete_indices removes the indices in `indices_to_delete` from the `word_list`.

    :param word_list: the word list to delete from
    :param indices_to_delete: a set of integer indices to delete from the word_list
    """
    num_deleted = 0
    for index in indices_to_delete:
        del word_list[index - num_deleted]
        num_deleted += 1

def find_word(word_list: list, word: str) -> int:
    """
    find_word attempts to find `word` in word_list, returning the index of the word if found.

    :param word_list: the word_list to search in
    :param word: the word to find in the `word_list`
    :return: the index of the word, -1 if not found
    """
    for i, word_list_word in enumerate(word_list):
        if word == word_list_word:
            return i

    return -1

def delete_words(word_list: list, words_to_delete: tuple) -> None:
    """
    insert_words tries to delete a tuple of words from the word list and prints which were successful and which weren't.

    :param word_list: the word list to insert into
    :param words_to_delete: the words to attempt to delete from the word list
    """
    indices_to_delete = set()
    success = []
    fail = []

    for word in words_to_delete:
        index = find_word(word_list, word)
        if index != -1:
            indices_to_delete.add(index)
            success.append(word)
        else:
            fail.append(word)

    delete_indices(word_list, indices_to_delete)

    if len(fail) > 0:
        print(f"Failed to delete: {' '.join(fail)}")
    if len(success) > 0:
        print(f"Successfully deleted: {' '.join(success)}")

def main():
    words_to_delete = parse_args()

    file = 'word_list.txt'

    with open(file, 'r') as word_file:
        word_list = [word.strip() for word in word_file]

    delete_words(word_list, words_to_delete)

    contents = '\n'.join(word_list)

    with open(file, 'w') as word_file:
        word_file.write(contents)

if __name__ == '__main__':
    main()