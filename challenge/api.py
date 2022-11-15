"""API functions for dealing with the star wars API"""
from typing import Dict
import requests


BASE_URL = 'https://pokeapi.co/api/v2'


def get_pikacho() -> Dict:
    """Function that will get data on pikachu from the poke api

    :returns: A dictionary of data about Pikachu
    :rtype: Dict
    """

    url = f'{BASE_URL}/pokemon/pikachu'

    return_data = requests.get(url).json()

    return_keys = ['abilities', 'base_experience', 'forms', 'height', 'held_items']
    return_data = {key: value for key, value in return_data.items() if key in return_keys}
    return return_data