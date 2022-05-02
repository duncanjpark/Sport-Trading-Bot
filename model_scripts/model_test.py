#!/usr/bin/env python3

import statsmodels.formula.api as smf
import sys
import pandas as pd
from IPython.display import display


# sys.path.insert(0, '../data')

# from  import display_events

types = {
    'Hitters': 'str',
    "H-AB": 'str',
    'AB': 'str',
    'R': 'str',
    'H': 'str',
    'RBI': 'str',
    'BB': 'str',
    'K': 'str',
    '#P': 'str',
    'AVG': 'str',
    'OBP': 'str',
    'SLG': 'str',
    'Game': 'int',
    'Team': 'str',
    'Position': 'str',
    'Hitter Id': 'str'
}

initial_DF = pd.read_csv('../data/hittersByGame.csv', dtype=types)

initial_DF = initial_DF[['Hitters', 'R', 'AB', 'Game']]
display(initial_DF)
initial_DF = initial_DF.dropna(how='all')
"""
filter1 = initial_DF["R"] != "--"
filter2 = initial_DF["R"] != "NaN"
initial_DF.where(filter1, inplace=True)

initial_DF.astype({'R': 'float', 'AB': 'float'}).dtypes
"""
initial_DF.reset_index()
display(initial_DF)

mlb_data = initial_DF

mlb_data.info()

model = smf.ols('R ~ AB', data=mlb_data)
model = model.fit()
