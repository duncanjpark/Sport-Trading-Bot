#!/usr/bin/env python3

"""

Function definitions for operations on the bets.py and portfolio.py classes

"""
import pandas as pd
import requests
from IPython.display import display


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

    # Flatten data
    events = pd.json_normalize(data, record_path=['events'])

    # return dataframe of events
    return events


# Place bet
    # Returns: confirmation of bet placed
    # Parameters: outcome object, stake, portfolio object

# Display all events
    # Returns: void
    # Parameters: dataframe of events


def display_events(events):
    events['startTime'] += -14400000    # adjust to Eastern Timezone
    events['startTime'] = pd.to_datetime(
        events['startTime'], unit='ms', origin='unix')  # convert formatting
    display(events[['description', 'startTime']])   # display events and time


def display_outcomes(market):
    outcomes = market['outcomes'][0]
    print("Market:     " + market['description'][0] + "\n")
    impliedTotal = 0
    for outcome in outcomes:
        print("Outcome:     " + outcome['description'])
        print("Odds:     Decimal:  " + outcome['price']['decimal']
              + "  American:  " + outcome['price']['american'])
        print("Implied Odds:     %4.4f\n" %
              implied(outcome['price']['decimal']))
        impliedTotal += implied(outcome['price']['decimal'])
    print("Cumulative sum of implied odds:     %4.4f" % impliedTotal)
    print("House Edge:     %4.4fs%%" % ((impliedTotal - 1)*100))


def implied(odds):
    return (1 / float(odds))
