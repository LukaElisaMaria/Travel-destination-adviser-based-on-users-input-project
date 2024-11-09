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
def test_querry_temperature_preference_warm(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Warm")
    assert querry_temperature_preference() == "Warm"

def test_querry_temperature_preference_cold(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Cold")
    assert querry_temperature_preference() == "Cold"

def test_querry_temperature_preference_invalid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Hot")
    with pytest.raises(ValueError):
        querry_temperature_preference()

# Test for querry_vacation_purpose
def test_querry_vacation_purpose_warm(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Beach")
    assert querry_vacation_purpose("Warm") == "Beach"

def test_querry_vacation_purpose_cold(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Skiing and Snowboarding")
    assert querry_vacation_purpose("Cold") == "Skiing and Snowboarding"

def test_querry_vacation_purpose_invalid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Space travel")
    result = querry_vacation_purpose("Warm")
    assert result == "Space travel"  # Adjust as needed if this requires validation

# Test for querry_best_season
def test_querry_best_season(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Summer")
    assert querry_best_season() == "Summer"

# Test for querry_duration
def test_querry_duration(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Week")
    assert querry_duration() == "Week"

# Test for querry_group_type
def test_querry_group_type(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Friends")
    assert querry_group_type() == "Friends"

# Test for querry_budget
def test_querry_budget(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1000")
    assert querry_budget() == 1000
