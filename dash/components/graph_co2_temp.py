
from dataframe_years import get_data_co2_temp
import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.graph_objs as go

# get data from database
df = get_data_co2_temp()

'''
This file builds a correlation graph, containing the values of concentration of CO2 (ppm) and 
the temperature anomalies (related to a base period, 1951-1980, with the source GISTEMP). The 
graph also divides the years in groups, for facilitating the visualization of the evolution of
both parameters 
'''


corr = '{0:.2%}'.format(df['Temperature'].corr(df['CO2']))

graph_co2_temp_layout = html.Div([
    dcc.Graph(
        id='life-exp-vs',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['Group'] == i]['CO2'],
                    y=df[df['Group'] == i]['Temperature'],
                    text=df[df['Group'] == i]['Year'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.Group.unique()
            ],
            'layout': go.Layout(
                title = 'The correlation between the T°C and the CO2 ppm is '+corr ,
                titlefont={
                    'size':25
                },
                xaxis={'title': 'CO2 ppm', 'titlefont':{'size':20}},
                yaxis={'title': 'Temperature anomalies', 'titlefont':{'size':20}},
                height=650,
                margin=go.layout.Margin(
                    l=50,
                    r=50,
                    b=100,
                    t=100,
                    pad=4
                ),
                legend={'x': 0, 'y': 1},
                hovermode='closest',
               
            )
        }
    )
])





