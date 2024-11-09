#!/usr/bin/env python
# coding: utf-8

# In[114]:


import pandas as pd
import random
import ipywidgets as widgets
from IPython.display import display
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import tkinter as tk
from tkinter import ttk
import numpy as np


# In[115]:


#dataset of destination, shows location it's temperature, what vacation purpose the location can serve, the best season to go to
#said location, for how long the location is best to stay in, with whom to go (based on with whom people tipically go to said location),
# What the everage cost of the stay at the location is.
# when the loctions are filtered the function will show a description of the location and what to do/experiance and how the user can get
#to the location.
#destinations are: Paris, Swiss Apls, Tuscany, Lisbon, Barcelona, Monaco, Berlin, Scandinavia, Athens, Rome, Prague,
# Greek Islands, Split, Istanbul, Dublin, Vienna, Edinburgh and Copenhagen
destinations = [
    {
        "Destination": "Paris",
        "Temperature Preference": "Warm",
        "Vacation Purpose": ["City trip", "Cultural & Historic"],
        "Best Season": ["Spring", "Summer", "Autumn"],
        "Duration": ["Weekend", "Week", "10 days"],
        "Group Suitability": ["Alone", "My Partner", "Friends", "Family", "Colleagues"],
        "Avg Cost/Person": 1500,
        "Description": "Rich cultural experiences, iconic landmarks, and excellent cuisine.",
        "Travel Options": {
            "Flying": {"Cost": 150, "Time": "1h 20m"},
            "Train": {"Cost": 90, "Time": "3h 20m"},
            "Driving": {"Cost": 60, "Time": "5h 30m"}
        }
    },
    {
        "Destination": "Swiss Alps",
        "Temperature Preference": "Cold",
        "Vacation Purpose": ["Skiing", "Nature", "Active"],
        "Best Season": ["Winter"],
        "Duration": ["Week", "10 days", "2 weeks"],
        "Group Suitability": ["Friends", "Family", "Siblings"],
        "Avg Cost/Person": 1800,
        "Description": "Stunning alpine scenery, skiing, and outdoor adventures.",
        "Travel Options": {
            "Flying": {"Cost": 200, "Time": "1h 45m"},
            "Train": {"Cost": 120, "Time": "8h 15m"},
            "Driving": {"Cost": 150, "Time": "9h 45m"}
        }
    },
    {
        "Destination": "Tuscany",
        "Temperature Preference": "Warm",
        "Vacation Purpose": ["Cultural & Historic", "Nature", "Active"],
        "Best Season": ["Spring", "Autumn"],
        "Duration": ["Week", "10 days", "2 weeks"],
        "Group Suitability": ["My Partner", "Friends", "Family"],
        "Avg Cost/Person": 1200,
        "Description": "Beautiful landscapes, vineyards, historic towns.",
        "Travel Options": {
            "Flying": {"Cost": 180, "Time": "2h 0m"},
            "Train": {"Cost": 140, "Time": "14h 30m"},
            "Driving": {"Cost": 200, "Time": "13h 0m"}
        }
    },
   {
        "Destination": "Lisbon",
        "Temperature Preference": "Warm",
        "Vacation Purpose": ["Beach", "City trip", "Cultural & Historic", "Nature"],
        "Best Season": ["Spring", "Summer", "Autumn"],
        "Duration": ["Weekend", "Week", "10 days"],
        "Group Suitability": ["Alone", "My Partner", "Friends", "Family", "Colleagues"],
        "Avg Cost/Person": 1200,
        "Description": "A charming city with a blend of rich history, stunning architecture, and beautiful beaches.",
        "Travel Options": {
            "Flying": {"Cost": 200, "Time": "2h 45m"},
            "Train": {"Cost": 180, "Time": "24h"},
            "Driving": {"Cost": 250, "Time": "23h 30m"}
        }
    },
    {
        "Destination": "Barcelona",
        "Temperature Preference": "Warm",
        "Vacation Purpose": ["Beach", "City trip", "Cultural & Historic", "Nature", "Active"],
        "Best Season": ["Spring", "Summer", "Autumn"],
        "Duration": ["Weekend", "Week", "10 days"],
        "Group Suitability": ["Alone", "My Partner", "Friends", "Family", "Colleagues"],
        "Avg Cost/Person": 1300,
        "Description": "A vibrant city known for its art, architecture, and Mediterranean beaches.",
        "Travel Options": {
            "Flying": {"Cost": 150, "Time": "2h 15m"},
            "Train": {"Cost": 200, "Time": "13h 30m"},
            "Driving": {"Cost": 180, "Time": "14h 30m"}
        }
    },
    {
        "Destination": "Monaco",
        "Temperature Preference": "Warm",
        "Vacation Purpose": ["City trip", "Cultural & Historic", "Beach"],
        "Best Season": ["Spring", "Summer"],
        "Duration": ["Weekend", "Week"],
        "Group Suitability": ["Alone", "My Partner", "Friends", "Colleagues"],
        "Avg Cost/Person": 1800,
        "Description": "A glamorous destination with luxury, beaches, and a rich cultural heritage.",
        "Travel Options": {
            "Flying": {"Cost": 250, "Time": "2h 0m"},
            "Train": {"Cost": 220, "Time": "10h 45m"},
            "Driving": {"Cost": 200, "Time": "12h 30m"}
        }
    },
    {
        "Destination": "Berlin",
        "Temperature Preference": "Cold",
        "Vacation Purpose": ["City trip", "Cultural & Historic", "Active"],
        "Best Season": ["Spring", "Autumn", "Winter"],
        "Duration": ["Weekend", "Week", "10 days"],
        "Group Suitability": ["Alone", "My Partner", "Friends", "Family", "Colleagues"],
        "Avg Cost/Person": 1000,
        "Description": "A city rich in history with a vibrant cultural scene and numerous landmarks.",
        "Travel Options": {
            "Flying": {"Cost": 100, "Time": "1h 15m"},
            "Train": {"Cost": 80, "Time": "6h 30m"},
            "Driving": {"Cost": 120, "Time": "7h 0m"}
        }
    },
    {
        "Destination": "Scandinavia",
        "Temperature Preference": "Cold",
        "Vacation Purpose": ["Nature", "Cultural & Historic", "Active"],
        "Best Season": ["Summer", "Winter"],
        "Duration": ["Week", "10 days", "2 weeks"],
        "Group Suitability": ["Alone", "My Partner", "Friends", "Family"],
        "Avg Cost/Person": 2000,
        "Description": "A region of stunning natural beauty, outdoor activities, and rich history.",
        "Travel Options": {
            "Flying": {"Cost": 300, "Time": "1h 45m"},
            "Train": {"Cost": 250, "Time": "18h 0m"},
            "Driving": {"Cost": 400, "Time": "17h 0m"}
        }
    },
    {
        "Destination": "Athens",
        "Temperature Preference": "Warm",
        "Vacation Purpose": ["Cultural & Historic", "City trip"],
        "Best Season": ["Spring", "Summer", "Autumn"],
        "Duration": ["Weekend", "Week", "10 days"],
        "Group Suitability": ["Alone", "My Partner", "Friends", "Family"],
        "Avg Cost/Person": 1400,
        "Description": "A city steeped in ancient history with impressive monuments and vibrant culture.",
        "Travel Options": {
            "Flying": {"Cost": 180, "Time": "3h 15m"},
            "Train": {"Cost": 400, "Time": "32h 0m"},
            "Driving": {"Cost": 350, "Time": "25h 0m"}
        }
    },
    {
        "Destination": "Rome",
        "Temperature Preference": "Warm",
        "Vacation Purpose": ["Cultural & Historic", "City trip", "Active"],
        "Best Season": ["Spring", "Autumn"],
        "Duration": ["Weekend", "Week", "10 days"],
        "Group Suitability": ["Alone", "My Partner", "Friends", "Family"],
        "Avg Cost/Person": 1600,
        "Description": "An ancient city with a wealth of history, art, and culture at every corner.",
        "Travel Options": {
            "Flying": {"Cost": 170, "Time": "2h 15m"},
            "Train": {"Cost": 220, "Time": "15h 0m"},
            "Driving": {"Cost": 250, "Time": "15h 30m"}
        }
    },
    {
        "Destination": "Prague",
        "Temperature Preference": "Cold",
        "Vacation Purpose": ["City trip", "Cultural & Historic"],
        "Best Season": ["Spring", "Autumn", "Winter","Summer"],
        "Duration": ["Weekend", "Week"],
        "Group Suitability": ["Alone", "My Partner", "Friends", "Family"],
        "Avg Cost/Person": 1100,
        "Description": "A city of stunning architecture, rich history, and a vibrant cultural scene.",
        "Travel Options": {
            "Flying": {"Cost": 130, "Time": "1h 40m"},
            "Train": {"Cost": 90, "Time": "11h 0m"},
            "Driving": {"Cost": 150, "Time": "9h 0m"}
        }
    },
    {
        "Destination": "Greek Islands",
        "Temperature Preference": "Warm",
        "Vacation Purpose": ["Beach", "Nature", "Cultural & Historic"],
        "Best Season": ["Spring", "Summer"],
        "Duration": ["Week", "10 days", "2 weeks"],
        "Group Suitability": ["My Partner", "Friends", "Family"],
        "Avg Cost/Person": 1700,
        "Description": "Beautiful islands with stunning beaches, crystal clear waters, and rich history.",
        "Travel Options": {
            "Flying": {"Cost": 250, "Time": "3h 30m"},
            "Train": {"Cost": 450, "Time": "35h 0m"},
            "Driving": {"Cost": 400, "Time": "30h 0m"}
        }
    },
    {
        "Destination": "Split",
        "Temperature Preference": "Warm",
        "Vacation Purpose": ["Beach", "Cultural & Historic", "Nature"],
        "Best Season": ["Summer", "Spring"],
        "Duration": ["Weekend", "Week", "10 days"],
        "Group Suitability": ["My Partner", "Friends", "Family"],
        "Avg Cost/Person": 1300,
        "Description": "A coastal city with beautiful beaches, historic sites, and natural beauty.",
        "Travel Options": {
            "Flying": {"Cost": 220, "Time": "2h 0m"},
            "Train": {"Cost": 300, "Time": "24h 0m"},
            "Driving": {"Cost": 280, "Time": "18h 0m"}
        }
    },
    {
        "Destination": "Istanbul",
        "Temperature Preference": "Warm",
        "Vacation Purpose": ["City trip", "Cultural & Historic", "Beach"],
        "Best Season": ["Spring", "Summer", "Autumn"],
        "Duration": ["Week", "10 days"],
        "Group Suitability": ["Alone", "My Partner", "Friends", "Family", "Colleagues"],
        "Avg Cost/Person": 1500,
        "Description": "Rich cultural experiences, iconic landmarks, and excellent cuisine.",
        "Travel Options": {
            "Flying": {"Cost": 150, "Time": "3h 25m"},
            "Train": {"Cost": 200, "Time": "60h 00m"},
            "Driving": {"Cost": 1270, "Time": "27h 00m"}
        }
    },
    {
        "Destination": "Dublin",
        "Temperature Preference": "Cold",
        "Vacation Purpose": ["City trip", "Cultural & Historic", "Nature"],
        "Best Season": ["Spring", "Autumn"],
        "Duration": ["Week", "Mid-week","10 days", "Weekend"],
        "Group Suitability": ["Alone", "My Partner", "Friends", "Family", "My siblings"],
        "Avg Cost/Person": 1500,
        "Description": "Rich cultural experiences, iconic landmarks, and excellent cuisine.",
        "Travel Options": {
            "Flying": {"Cost": 50, "Time": "1h 00m"},
            "Train": {"Cost": 250, "Time": "15h 30m"},
            "Driving": {"Cost": 440, "Time": "14h 30m"}
        }
    },
    {
        "Destination": "Vienna",
        "Temperature Preference": "Cold",
        "Vacation Purpose": ["City trip", "Cultural & Historic", "Nature"],
        "Best Season": ["Spring", "Autumn", "Winter"],
        "Duration": ["Weekend", "Mid-week", "Week"],
        "Group Suitability": ["Alone", "My Partner", "Friends", "Family", "My siblings"],
        "Avg Cost/Person": 1200,
        "Description": "Elegant palaces, classical music, and picturesque parks.",
        "Travel Options": {
            "Flying": {"Cost": 70, "Time": "2h 00m"},
            "Train": {"Cost": 180, "Time": "7h 00m"},
            "Driving": {"Cost": 250, "Time": "6h 00m"}
        }
    },
    {
        "Destination": "Edinburgh",
        "Temperature Preference": "Cold",
        "Vacation Purpose": ["City trip", "Cultural & Historic", "Nature", "Active"],
        "Best Season": ["Spring", "Summer", "Autumn"],
        "Duration": ["Weekend", "Mid-week", "Week","10 days", "2 weeks"],
        "Group Suitability": ["Alone", "My Partner", "Friends", "Family"],
        "Avg Cost/Person": 1300,
        "Description": "Medieval castles, festivals, and beautiful highland scenery.",
        "Travel Options": {
            "Flying": {"Cost": 60, "Time": "1h 30m"},
            "Train": {"Cost": 250, "Time": "6h 00m"},
            "Driving": {"Cost": 300, "Time": "7h 00m"}
        }
    },
    {
        "Destination": "Copenhagen",
        "Temperature Preference": "cold",
        "Vacation Purpose": ["City trip", "Cultural & Historic", "Nature"],
        "Best Season": ["Spring", "Summer"],
        "Duration": ["Weekend", "Mid-week", "Week"],
        "Group Suitability": ["Alone", "My Partner", "Friends", "Family"],
        "Avg Cost/Person": 1400,
        "Description": "Charming, eco-friendly city with historic sites and scenic waterfronts.",
        "Travel Options": {
            "Flying": {"Cost": 70, "Time": "1h 45m"},
            "Train": {"Cost": 220, "Time": "10h 00m"},
            "Driving": {"Cost": 350, "Time": "11h 00m"}
        }
    }
]


