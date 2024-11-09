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

#test destinations function

@pytest.fixture
def destinations():
    return [
        {
            "Destination": "Paris",
            "Temperature Preference": "Warm",
            "Vacation Purpose": ["Cultural & Historic", "City trip"],
            "Best Season": ["Spring", "Summer"],
            "Duration": ["Weekend", "Week"],
            "Group Suitability": ["Alone", "Friends", "My Partner"],
            "Avg Cost/Person": 800,
            "Description": "Experience the culture, art, and food of Paris.",
            "Travel Options": {"Train": {"Cost": 200, "Time": "3h"}, "Flight": {"Cost": 300, "Time": "1h"}}
        },
        {
            "Destination": "Swiss Alps",
            "Temperature Preference": "Cold",
            "Vacation Purpose": ["Skiing and Snowboarding", "Nature"],
            "Best Season": ["Winter"],
            "Duration": ["Week", "2 weeks"],
            "Group Suitability": ["Friends", "My family"],
            "Avg Cost/Person": 1200,
            "Description": "Enjoy skiing and snowboarding in the beautiful Alps.",
            "Travel Options": {"Flight": {"Cost": 400, "Time": "1.5h"}}
        },
        
    ]

#test filter destinations function
from maincode import filter_destinations

def test_filter_destinations(destinations):
    result = filter_destinations(
        temp_preference="Warm",
        vacation_purpose="City trip",
        best_season="Summer",
        duration="Week",
        group_type="Friends",
        budget=1000
    )
    assert len(result) == 1
    assert result[0]["Destination"] == "Paris"

    # Test for no match
    result = filter_destinations(
        temp_preference="Cold",
        vacation_purpose="Beach",
        best_season="Summer",
        duration="Weekend",
        group_type="Alone",
        budget=500
    )
    assert result == []

# testing display functions
from maincode import (
    display_temp_preference,
    display_vacation_purpose,
    display_best_season,
    display_duration,
    display_group_type,
    display_budget,
    display_user_choices,
    display_destination
)

def test_display_temp_preference(capsys):
    display_temp_preference("Warm")
    captured = capsys.readouterr()
    assert "You prefer a warm destination." in captured.out

def test_display_vacation_purpose(capsys):
    display_vacation_purpose("Beach")
    captured = capsys.readouterr()
    assert "Your vacation purpose is: Beach." in captured.out

def test_display_user_choices(capsys):
    display_user_choices("Warm", "Beach", "Summer", "Week", "Friends", 1000)
    captured = capsys.readouterr()
    assert "You prefer a warm destination." in captured.out
    assert "Your vacation purpose is: Beach." in captured.out
    assert "Your chosen season for travel is: Summer." in captured.out
    assert "You plan to go for: Week." in captured.out
    assert "You are traveling with: Friends." in captured.out
    assert "Your maximum budget per person is: $1000." in captured.out

def test_display_destination_no_results(capsys):
    display_destination([])
    captured = capsys.readouterr()
    assert "No destinations found that match your criteria." in captured.out

def test_display_destination_with_results(capsys, destinations):
    display_destination(destinations)
    captured = capsys.readouterr()
    assert "Here are some vacation destinations that match your criteria:" in captured.out
    assert "Destination: Paris" in captured.out
    assert "Destination: Swiss Alps" in captured.out

#test final function, the vacation planner
from maincode import vacation_planner

def test_vacation_planner(monkeypatch, capsys, destinations):
    inputs = iter(["Warm", "Beach", "Summer", "Week", "Friends", "1000"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    # Run the planner
    vacation_planner()

    # Capture output
    captured = capsys.readouterr()
    assert "Let's plan your European vacation from Amsterdam!" in captured.out
    assert "You prefer a warm destination." in captured.out
    assert "Your vacation purpose is: Beach." in captured.out
    assert "Your chosen season for travel is: Summer." in captured.out
    assert "You plan to go for: Week." in captured.out
    assert "You are traveling with: Friends." in captured.out
    assert "Your maximum budget per person is: $1000." in captured.out
    assert "Here are some vacation destinations that match your criteria:" in captured.out
    assert "Destination: Paris" in captured.out
