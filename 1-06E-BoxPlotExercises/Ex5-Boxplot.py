#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

# Perform imports here:
import plotly.graph_objs as go
import plotly.offline as pyo
import pandas as pd
import numpy as np

# create a DataFrame from the .csv file:
#reading data set online
abalone_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data'
df = pd.read_csv(abalone_url)

# take two random samples of different sizes:
set1 = list(df['rings'][np.random.randint(0,4177, 200)])
set2 = list(df['rings'][np.random.randint(0,4177, 400)])


# create a data variable with two Box plots:
data = [
    go.Box(
    y = set1,
    name = 'Randome Set 1',
    boxpoints='all',
    jitter=0.3,
    pointpos=-1.8
    ),
    go.Box(
        y = set2,
        name = 'Randome Set 2',
        boxpoints='all',
        jitter=0.3,
        pointpos=-1.8
    )
]
layout = go.Layout(
    title = 'Two box plots of randomly selected '
    )
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='box_ex.html')










# add a layout




# create a fig from data & layout, and plot the fig
