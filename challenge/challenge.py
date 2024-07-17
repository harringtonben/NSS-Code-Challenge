"""NSS Code Challenge"""
from challenge.api import get_pikacho


def get_all_the_data():
    """entry point for code challenge"""

    pikachu = get_pikacho()

    return pikachu