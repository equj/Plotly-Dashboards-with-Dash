#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Perform imports here:
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo



# create a DataFrame from the .csv file:
df = pd.read_csv('../data/mpg.csv')

df['text_disp']=df['name'] + ' with ' + df['horsepower'] + ' HP'
print(df.head())
# create data by choosing fields for x, y and marker size attributes

data = [go.Scatter(
    x=df['mpg'],
    y=df['acceleration'],
    text=df['text_disp'],
    mode='markers',
    marker=dict(size=3*df['cylinders'],
    color=df['displacement'],
    showscale=True)
)]

# create a layout with a title and axis labels
layout = go.Layout(
    title='Cars Acceleration vs mpg',
    xaxis=dict(title='mpg'),
    yaxis=dict(title='Acceleration'),
    hovermode='closest'
)

# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubble_ex.html')
