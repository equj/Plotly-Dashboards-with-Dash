#######
# Objective: Create a histogram that plots the 'length' field
# from the Abalone dataset (../data/abalone.csv).
# Set the range from 0 to 1, with a bin size of 0.02
######

# Perform imports here:
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

# create a DataFrame from the .csv file:
#abalone_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data'
#df = pd.read_csv(abalone_url)

df = pd.read_csv('../data/abalone.csv')

# create a data variable:
data =[go.Histogram(
    x = df['length'],
    xbins = dict(start=0, end=1, size=0.02)
    ),
    go.Histogram(
        x = df['length'],
        nbinsx=100
)]

# add a layout
layout = go.Layout(
    title = 'Length of Abalones',
    barmode='overlay'
)

# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='hist_abalone.html')
