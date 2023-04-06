# test_friend.py

# assert expression
## if true nothing happens
## if false raises AssertionError

# create virtual environment and activate
# pip install pytest
# pip install pytest-cov

# run tests with python -m pytest -s
# compare -s and -v when running the tests
# run coverage tests with python -m pytest --cov

import pytest
from datetime import date
from friend import *


### unit tests ###

def test_calculate_current_age():
    """
    GIVEN a user enters the year they were born
    WHEN that year is passed to this function
    THEN the user's age is accurately calculated
    """
    birth_year = 2000
    today = date.today()
    expected_age = today.year - birth_year
    print('/r')
    print(" -- calculate_current_age unit test")
    assert (
        calculate_current_age(birth_year) == expected_age
    )  # DYNAMIC: calculates the current year


def test_calculate_future_age():
    """
    GIVEN a user's current age
    WHEN that age is passed to this function
    THEN the user's age is accurately calculated to be 10 years into the future
    """
   
    user_age = 20
    print('/r')
    print(" -- calculate_future_age unit test")
    assert (
        calculate_future_age(user_age) == 30
    )  

def test_calculate_past_age():
    """
    GIVEN a user's current age
    WHEN that age is passed to this function
    THEN the user's age is accurately calculated to be 10 years in the past
    """
   
    current_age = 20
    expected_age = current_age - 10
    print('/r')
    print(" -- calculate_past_age unit test")
    assert (
        calculate_past_age(current_age) == expected_age
    )  

def test_add_friend():
    first_name = "john"
    last_name = "doe"
    current_age = 30
    future_age = 40
    past_age = 20
    add_friend(first_name, last_name, current_age, future_age, past_age)
    print('/r')
    print(" -- add_friend unit test")
    assert friend_list[-1]["name"] == "john doe"
    assert friend_list[-1]["age"] == 30
    assert friend_list[-1]["future"] == 40
    assert friend_list[-1]["past"] == 20

    def test_collectUserDetails(monkeypatch):
        input_values = ["john", "doe", "2000"]
        def mock_input(s):
            return(first_name, last_name, birth_year)
                   
    def main():
        print(friend_list)
        first_name, last_name, brith_year = collectUserDetails()
        current_age = calculate_current_age(birth_year)
        future_age= calculate_future_age(current_age)
        past_age = calculate_past_age(current_age)
        add_friend(first_name, last_name, current_age, future_age, past_age)
        print(friend_list)

    def test_main(monkeypatch, capsys):
        input_values = ["Jane", "Doe", "1995"]
        def mock_input(s): 
            return input_values.pop(0)
        monkeypatch.setattr("builtins.input", mock_input)
        main() 
        captured = capsys.readouterr()
        assert "Jane Doe" in captured.out
        assert friend_list [-1]["name"] == "Jane Doe"
        assert friend_list [-1]["age"] == 26
        assert friend_list [-1]["future"] == 36
        assert friend_list [-1]["past"] == 16
    




