import argparse
import time

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

def find_words(word_list: set, letters: tuple, length: int) -> list:
  found_words = []
  
  for word in word_list:
    valid_word = True
    if len(word) != length or letters[0] not in word:
      continue
    else:
      for letter in word:
        if letter not in letters:
          valid_word = False
          break
    
    if valid_word:
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
    print(f'Words of length {length}:'.ljust(19), f'{joined_words}')

def count_words(words_by_length: dict) -> int:
  count = 0
  for length, words in words_by_length.items():
    count += len(words)

  return count

def main():
  start = time.time()
  
  args_dict = parse_args()

  with open('word_list.txt', 'r') as word_file:
    word_list = set(word.strip() for word in word_file)

  words_by_length = find_all_words(word_list, args_dict['letters'], args_dict['max_length'])

  print_words(words_by_length)

  end = time.time()
  print('Execution took:'.ljust(15), f'{end-start:.4f}s')
  
  count = count_words(words_by_length)
  print(f'Number of words found: {count}')

if __name__ == '__main__':
  main()