"""NSS Code Challenge"""
from challenge.api import get_luke


def get_all_the_data():
    """entry point for code challenge"""

    luke = get_luke()

    return luke