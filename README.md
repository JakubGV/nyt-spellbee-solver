# nyt-spellbee-solver

## Description
nyt-spellbee-solver is a quick little script I made after I could not for the life of me find the pangram in the New York Times' [spelling bee](https://www.nytimes.com/puzzles/spelling-bee). For those of you who haven't played, please go try a round and you might perhaps better understand the rational behind this project.

All [solve.py](./solve.py) does is take the letters used in the spelling bee as an input and find all the words it can from the [word list](./word_list.txt).

At first, I generated all the possible sequences of letters and tried to match them those in the word list. Here I learned more about the differences between Python's tuples, lists, and sets, for which I decided to use a set for the fastest lookup time of whether a random sequence of letters was in the word list. Turns out, it is much faster to just go through the word list and see if the word has the necessary letters.

In the future I'd like to keep improving this project, hoping to one day match exactly the answers the NYT gives.

## Installing and Running
With no dependencies, all you need is a recent version of Python (this was built on version 3.10.0) to run the script and you are on your way. Oh, and it also needs [word_list.txt](./word_list.txt) of course.

## Using the Project
From the command line, a simple `py solve.py lpubicy` will print out all the words it finds with letters 'l', 'p', 'u', 'b', 'i', 'c', and 'y'. Keep in mind the first letter provided will be used as the 'must have' letter (e.g. 'l').

I also created a script called [insert_words.py](./insert_words.py) to support the vision of growing the word list to return better and better answers. Run the script with any number of words as the command line arguments and it will insert them, in alphabetical order, into the word list.

## Credits
The original word list I used at the very start of this program is not mine, but is in fact Mieliestronk's. A link to that original word list is [here](http://www.mieliestronk.com/wordlist.html).