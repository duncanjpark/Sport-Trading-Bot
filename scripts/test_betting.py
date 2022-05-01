#!/usr/bin/env python3

from betting import display_events, get_events, display_outcomes
from IPython.display import display
import pandas as pd


events = get_events("NBA")

print('\n')

display_events(events)

event = events.iloc[[1]]

dispGroups = event['displayGroups'][1]

displayGroup = dispGroups[0]
markets = displayGroup['markets']
markets = pd.DataFrame(markets)

market = markets.iloc[[0]]

print('\n\n')


display_outcomes(market)