# In[117]:


# Function to determine vacation destination.
# Original function

def vacation_planner():
    print("Let's plan your European vacation from Amsterdam!")

    # Users input, questions Temperature preferance, Vacation purpose, which season, the duration of their vacation, 
    #with whom the user is going and how much budget they have.
    temp_preference = input("Do you want to go on a vacation to a warm or a cold place? ")
    if temp_preference not in ["Warm", "Cold"]:
        print("Invalid input for temperature preference.")
        return
    
    if temp_preference == "Warm":
        vacation_purpose = input("What is the purpose of your vacation? (Beach, City trip, Cultural & Historic, Nature, Active): ")
    else:
        vacation_purpose = input("What is the purpose of your vacation? (City trip, Cultural & Historic, Nature, Active, Skiing and Snowboarding): ")

    best_season = input("When are you going on vacation? (Summer, Autumn, Winter, Spring): ")
    duration = input("For how long are you going on vacation? (Weekend, Mid-week, Week, 10 days, 2 weeks, 3 weeks, Month): ")
    group_type = input("With whom are you going on vacation? (Alone, Best friend, My Partner, Friends, Colleagues, My family, My parents, My siblings): ")
    budget = int(input("What is your max budget per person? (in USD): "))

    # Filter destinations based on users input
    filtered_destinations = [
        dest for dest in destinations
        if (dest["Temperature Preference"] == temp_preference and
           vacation_purpose in dest["Vacation Purpose"] and
           best_season in dest["Best Season"] and
           duration in dest["Duration"] and
           group_type in dest["Group Suitability"] and
           dest["Avg Cost/Person"] <= budget)
    ]
      
    #displays possible destinations and temperature preferance.
    display_destination(filtered_destinations)
