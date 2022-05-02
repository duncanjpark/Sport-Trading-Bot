#!/usr/bin/env python3

import statsmodels.formula.api as smf
import pandas as pd
from IPython.display import display
import numpy as np
from matplotlib import pyplot as plt

# sys.path.insert(0, '../data')

# from  import display_events

types = {
    'Hitters': 'str',
    "H-AB": 'str',
    'AB': 'str',
    'R': 'int',
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


initial_DF = pd.read_csv('../data/hittersByGame.csv',
                         header=0, names=types.keys())

for i, col in enumerate(types.keys()):
    if i > 1 and i < 12:
        initial_DF[col] = pd.to_numeric(initial_DF[col], errors='coerce')


display(initial_DF)

initial_DF = initial_DF[['Hitters', 'R', 'AB', 'Game']]

mlb_data = initial_DF

mlb_data.info()

print('\n')

model = smf.ols('R ~ AB', data=mlb_data)
results = model.fit()

print(results.params)
print(results.tvalues)
print(results.t_test([1, 0]))
print(results.f_test(np.identity(2)))

run_predict = results.predict()

# Plot regression against actual data
plt.figure(figsize=(12, 6))
# scatter plot showing actual data
plt.plot(mlb_data['AB'], mlb_data['R'], 'o')
plt.plot(mlb_data['AB'], run_predict, 'r', linewidth=2)   # regression line
plt.xlabel('AB')
plt.ylabel('Runs')
plt.title('AB vs Runs')

plt.show()
