# NSS-Code-Challenge(Python): SWAPI API



###### This is a code challenge that leverages the Star Wars API to get data about Luke Skywalker and return a full object of enriched data.

## The Objective

The Star wars API returns relational data from other endpoints as api urls like so:
```
{
    'name': 'Luke Skywalker',
    'height': '172',
    'mass': '77',
    'hair_color': 'blond',
    'skin_color': 'fair',
    'eye_color': 'blue',
    'birth_year': '19BBY',
    'gender': 'male',
    'homeworld': 'http://swapi.dev/api/planets/1/',
    'films': [
        'http://swapi.dev/api/films/1/',
        'http://swapi.dev/api/films/2/',
        'http://swapi.dev/api/films/3/',
        'http://swapi.dev/api/films/6/'
    ],
    'species': [],
    'vehicles': [
        'http://swapi.dev/api/vehicles/14/',
        'http://swapi.dev/api/vehicles/30/'
    ],
    'starships': [
        'http://swapi.dev/api/starships/12/',
        'http://swapi.dev/api/starships/22/'
    ],
    'created': '2014-12-09T13:50:51.644000Z',
    'edited': '2014-12-20T21:17:56.891000Z',
    'url': 'http://swapi.dev/api/people/1/'
}
```

In order to return an object with all of the data about Luke Skywalker, we will have to iterate over this object and get all of the data associated with luke and transform this object to replace the urls with the necessary data

## Docs For Reference
 Documentation for the star wars api can be found here: https://swapi.dev/

## Project Setup
To make things easier, this project makes use of a `Makefile` to wrap all of the commands you might need into easier commands. To setup the environment type this into your terminal:
`make setup_project`

If you are using windows, then type:
`pip install poetry && poetry install`

## To Run The Code
In order to be able to test the solution, you can run:
`make run_solution`
or on windows:
`poetry run python3 scripts/run_solution.py`

This will run the solution and print the return from `get_all_the_data` in `challenge/challenge.py`