"""API functions for dealing with the star wars API"""
from typing import Dict
import requests


BASE_URL = 'https://swapi.dev/api'


def get_luke_skywalker() -> Dict:
    """Function that will get data on luke skywalker from the star wars api

    :returns: A dictionary of data about Luke Skywalker
    :rtype: Dict
    """

    url = f'{BASE_URL}/people/1/'
    return_data = requests.get(url).json()

    return return_data
