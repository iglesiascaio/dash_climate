import dash
import dash_html_components as html
import dash_core_components as dcc

import sys
sys.path.insert(1, 'auxiliaryfunctions')
from dataframe_years import separate_means_years

'''
This file builds a graph containing the evolution of the temperature during the year, for 
a number of year selected by the uses. It supports a multi-dropdown feature, that interacts 
directly with the file 'menu_dash.py', that contains the appcallback that is necessary for 
the multi dropdown functionality to work
'''

dict_years = separate_means_years()

graph_temp_france_layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown',
        options=[

            {'label': '2010', 'value': '2010'},
            {'label': '2011', 'value': '2011'},
            {'label': '2012', 'value': '2012'},
            {'label': '2013', 'value': '2013'},
            {'label': '2014', 'value': '2014'},
            {'label': '2015', 'value': '2015'},
            {'label': '2016', 'value': '2016'},
            {'label': '2017', 'value': '2017'},
            {'label': '2018', 'value': '2018'},
            {'label': '2019', 'value': '2019'}

        ],
        multi = True,
        value = ['2019','2010']
    ),
    dcc.Graph(
        id='graph',
        config={
            'showSendToCloud': True,
            'plotlyServerURL': 'https://plot.ly'
        }
    )
])


