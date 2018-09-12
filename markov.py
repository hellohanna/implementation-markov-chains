"""Generate Markov text from text files."""

from random import choice
import sys

def open_and_read_file(file_path1,file_path2 =None):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    f1 = open(file_path1)
    file_string1 = f1.read()
    f1.close()

    if file_path2 != None:
        f2 = open(file_path2)
        file_string2 = f2.read()
        f2.close
        return file_string1 + ' ' + file_string2
    else:
        return file_string1



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


def make_text(chains, n, max_length):
    """Return text from chains."""

    words = []

    while True:
        next_key = choice(list(chains.keys()))
        if next_key[0].istitle():
            break

    for i in range(n):
        words.append(next_key[i])

    while next_key in chains and len(words) < max_length:
        random_value = choice(chains[next_key])
        words.append(random_value)
        next_key_lst = list(next_key)[1:]
        next_key_lst.append(random_value)
        next_key = tuple(next_key_lst)

    words_copy = words[:]
    while len(words_copy) > 0:
        last_word = words_copy[len(words_copy)-1]
        last_char = last_word[len(last_word)-1] 
        if last_char in ['.','!','?']:
            break
        else:
            del words_copy[len(words_copy)-1]

    if len(words_copy) > 0:
        return " ".join(words_copy)
    elif words[len(words)-1].isalpha():
        words[len(words)-1] += "."
    else:
        words[len(words)-1] = words[len(words)-1][:-2] + '.'

    return " ".join(words)

def input_number(message, input_text, min_num = 1):
    words_list = input_text.split()
    number_of_words = len(words_list)
    while True:
        user_number = input(message)
        if user_number.isdigit() and user_number != '0':
            n = int(user_number)
            if n < number_of_words and n >= min_num:
                return n
        print("Incorrect input. Try number between {} and {}.".format(min_num, number_of_words-1))


if len(sys.argv) == 1:
    input_path = "green-eggs.txt"
    input_text = open_and_read_file(input_path)
elif len(sys.argv) == 2:
    input_path = str(sys.argv[1])
    input_text = open_and_read_file(input_path)
elif len(sys.argv) == 3:
    input_path1 = str(sys.argv[1])
    input_path2 = str(sys.argv[2])
    input_text = open_and_read_file(input_path1,input_path2)


n = input_number("Enter size of n-gram: ", input_text)
max_length = input_number("Enter max limit for markov chain: ",input_text, n)

# Get a Markov chain
chains = make_chains(input_text, n)

# Produce random text
random_text = make_text(chains, n, max_length)

print(random_text)
