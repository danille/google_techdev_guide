def find(char, string):
    for i in range(len(string)):
        if char == string[i]:
            return i
    return -1


def is_substring(letters: str, string: str):
    i = 0
    positions = []
    while len(letters) != 0 and i != len(string):
        char = string[i]
        char_index = find(char, letters)
        if char_index == -1:
            return False
        else:
            letters = letters[char_index:]
            positions.append(char_index)
        i += 1
    return len(positions) == len(string)


def find_longest_word_in_string(letters, words):
    """
    The Challenge
    Given a string S and a set of words D, find the longest word in D that is a subsequence of S.

    Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.

    Note: D can appear in any format (list, hash table, prefix tree, etc.

    For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"

    The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
    The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.
    The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.

    :param letters: string which should be analyzed for subwords
    :param words: list of words against which analysis should be conduct
    :return: the longest subword of string from words
    """
    # Define some useful values
    # First iterating through the list of words
    for word in sorted(words, key=lambda x: len(x), reverse=True):
        if is_substring(letters, word):
            return word
    return None


S = "abppplee"
D = {"able", "ale", "apple", "bale", "kangaroo"}
print(find_longest_word_in_string(S, D))
assert find_longest_word_in_string(S, D) == 'apple'


def string_splosion(string):
    """
    Given a non-empty string like "Code" return a string like "CCoCodCode".
    :param string: non-empty string
    :return: resulting string
    """
    result = ''
    for i in range(len(string) + 1):
        result += string[:i]
    return result
