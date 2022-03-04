import argparse
from itertools import product

def parse_args() -> dict:
  parser = argparse.ArgumentParser(description='Solve the NYT spelling bee')
  parser.add_argument('letters', help='The 7 letters of the spelling bee with no spaces. (First is necessary letter)')
  parser.add_argument('max_length', type=int, help='Max length of word to find. (4 <= length <= 20)')

  args = parser.parse_args()

  if len(args.letters) != 7:
    raise ValueError('Only 7 letters may be entered')
  if not 4 <= args.max_length <= 20:
    raise ValueError('Lengh must be between 4 and 20 inclusive')
  
  letters = []
  for letter in args.letters:
    letters.append(letter)

  return {
    'letters': letters,
    'max_length': args.max_length
  }

def is_word(word_list, word: str) -> bool:
  return word in word_list

def find_words(word_list, letters: tuple, length: int) -> list:
  needed_letter = letters[0]
  word = needed_letter + 3 * letters[1]
  found_words = []

  possibilities = map(''.join, product(letters, repeat=length))
  for word in possibilities:
    if needed_letter in word and is_word(word_list, word):
      found_words.append(word)

  return found_words

def find_all_words(word_list, letters: tuple, max_length: int) -> dict:
  words_by_length = {}
  for length in range(4, max_length + 1):
    key = length
    val = find_words(word_list, letters, length)
    words_by_length[key] = val

  return words_by_length

def print_words(words_by_length: dict) -> None:
  for length, words in words_by_length.items():
    words.sort()
    joined_words = ' '.join(words)
    print(f'Words of length {length}: {joined_words}')

def main():
  args_dict = parse_args()

  with open('word_list.txt') as word_file:
    word_list = set(word.strip() for word in word_file)

  words_by_length = find_all_words(word_list, args_dict['letters'], args_dict['max_length'])

  print_words(words_by_length)

if __name__ == '__main__':
  main()