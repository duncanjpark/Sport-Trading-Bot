#!/usr/bin/env python3

from betting import get_events, league_prompt, display_outcomes
from betting import event_prompt, displayGroup_prompt, market_prompt
from betting import all_event_outcomes
from IPython.display import display
import pandas as pd


events = get_events(league_prompt())

whichE, event = event_prompt(events)
f_name = str(event['description'][whichE] + '.txt')

f = open(f_name, "w")


all_event_outcomes(whichE, event, f)

f.close()

#displayGroups = pd.DataFrame(event['displayGroups'][whichE])

#whichDG, displayGroup = displayGroup_prompt(displayGroups)

#market = market_prompt(displayGroup, whichDG)

#display_outcomes(market)
