#!/usr/bin/env python3

"""

Class definitions for event, displayGroup, market, and outcome

"""

# from datetime import datetime


# Event class
class Event:
    # has descriptive variables such as time, competititors, and link
    # has displayGroup objects
    time = 0
    competititors = {}
    link = ""
    groups = []
    # needs initialization function to take link as argument and fill variables

    def __init__(self, json):
        # which includes creating displayGroup objects
        pass

    # Display event
    def display(self):
        pass

    # Display displayGroups
    def display_DisplayGroups(self):
        pass


# DisplayGroup class
class DisplayGroup:
    # has description and type of bets
    # has market objects
    description = ""
    type = ""
    markets = []

    # needs initialization function to take json argument and fill variables
    def __init__(self, json):
        # which includes creating market objects
        pass

    # Display displayGroup
    def display(self):
        pass

    # Display markets for a displayGroup:
    def display_markets(self):
        # Returns: void
        # Parameters: displayGroup
        pass


# Market class
class Market:
    # has variables such as id, description, and period
    id = 0
    # has outcome objects
    outcomes = []

    # needs initialization function to take json argument and fill variables
    def __init__(self, json):
        # which includes creating outcome objects
        pass

    # Display market
    def display(self):
        pass

    # Display outcomes for a market:
    def display_outcomes(self):
        # Returns: void
        # Parameters: market
        pass


# Outcome class
class Outcome:
    # has outcome type, id, description etc.
    type = ""
    decimal = 2.5
    # and most importantly, the price (odds)
    # from price create implied odds variable
    implied = 1 / decimal

    # needs initialization function to take json argument and fill variables
    def __init__(self, json):
        # which includes calculating implied odds
        pass

    # display outcomes
    def display(self):
        pass
