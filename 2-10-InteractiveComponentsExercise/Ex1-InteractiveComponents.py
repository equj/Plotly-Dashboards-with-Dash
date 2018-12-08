#######
# Objective: Create a dashboard that takes in two or more
# input values and returns their product as the output.
######

# Perform imports here:

#               Step 1: import things
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# Launch the application:
#              Step 2: launch mani app
app = dash.Dash()

# Create a Dash layout that contains input components
# and at least one output. Assign IDs to each component:

#              Step 3: Creat Dash layout

#build slider markers
smarks = dict()

for i in range (-5,7):
    smarks[i] = str(i)



app.layout = html.Div([
    dcc.RangeSlider(
        id = 'my-slider',
        min=-5,
        max=6,
        marks=smarks,
        value=[-5, 4]),

    html.Br(),
    html.Br(),
    html.H1(id='my-text')
], style={'fontFamily':'helvetica', 'fontSize':18})


# Create a Dash callback:
#           Step 4: Inact call back function
@app.callback(
        Output(component_id='my-text', component_property='children'),
        [Input('my-slider', 'value')])


#          Step 5: Define callback function
def slider_callback(slider_val):
        product = slider_val[0]*slider_val[1]
        return 'slider product: {}'.format(product)


# Add the server clause:
#           Step 6: Run app server!!!

if __name__ == '__main__':
    app.run_server()
