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


class Market:

    def __init__(self, event, whichDG, whichM, market):
        self.event = event
        self.whichDG = whichDG
        self.whichM = whichM
        self.market = market

    def update(self):
        self.event = update_event(self.event)
        displayGroups = pd.DataFrame(self.event['displayGroups'][0])
        self.whichDG, displayGroup = displayGroup_prompt(
            displayGroups, self.whichDG)
        self.whichM, self.market = market_prompt(
            self.whichDG, displayGroup, self.whichM)

    def full_update(self):
        self.update()
        display_outcomes(self.market)


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
    # display events and time
    display(events[['description', 'startTime', 'live']])


# given a market (Series), displays the outcomes and their implied odds
def display_outcomes(market):
    print('\n')
    outcomes = market['outcomes']

    print("\nMarket:     " + market['description']
          + ", " + market['period'])
    impliedTotal = 0
    for outcome in outcomes:
        impliedTotal += display_outcome(outcome)
    print("Cumulative sum of implied odds:     %4.4f" % impliedTotal)
    print("House Edge:     %4.4f%%\n" % ((impliedTotal - 1)*100))


# returns a float
def implied(outcome):
    return (1 / float(outcome['price']['decimal']))


# returns an int
def get_user_choice(size):
    print()
    num = input("Enter the Index of the element you are interested "
                + "in from the displayed data set:  ")
    user_in = int(num) if num.isdigit() else -1
    while(not (user_in < size and user_in >= 0)):
        num = input("Please enter a valid index:  ")
        user_in = int(num) if num.isdigit() else -1

    return user_in


# returns a league (string)
def league_prompt():
    leagues = pd.DataFrame(["NBA", "NFL", "MLB"], columns=['League'])
    display(leagues)
    which = get_user_choice(leagues.shape[0])
    return leagues['League'][which]


# returns an event (DataFrame) and its index in the events DataFrame
# the returned event DataFrame has 17 columns, including displayGroups
def event_prompt(events):
    display_events(events)

    which = get_user_choice(events.shape[0])
    event = events.iloc[[which]]

    return update_event(event, which)


# returns the index within displayGroups that the returned displayGroup is at
# returned displayGroup is a DataFrame with 6 columns, including markets
def displayGroup_prompt(displayGroups, choice=-1):
    if(choice == -1):
        print("Offered types of bets for this event:")
        displayGroups_DF = pd.DataFrame(displayGroups['description'])
        print(displayGroups_DF)
        which = get_user_choice(displayGroups_DF.shape[0])
    else:
        which = choice

    return which, displayGroups.iloc[[which]]


# returns a market (Series)
def market_prompt(whichDG, displayGroup, choice=-1):
    markets_DF = pd.DataFrame(displayGroup['markets'][whichDG])

    markets_DF['period'] = markets_DF['period'].apply(
        lambda x: x['description'])

    if(choice == -1):
        print("\nKind of Bet: " + displayGroup['description'][whichDG])

        display(
            markets_DF[['descriptionKey', 'description', 'period', 'status']])

        which = get_user_choice(markets_DF.shape[0])
    else:
        which = choice

    return which, markets_DF.iloc[which]


def all_event_outcomes(event, f):
    displayGroups = pd.DataFrame(event['displayGroups'][0])
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


def display_outcome(outcome):
    print("Outcome:     " + outcome['description'])
    print("Odds:     Decimal:  " + outcome['price']['decimal']
          + "  American:  " + outcome['price']['american'])
    print("Implied Odds:     %4.4f" % implied(outcome))
    if 'handicap' in outcome['price'].keys():
        print("Handicap: " + outcome['price']['handicap'])
    print()
    return implied(outcome)


def update_event(event, whichE=0):
    data = requests.get(path + event['link'][whichE]).json()

    event = pd.DataFrame(data)
    event = pd.DataFrame(event['events'][0])

    return event
