import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

'''
This file builds an interactive map, that shows the concentration of CO2 per capita for each
country. The bar in the right represents the scale for analysing the colors of the map.
'''

filename='../Data/co2/co-emissions-per-capita.csv'
df = pd.read_csv(filename, delimiter=',')
df = df[df['Year'] == 2017]

map_co2_layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        style={
            'height':'250px'
        },
        figure={
            'data': [go.Choropleth(
    locations = df['Code'],
    z = df['percapita'],
    text = df['Country'],
    colorscale = 'Reds',
    autocolorscale=False,
    reversescale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_tickprefix = 't',
    colorbar_title = 'Annual CO2 emission',
)],
            'layout': go.Layout(
                title = 'Annual 2017 CO2 emission' ,
                titlefont = {
                    'size':30
                },
                autosize=True,
               
               margin=go.layout.Margin(
                    l=5,
                    r=5,
                    b=0,
                    t=50,
                    pad=3
                )
            )
        }
    )
])






