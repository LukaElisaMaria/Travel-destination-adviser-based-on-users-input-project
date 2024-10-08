#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import random
import ipywidgets as widgets
from IPython.display import display
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import tkinter as tk
from tkinter import ttk


# In[2]:


#dataset
#destinations are: Paris, Swiss Apls, Tuscany, Lisbon, Barcelona, Monaco, Berlin, Scandinavia, Athens, Rome, Prague,
# Greek Islands, Split
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
    }
]


# In[27]:


# Function to determine vacation destination.

def vacation_planner():
    print("Let's plan your European vacation from Amsterdam!")

    # User input
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
    group_type = input("With whom are you going on vacation? (Alone, Best friend, My Partner, Group of girl friends, Group of Guy friends, Group of friends, Colleagues, My family, My parents, My siblings): ")
    budget = int(input("What is your max budget per person? (in USD): "))

    # Filter destinations based on user input
    filtered_destinations = [
        dest for dest in destinations
        if (dest["Temperature Preference"] == temp_preference and
           vacation_purpose in dest["Vacation Purpose"] and
           best_season in dest["Best Season"] and
           duration in dest["Duration"] and
           group_type in dest["Group Suitability"] and
           dest["Avg Cost/Person"] <= budget)
    ]

#     for dest in destinations:
#         if dest["Temperature Preference"] == temp_preference:
#             if vacation_purpose in dest["Vacation Purpose"]:
#                 if best_season in dest["Best Season"]:
#                     if duration in dest["Duration"]:
#                         if group_type in dest["Group Suitability"]:
#                             if dest["Avg Cost/Person"] <= budget:
#                                 print("Avg Cost is True")
#                                 filtered_destinations.append(dest)
        
    
    # Display the recommended destination(s)
    if len(filtered_destinations) != 0:
        for dest in filtered_destinations:
            print(f"\nBased on your preferences, we recommend visiting {dest['Destination']}!")
            print(f"Description: {dest['Description']}")
            print(f"Average cost per person: ${dest['Avg Cost/Person']}")
            print("Travel Options from Amsterdam:")
            for mode, details in dest["Travel Options"].items():
                print(f"  {mode}: Cost - ${details['Cost']}, Time - {details['Time']}")
    else:
        print("\nSorry, no destinations match your preferences and budget. Try adjusting your options.")

# Call the function
vacation_planner()


# In[ ]:





# In[ ]:





# In[ ]:




