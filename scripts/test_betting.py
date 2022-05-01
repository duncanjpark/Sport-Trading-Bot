#!/usr/bin/env python3

from betting import get_events, league_prompt, display_outcomes
from betting import event_prompt, displayGroup_prompt, market_prompt
from betting import all_event_outcomes
# from IPython.display import display
import pandas as pd

while(True):
    events = get_events(league_prompt())

    whichE, event = event_prompt(events)

    while(True):
        user_in = input(
            "Choose an option:\n[A]ll house edge odds for this event\n"
            + "[S]pecific bet details\n")
        if 's' in user_in.lower():
            displayGroups = pd.DataFrame(event['displayGroups'][whichE])
            whichDG, displayGroup = displayGroup_prompt(displayGroups)
            market = market_prompt(displayGroup, whichDG)
            display_outcomes(market)
            break
        elif 'a' in user_in.lower():
            f_name = str(event['description'][whichE] + '.txt')
            f = open(f_name, "w")
            all_event_outcomes(whichE, event, f)
            f.close()
            break
        else:
            pass

    user_in = input(
        "Would you like to do another round of searching/operations? Y/N: ")
    if 'n' in user_in.lower():
        break
    elif 'y' in user_in.lower():
        pass
