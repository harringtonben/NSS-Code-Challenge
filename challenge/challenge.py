"""Functions for checking a palindrome"""
from typing import List, Tuple

def check_palindrome_examples(word_list: List) -> Tuple:
    """Takes in a list of words that could or could not be a palindrome
       and outputs a list of palindromes and a list of non-palendromes

    :param word_list: List of words that could or could not be a palendrome
    :type word_list: List
    :returns: Tuple of Palendromes and Non-palendromes
    :rtype: Tuple
    """

    palendromes = []
    non_palendroms = []

    # Solution code here


    return palendromes, non_palendroms


def run_tests() -> None:
    """function for running palendrome tests"""

    # Out list of words to check for palendromes

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

    palendromes, non_palendromes = check_palindrome_examples(word_list)

    # Print out our answers to check them

    print(f'The following words are palendromes: {"".join(palendromes)}')
    print(f'The following words are not palendromes: {"".join(non_palendromes)}')

run_tests()