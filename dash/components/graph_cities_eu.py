import dash
import dash_core_components as dcc
import dash_html_components as html
import sys
sys.path.append('../')
import pandas as pd

from temperatures_europe.load_usefull_data_in_dataframe import create_dataframe

'''
This file creates a graph of the evolution of the temperatures for each year, for a number of cities selected.
It supports a multi-dropdown feature, that interacts directly with the file 'menu_dash.py', that contains the
appcallback that is necessary for the multi dropdown functionality to work

'''

#loading dataframe
df=create_dataframe()

def temp_values(i):
    data_serie=df.iloc[i][0]

    #removing NaN values
    data_final=data_serie.dropna()

    #data for the graph
    x=data_final.index
    y=data_final.tolist()
    return {'x':x, 'y':y}

graph_cities_eu_layout = html.Div(children=[
   dcc.Dropdown(
        id='my-dropdown-graph_cities_eu',
        options=[

            {'label': 'BERLIN-DAHLEM', 'value': 'BERLIN-DAHLEM'},
            {'label': 'CORFU', 'value': 'CORFU'},
            {'label': 'KIEV', 'value': 'KIEV'},
            {'label': 'MADRID', 'value': 'MADRID'},
            {'label': 'MOSCOW', 'value': 'MOSCOW'},
            {'label': 'PARIS', 'value': 'PARIS'},
            {'label': 'ROMA', 'value': 'ROMA'},
            {'label': 'SHAWBURY', 'value': 'SHAWBURY'},
            {'label': 'STOCKHOLM', 'value': 'STOCKHOLM'},
            {'label': 'VAN', 'value': 'VAN'},
            {'label': 'WIEN', 'value': 'WIEN'},
            

        ],
        multi = True,
        value = ['ROMA', 'PARIS']
    ),
    dcc.Graph(
        id='graph-graph_cities_eu',
        config={
            'showSendToCloud': True,
            'plotlyServerURL': 'https://plot.ly'
        }
    )
])

    