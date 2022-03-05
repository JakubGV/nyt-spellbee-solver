import argparse

def parse_args() -> tuple:
  parser = argparse.ArgumentParser(description='Insert a word into the specified word list.')
  parser.add_argument('words', nargs='*', help='The words to insert.')

  args = parser.parse_args()

  return tuple(args.words)

def insert_word(word_list: list, word_to_insert: str) -> bool:
  index_to_insert = 0
  for i, word in enumerate(word_list):
    if word_to_insert < word:
      index_to_insert = i
      break
    elif word_to_insert == word:
      return False
    
    if i == len(word_list) - 1: # take care of inserting at the end of the list
      index_to_insert = len(word_list)

  word_list.insert(index_to_insert, word_to_insert)
  return True
  
def insert_words(word_list: list, words_to_insert: tuple) -> str:
  success = []
  fail = []
  
  for word in words_to_insert:
    if insert_word(word_list, word):
      success.append(word)
    else:
      fail.append(word)
  
  print(f"Failed to insert: {' '.join(fail)}")
  print(f"Successfully inserted: {' '.join(success)}")
  
  contents = '\n'.join(word_list)

  return contents

def main():
  words_to_insert = parse_args()
  
  file = 'word_list.txt'

  with open(file, 'r') as word_file:
    word_list = [word.strip() for word in word_file]

  contents = insert_words(word_list, words_to_insert)
    
  with open(file, 'w') as word_file:
    word_file.write(contents)

if __name__ == '__main__':
  main()