# NSS-Code-Challenge(Python): Poke API



###### This is a code challenge that leverages the Poke API to get data about Pikachu and return a full object of enriched data.

## The Objective

The Poke API returns relational data from other endpoints as api urls like so:
```
{
    "abilities": [
        {
            "ability": {
                "name": "static",
                "url": "https://pokeapi.co/api/v2/ability/9/"
            },
            "is_hidden": false,
            "slot": 1
        },
        {
            "ability": {
                "name": "lightning-rod",
                "url": "https://pokeapi.co/api/v2/ability/31/"
            },
            "is_hidden": true,
            "slot": 3
        }
    ],
    "base_experience": 112,
    "forms": [
        {
            "name": "pikachu",
            "url": "https://pokeapi.co/api/v2/pokemon-form/25/"
        }
    ],
}
```

We want to return an object that tells us about Pikachus forms, like this:
```
{
    "abilities": [
        {
            "ability": {
                "name": "static",
                "url": "https://pokeapi.co/api/v2/ability/9/"
            },
            "is_hidden": false,
            "slot": 1
        },
        {
            "ability": {
                "name": "lightning-rod",
                "url": "https://pokeapi.co/api/v2/ability/31/"
            },
            "is_hidden": true,
            "slot": 3
        }
    ],
    "base_experience": 112,
    "form": {
        "form_name": "",
        "form_names": [],
        "form_order": 1,
        "id": 25,
        "is_battle_only": false,
        "is_default": true,
        "is_mega": false,
        "name": "pikachu",
        "names": [],
        "order": 36,
        "pokemon": {
            "name": "pikachu",
            "url": "https://pokeapi.co/api/v2/pokemon/25/"
        },
        "sprites": {
            "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/25.png",
            "back_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/female/25.png",
            "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/25.png",
            "back_shiny_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/female/25.png",
            "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
            "front_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/female/25.png",
            "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/25.png",
            "front_shiny_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/female/25.png"
        },
        "types": [
            {
                "slot": 1,
                "type": {
                    "name": "electric",
                    "url": "https://pokeapi.co/api/v2/type/13/"
                }
            }
        ],
        "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
        }
    }
}
```

## Project Setup
To make things easier, this project makes use of a `Makefile` to wrap all of the commands you might need into easier commands. To setup the environment type this into your terminal:
`make setup_project && source nss-code-challenge/bin/activate`

If you are using windows, then type:
`python -m venv nss-code-challenge && source nss-code-challenge/bin/activate && pip install -r requirements.txt && pip install -e .`

## To Run The Code
In order to be able to test the solution, you can run:
`make run_solution`
or on windows:
`python3 scripts/run_solution.py`

This will run the solution and print the return from `get_all_the_data` in `challenge/challenge.py`
