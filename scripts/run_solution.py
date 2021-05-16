"""Script used for running code solution"""

from challenge.challenge import get_all_the_data

def run_solution():
    """Function for running the code solution"""

    results = get_all_the_data()

    print('*' * 100)
    print('*' * 38 + 'And the results are in!!' + '*' * 38)
    print(results)
    print('*' * 100)


run_solution()