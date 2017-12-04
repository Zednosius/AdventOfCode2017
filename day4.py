from get_data import get_data
import functools
import itertools as it


@functools.lru_cache()
def anagramize(word):
    """Returns a Mapping of each letter to the amount of times it occurs in word. 
    Two words are anagrams if same amount of letters. """
    anagram = {}
    for letter in word:
        anagram[letter] = 1 + anagram.get(letter, 0)
    return anagram

def are_anagrams(word1, word2):
    "True if the words are anagrams"
    return anagramize(word1) == anagramize(word2)


def contains_anagram(phrase):
    "True if the phrase contains an anagram"
    word_word_list = it.permutations(phrase, 2)
    for word_word in word_word_list:
        word1, word2 = word_word
        if are_anagrams(word1, word2):
            return True
    return False


def contains_duplicate(phrase):
    "True if there are two words that are the same."
    wordset = set()
    for word in phrase:
        if word in wordset:
            return True
    return False

def valid_passphrase_task2(phrase):
    "True if phrase is valid for task 2"
    return not (contains_duplicate(phrase) or contains_anagram(phrase))


def valid_passphrase_task1(phrase):
    "True if phrase is valid for task 1"
    return not contains_duplicate(phrase)


def doTask2(data):
    valid_phrases = 0
    for phrase in data:
        valid_phrases += 1 if valid_passphrase_task2(phrase) else 0
    return valid

def count_valid(data, valid_func):
    valid_phrases = 0
    for phrase in data:
        valid_phrases += 1 if valid_func(phrase) else 0
    return valid_phrases

if __name__ == '__main__':
    data = get_data(4)
    print("Task1 Valid Phrases: ", count_valid(data, valid_passphrase_task1))
    print("Task2 Valid Phrases: ", count_valid(data, valid_passphrase_task2))
   
