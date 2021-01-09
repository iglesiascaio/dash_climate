import dash
import dash_html_components as html
import dash_core_components as dcc
import sys
sys.path.insert(1, '../convertCSV')
from read_files import all_dataframes_generator
sys.path.insert(1, 'auxiliaryfunctions')
from dataframe_years import separate_data_meteo
import plotly.graph_objs as go

'''
This file reads the data from a csv file, and then uses the function separate_date_meteo() 
for organizing the data, by separating the parameters desired by years. It supports a 
multi-dropdown feature, that interacts directly with the file 'menu_dash.py', 
that contains the appcallback that is necessary for the multi dropdown functionality to work.
The graph restricts the selection of 2 functions, because it's a graph with a maximum of two 
y-axis.
'''

df_all_years = all_dataframes_generator()["observation-meteorologique-historiques-france-synop-orly"]
data_temperature,data_pression,data_precipitation,data_humidity,years = separate_data_meteo()

graph_meteo_france_layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown-graph_meteo_france',
        options=[

            {'label': 'Temperature', 'value': 'Temperature'},
            {'label': 'Pression', 'value': 'Pression'},
            {'label': 'Precipitation', 'value': 'Precipitation'},
            {'label': 'Humidity', 'value': 'Humidity'},
        

        ],
        multi = True,
        value = ['Temperature', 'Pression'],
        
    ),
    dcc.Graph(
        id='graph-graph_meteo_france',
        config={
            'showSendToCloud': True,
            'plotlyServerURL': 'https://plot.ly'
        }
    )
])

