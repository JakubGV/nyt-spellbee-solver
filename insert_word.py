import argparse

def parse_args() -> str:
  parser = argparse.ArgumentParser(description='Insert a word into the specified word list.')
  parser.add_argument('word', help='The word to insert.')

  args = parser.parse_args()

  return args.word.lower()

def insert_word(word_list: list, word_to_insert: str) -> str:
  index_to_insert = 0
  for i, word in enumerate(word_list):
    if word_to_insert < word:
      index_to_insert = i
      break
    elif word_to_insert == word:
      raise RuntimeError("Word to insert already exists in word list.")
    
    if i == len(word_list) - 1: # take care of inserting at the end of the list
      index_to_insert = len(word_list)

  word_list.insert(index_to_insert, word_to_insert)
  contents = '\n'.join(word_list)

  return contents

def main():
  word_to_insert = parse_args()
  file = 'word_list.txt'

  with open(file, 'r') as word_file:
    word_list = [word.strip() for word in word_file]

  contents = insert_word(word_list, word_to_insert)
    
  with open(file, 'w') as word_file:
    word_file.write(contents)

if __name__ == '__main__':
  main()