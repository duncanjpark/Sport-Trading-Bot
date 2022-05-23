#!/usr/bin/env python3

# NBA in play live bot
# moneyline only

from betting import get_events, league_prompt, display_outcomes
from betting import event_prompt, displayGroup_prompt, market_prompt
from betting import all_event_outcomes, update_event, get_user_choice
from betting import Market, get_score, score_change, ML_change
from IPython.display import display
import pandas as pd
import requests
import time


# Constants
LEAGUE_URL = "https://www.bovada.lv/services/sports/event/coupon/" + \
    "events/A/description" + "/basketball/e-basketball/enba/nba-esports-battle-e"

GAME = 0
WHICH_DG = 0
WHICH_MARKET = 0

# get Market object
data = requests.get(LEAGUE_URL).json()
event = pd.json_normalize(data, record_path=['events']).iloc[[GAME]]
the_market = Market(event, WHICH_DG, WHICH_MARKET, None)
the_market.update()
id = the_market.event['id'][0]

# main while loop
while(True):
    print("\nScore Change:")
    display(score_change(get_score(id), id))
    print("\nHome Odds Change:")
    display(ML_change(the_market))
    time.sleep(2)
