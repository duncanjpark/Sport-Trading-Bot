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
    "NFL": path + "/football/nfl",
    "MLB": path + "/baseball/mlb"
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


def display_events(events):
    print('\n')
    events['startTime'] += -14400000    # adjust to Eastern Timezone
    events['startTime'] = pd.to_datetime(
        events['startTime'], unit='ms', origin='unix')  # convert formatting
    display(events[['description', 'startTime']])   # display events and time


def display_outcomes(market):
    print('\n')
    outcomes = market['outcomes']

    print("Market:     " + market['description']
          + market['period']['description'])
    impliedTotal = 0
    for outcome in outcomes:
        print("Outcome:     " + outcome['description'])
        print("Odds:     Decimal:  " + outcome['price']['decimal']
              + "  American:  " + outcome['price']['american'])
        print("Implied Odds:     %4.4f\n" %
              implied(outcome))
        impliedTotal += implied(outcome)
    print("Cumulative sum of implied odds:     %4.4f" % impliedTotal)
    print("House Edge:     %4.4f%%\n" % ((impliedTotal - 1)*100))


def implied(outcome):
    return (1 / float(outcome['price']['decimal']))


def get_user_choice(size):
    print()
    num = input("Enter the Index of the element you are interested "
                + "in from the displayed data set:  ")
    user_in = int(num) if num.isdigit() else -1
    while(not (user_in < size and user_in >= 0)):
        num = input("Please enter a valid index:  ")
        user_in = int(num) if num.isdigit() else -1

    return user_in


def league_prompt():
    leagues = pd.DataFrame(["NBA", "NFL", "MLB"], columns=['League'])
    display(leagues)
    which = get_user_choice(leagues.shape[0])
    return leagues['League'][which]


def event_prompt(events):
    display_events(events)

    which = get_user_choice(events.shape[0])
    return which, events.iloc[[which]]


def displayGroup_prompt(displayGroups):
    print("Offered types of bets for this event:")
    displayGroups_DF = pd.DataFrame(displayGroups['description'])
    print(displayGroups_DF)
    which = get_user_choice(displayGroups_DF.shape[0])

    return which, displayGroups.iloc[[which]]


def market_prompt(displayGroup, which):
    print("\nKind of Bet: " + displayGroup['description'][which])
    markets_DF = pd.DataFrame(displayGroup['markets'][which])

    markets_DF['period'] = markets_DF['period'].apply(
        lambda x: x['description'])

    display(markets_DF[['descriptionKey', 'description', 'period', 'status']])

    whichM = get_user_choice(markets_DF.shape[0])
    return markets_DF.iloc[whichM]


def all_event_outcomes(whichE, event, f):
    displayGroups = pd.DataFrame(event['displayGroups'][whichE])
    for i in range(displayGroups.shape[0]):
        displayGroup = displayGroups.iloc[[i]]
        markets_DF = pd.DataFrame(displayGroup['markets'][i])
        for q in range(markets_DF.shape[0]):
            market = markets_DF.iloc[q]
            print("Market: %s, %s. House Edge:     %4.4f%%" %
                  (market['description'], market['period']['description'],
                   house_edge(market)))
            f.write("Market: %s, %s. House Edge:     %4.4f%%\n" %
                    (market['description'], market['period']['description'],
                     house_edge(market)))


def house_edge(market):
    outcomes = market['outcomes']

    impliedTotal = 0
    for outcome in outcomes:
        impliedTotal += implied(outcome)

    return ((impliedTotal - 1)*100)