# Call the function
vacation_planner()


# In[ ]:


#splitting function into multiple smaller functions.


# In[118]:


# Function to querry user on temperature preference of their vacation location.
def querry_temperature_preference():
    temp_preference = input("Do you want to go on a vacation to a warm or a cold place? ")
    if temp_preference not in ["Warm", "Cold"]:
        raise ValueError("Invalid input for temperature preference.")
    return temp_preference


# In[119]:


# Function to querry user on the purpose of their vacation, this function is based on temperature preference 
# as you can't do the same things in cold places as you can in warm places.
def querry_vacation_purpose(temp_preference):
    if temp_preference == "Warm":
        return input("What is the purpose of your vacation? (Beach, City trip, Cultural & Historic, Nature, Active): ")
    else:
        return input("What is the purpose of your vacation? (City trip, Cultural & Historic, Nature, Active, Skiing and Snowboarding): ")


# In[120]:


# Functions to querry user on perfered season, duration, group type, and budget fpr the vacation.
def querry_best_season():
    return input("When are you going on vacation? (Summer, Autumn, Winter, Spring): ")

def querry_duration():
    return input("For how long are you going on vacation? (Weekend, Mid-week, Week, 10 days, 2 weeks, 3 weeks, Month): ")

def querry_group_type():
    return input("With whom are you going on vacation? (Alone, Best friend, My Partner, Friends, Colleagues, My family, My parents, My siblings): ")

