import argparse
import time
from spelling_bee_solver import SpellingBeeSolver

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

def main():
  start = time.time()
  letters = parse_args()

  solver = SpellingBeeSolver('word_list.txt')
  found_words = solver.solve(letters)
  
  print(f'Number of words found: {len(found_words)}')
  solver.pprint_words(found_words)

  pangrams = solver.find_pangrams(found_words, letters)
  print(f"Pangrams: {' '.join(pangrams)}")

  end = time.time()
  print('Execution took:'.ljust(15), f'{end-start:.4f}s')
  
if __name__ == '__main__':
  main()