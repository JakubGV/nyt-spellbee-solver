import argparse
import time

def parse_args() -> tuple:
  parser = argparse.ArgumentParser(description='Solve the NYT spelling bee.')
  parser.add_argument('letters', help='The 7 letters of the spelling bee with no spaces. (First must be the necessary letter)')

  args = parser.parse_args()

  if len(args.letters) != 7:
    raise ValueError('Only 7 letters may be entered')
  
  letters = []
  for letter in args.letters:
    letters.append(letter)

  return tuple(letters)

def find_all_words(word_list: tuple, letters: tuple) -> tuple:
  """
  find_all_words finds all the words from the word_list that are only made up of the specified letters.

  :param word_list: the words that make up the list of words to search in
  :param letters: the letters on which to find words from
  :return: a tuple of words are only made up of the specified letters
  """
  found_words = []
  
  for word in word_list:
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

def organize_words_by_length(found_words: tuple) -> dict:
  """
  organize_words_by_length organizes the found words into a dictionary by length.

  :param found_words: the tuple of words to organize
  :return: a dict with key value pairs of a length to a list of words at that length
  """
  words_by_length = {}
  
  for word in found_words:
    length = len(word)
    if length in words_by_length:
      words_by_length[length].append(word)
    else:
      words_by_length[length] = [word]
  
  return words_by_length

def print_words(words_by_length: dict) -> None:
  """
  print_words prints the words found by length first and by alphabetical order second.

  :param words_by_length: a dict with key value pairs of a length to a list of words at that length
  """
  for length in sorted(words_by_length):
    words = words_by_length[length]
    words.sort()
    joined_words = ' '.join(words)
    print(f'Words of length {length}:'.ljust(19), f'{joined_words}')

def count_words(words_by_length: dict) -> int:
  """
  count_words counts the number of words in the words by length dict.

  :param words_by_length: a dict with key value pairs of a length to a list of words at that length
  :return: number of words
  """
  count = 0
  for _, words in words_by_length.items():
    count += len(words)

  return count

def main():
  start = time.time()
  
  letters = parse_args()

  with open('word_list.txt', 'r') as word_file:
    word_list = tuple(word.strip() for word in word_file)

  found_words = find_all_words(word_list, letters)
  
  words_by_length = organize_words_by_length(found_words)

  print_words(words_by_length)

  end = time.time()
  print('Execution took:'.ljust(15), f'{end-start:.4f}s')
  
  count = count_words(words_by_length)
  print(f'Number of words found: {count}')

if __name__ == '__main__':
  main()