def querry_budget():
    return int(input("What is your max budget per person? (in USD): "))


# In[121]:


# Function to filter destinations based on user input
def filter_destinations(temp_preference, vacation_purpose, best_season, duration, group_type, budget):
    return [
        dest for dest in destinations
        if (dest["Temperature Preference"] == temp_preference and
           vacation_purpose in dest["Vacation Purpose"] and
           best_season in dest["Best Season"] and
           duration in dest["Duration"] and
           group_type in dest["Group Suitability"] and
           dest["Avg Cost/Person"] <= budget)
    ]


# In[122]:


# display functions for querries

def display_temp_preference(temp_preference):
    print(f"You prefer a {temp_preference.lower()} destination.")

def display_vacation_purpose(vacation_purpose):
    print(f"Your vacation purpose is: {vacation_purpose}.")

def display_best_season(best_season):
    print(f"Your chosen season for travel is: {best_season}.")

def display_duration(duration):
    print(f"You plan to go for: {duration}.")

def display_group_type(group_type):
    print(f"You are traveling with: {group_type}.")

def display_budget(budget):
    print(f"Your maximum budget per person is: ${budget}.")

# Display function for user choices, displays all answers of the user on the querries asked in querry functions.
def display_user_choices(temp_preference, vacation_purpose, best_season, duration, group_type, budget):
    display_temp_preference(temp_preference)
    display_vacation_purpose(vacation_purpose)
    display_best_season(best_season)
    display_duration(duration)
    display_group_type(group_type)
    display_budget(budget)
    
