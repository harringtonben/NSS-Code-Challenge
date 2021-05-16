"""API functions for dealing with the star wars API"""
from typing import Dict
import requests


BASE_URL = 'https://swapi.dev/api'


def get_luke() -> Dict:
    """Function that will get data on Luke Skywalker from the atar wars API

    :returns: A dictionary of data about Luke Skywalker
    :rtype: Dict
    """

    url = f'{BASE_URL}/people/1'

    return requests.get(url).json()