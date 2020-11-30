"""Functions for checking a palindrome"""
from typing import List, Tuple

def check_palindrome_examples(word_list: List) -> Tuple:
    """Takes in a list of words that could or could not be a palindrome
       and outputs a list of palindromes and a list of non-palindromes

    :param word_list: List of words that could or could not be a palindrome
    :type word_list: List
    :returns: Tuple of palindromes and Non-palindromes
    :rtype: Tuple
    """

    palindromes = []
    non_palendroms = []

    # Solution code here


    return palindromes, non_palendroms


def run_tests() -> None:
    """function for running palindrome tests"""

    # Out list of words to check for palindromes

    word_list = [
        'Madam',
        'rotator',
        'stats',
        'my Gym',
        'top spot',
        'turkey',
        'sports',
        'javascript'
    ]

    palindromes, non_palindromes = check_palindrome_examples(word_list)

    # Print out our answers to check them

    print(f'The following words are palindromes: {", ".join(palindromes)}')
    print(f'The following words are not palindromes: {", ".join(non_palindromes)}')

run_tests()