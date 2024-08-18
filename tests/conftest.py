import pytest


@pytest.fixture
def correct_luke_object():
    return {
        "name": "Luke Skywalker",
        "height": "172",
        "mass": "77",
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": "19BBY",
        "gender": "male",
        "homeworld": "Tatooine",
        "films": [
            "A New Hope",
            "The Empire Strikes Back",
            "Return of the Jedi",
            "Revenge of the Sith"
        ],
        "species": [],
        "vehicles": [
            "Snowspeeder",
            "Imperial Speeder Bike"
        ],
        "starships": [
            "X-wing",
            "Imperial shuttle"
        ],
        "created": "2014-12-09T13:50:51.644000Z",
        "edited": "2014-12-20T21:17:56.891000Z",
        "url": "https://swapi.dev/api/people/1/"
    }

