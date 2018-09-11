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


def make_chains(text_string, n):
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
    for i in range(len(words_list)-n):
        key_lst = []
        for j in  range(i, i+n):
            key_lst.append(words_list[j])
        key_tuple = tuple(key_lst)

       
        if key_tuple not in chains:
            chains[key_tuple] = []
        chains[key_tuple].append(words_list[i+n])


    return chains


def make_text(chains, n):
    """Return text from chains."""

    words = []

    next_key = choice(list(chains.keys()))

    for i in range(n):
        words.append(next_key[i])

    while next_key in chains:
        random_value = choice(chains[next_key])
        words.append(random_value)
        next_key_lst = list(next_key)[1:]
        next_key_lst.append(random_value)
        next_key = tuple(next_key_lst)


    return " ".join(words)

def input_number():
    while True:
        user_number = input("Enter size of n-gram: ")
        if user_number.isdigit() and user_number != '0':
            n = int(user_number)
            return n
        else:
            print("Incorrect input. Try again.")


if len(sys.argv) == 1:
    input_path = "green-eggs.txt"
else:
    input_path = str(sys.argv[1])

#input_path = "gettysburg.txt"
# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

n = input_number()

# Get a Markov chain
chains = make_chains(input_text, n)

# Produce random text
random_text = make_text(chains, n)

print(random_text)