# Display function output, shows possible destinations based on input user which was displayed in function display_user_choices.
def display_destination(destinations):
    if not destinations:
        print("No destinations found that match your criteria.")
    else:
        print("Here are some vacation destinations that match your criteria:")
        for dest in destinations:
            print(f"\nDestination: {dest['Destination']}")
            print(f"  - Average Cost per Person: ${dest['Avg Cost/Person']}")
            print(f"  - Description: {dest['Description']}")
            print("  - Travel Options:")
            for option, details in dest["Travel Options"].items():
                print(f"    * {option}: ${details['Cost']}, {details['Time']}")


# In[123]:


# Main function to orchestrate the vacation planner
def vacation_planner():
    print("Let's plan your European vacation from Amsterdam!")

    # querries for user that provides the inputs to make a desicion on location
    temp_preference = querry_temperature_preference()
    vacation_purpose = querry_vacation_purpose(temp_preference)
    best_season = querry_best_season()
    duration = querry_duration()
    group_type = querry_group_type()
    budget = querry_budget()

    # Display the user's choices
    print("\nHere are your vacation preferences:")
    display_user_choices(temp_preference, vacation_purpose, best_season, duration, group_type, budget)
    
    # Filter destinations based on user input
    filtered_destinations = filter_destinations(
        temp_preference, vacation_purpose, best_season, duration, group_type, budget
    )
      
    # Display results
    display_destination(filtered_destinations)

# Run the main function
vacation_planner()


# In[ ]:




