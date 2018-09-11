"""Generate Markov text from text files."""

from random import choice
import sys

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    f = open(file_path)
    file_string = f.read()
    f.close()

    return file_string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words_list = text_string.split()
    for i in range(len(words_list) - 2):
        key_tuple = (words_list[i], words_list[i+1])

       
        if key_tuple not in chains:
            chains[key_tuple] = []
        chains[key_tuple].append(words_list[i+2])


    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    next_key = choice(list(chains.keys()))

    words.append(next_key[0])
    words.append(next_key[1])

    while next_key in chains:
        random_value = choice(chains[next_key])
        words.append(random_value)
        next_key = (next_key[1],random_value)

    

    return " ".join(words)


if len(sys.argv) == 1:
    input_path = "green-eggs.txt"
else:
    input_path = str(sys.argv[1])

#input_path = "gettysburg.txt"
# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
