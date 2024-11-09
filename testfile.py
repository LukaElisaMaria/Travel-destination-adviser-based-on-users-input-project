import pytest

from maincode import (
    querry_temperature_preference,
    querry_vacation_purpose,
    querry_best_season,
    querry_duration,
    querry_group_type,
    querry_budget
)

# Test for querry_temperature_preference
def test_querry_temperature_preference():
    assert querry_temperature_preference("Warm") == "Warm"
    assert querry_temperature_preference("Cold") == "Cold"
    with pytest.raises(ValueError):
        querry_temperature_preference("Hot")

# Test for querry_vacation_purpose
def test_querry_vacation_purpose():
    assert querry_vacation_purpose("Warm", "Beach") == "Beach"
    assert querry_vacation_purpose("Cold", "Skiing and Snowboarding") == "Skiing and Snowboarding"
    with pytest.raises(ValueError):
        querry_vacation_purpose("Warm", "Skiing and Snowboarding")

# Test for querry_best_season
def test_querry_best_season():
    assert querry_best_season("Summer") == "Summer"
    with pytest.raises(ValueError):
        querry_best_season("Rainy")

# Test for querry_duration
def test_querry_duration():
    assert querry_duration("Week") == "Week"
    with pytest.raises(ValueError):
        querry_duration("Year")

# Test for querry_group_type
def test_querry_group_type():
    assert querry_group_type("Friends") == "Friends"
    with pytest.raises(ValueError):
        querry_group_type("Enemies")

# Test for querry_budget
def test_querry_budget():
    assert querry_budget(1000) == 1000
    with pytest.raises(ValueError):
        querry_budget(-50)

