#!/usr/bin/env python3

from betting import get_events, league_prompt, display_outcomes
from betting import event_prompt, displayGroup_prompt, market_prompt
from betting import all_event_outcomes, update_event, get_user_choice
from betting import Market
from IPython.display import display
import pandas as pd


while(True):
    events = get_events(league_prompt())

    event = event_prompt(events)

    while(True):
        user_in = input(
            "Choose an option:\n[A]ll house edge odds for this event\n"
            + "[S]pecific bet details\n")
        if 's' in user_in.lower():
            displayGroups = pd.DataFrame(event['displayGroups'][0])
            whichDG, displayGroup = displayGroup_prompt(displayGroups)
            whichM, market = market_prompt(whichDG, displayGroup)
            display_outcomes(market)
            # whichO = get_user_choice(200)
            # outcome = market['outcomes'][whichO]
            test_Market = Market(event, whichDG, whichM, market)
            while(True):
                if (get_user_choice(200) == 9):
                    break
                test_Market.full_update()
            break
        elif 'a' in user_in.lower():
            f_name = str('../results/' + event['description'][0] + '.txt')
            f = open(f_name, "w")
            all_event_outcomes(event, f)
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
