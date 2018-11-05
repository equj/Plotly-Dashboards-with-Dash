#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Perform imports here:
import pandas as pd
import plotly.figure_factory as ff
import plotly.offline as pyo

# create a DataFrame from the .csv file:
df = pd.read_csv('../data/iris.csv')


# Define the traces
i_set = df[df['class']=='Iris-setosa']['petal_length']
i_ver = df[df['class']=='Iris-versicolor']['petal_length']
i_vir = df[df['class']=='Iris-virginica']['petal_length']

# HINT:
# This grabs the petal_length column for a particular flower
#df[df['class']=='Iris-some-flower-class']['petal_length']

# Define a data variable
iris_data = [i_set, i_ver, i_vir]
group_labels = ['Iris-setosa','Iris-versicolor','Iris-virginica']

# Create a fig from data and layout, and plot the fig
fig = ff.create_distplot(iris_data, group_labels)
pyo.plot(fig, filename='iris.html')
