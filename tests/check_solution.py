from challenge.challenge import get_all_the_data


def test_check_solution(correct_luke_object):

    result = get_all_the_data()

    assert result == correct_luke_object

