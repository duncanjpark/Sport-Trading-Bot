#!/usr/bin/env python3

"""

Function definitions for operations on the bets.py and portfolio.py classes

"""
import pandas as pd
import requests

# Constants for URLs
path = "https://www.bovada.lv/services/sports/event/coupon/events/A/description"
URLs = {
    "NBA": path + "/basketball/nba",
    "NFL": path + "/description/football/nfl"
}


# Function to initialize events for a given league
def get_events(league):
    # Returns: dataframe of events with their start times and if they're live
    # Parameters: a league (constant)
    data = requests.get(URLs[league]).json()
    data = data[1]["events"]

    print(data)

# Place bet
    # Returns: confirmation of bet placed
    # Parameters: outcome object, stake, portfolio object

# Display all events
    # Returns: void
    # Parameters: dataframe of events
