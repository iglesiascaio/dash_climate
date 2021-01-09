import dash
import dash_html_components as html
import dash_core_components as dcc
import sys
import pandas as pd
import plotly.graph_objs as go

filename='../Data/co2/annual-co-emissions-by-region.csv'
df = pd.read_csv(filename, delimiter=',')

'''
This file makes a pie chart that show the countries/regions that contribute the most to the 
emission of CO2. It supports a multi-dropdown feature, that interacts directly with the file 'menu_dash.py', 
that contains the appcallback that is necessary for the multi dropdown functionality to work
'''

df_2017 = df[(df['Year'] == 2017) & ((df['Country'] == 'Asia and Pacific (other)') | (df['Country'] == 'China') | (df['Country'] == 'India') | (df['Country'] == 'Africa') | (df['Country'] == 'Middle East') | (df['Country'] == 'United States') | (df['Country'] == 'Americas (other)') | (df['Country'] == 'EU-28') | (df['Country'] == 'Europe (other)') | (df['Country'] == 'International transport')  )]['Annual emissions']  
df_2005 = df[(df['Year'] == 2005) & ((df['Country'] == 'Asia and Pacific (other)') | (df['Country'] == 'China') | (df['Country'] == 'India') | (df['Country'] == 'Africa') | (df['Country'] == 'Middle East') | (df['Country'] == 'United States') | (df['Country'] == 'Americas (other)') | (df['Country'] == 'EU-28') | (df['Country'] == 'Europe (other)') | (df['Country'] == 'International transport') )]['Annual emissions']
df_1995 = df[(df['Year'] == 1995) & ((df['Country'] == 'Asia and Pacific (other)') | (df['Country'] == 'China') | (df['Country'] == 'India') | (df['Country'] == 'Africa') | (df['Country'] == 'Middle East') | (df['Country'] == 'United States') | (df['Country'] == 'Americas (other)') | (df['Country'] == 'EU-28') | (df['Country'] == 'Europe (other)') | (df['Country'] == 'International transport') )]['Annual emissions']   
df_1965 = df[(df['Year'] == 1965) & ((df['Country'] == 'Asia and Pacific (other)') | (df['Country'] == 'China') | (df['Country'] == 'India') | (df['Country'] == 'Africa') | (df['Country'] == 'Middle East') | (df['Country'] == 'United States') | (df['Country'] == 'Americas (other)') | (df['Country'] == 'EU-28') | (df['Country'] == 'Europe (other)') | (df['Country'] == 'International transport') )]['Annual emissions']   



labels = ["Africa", "Americas (other)", "Asia and Pacific (other)", "China", "European Union (28)", "Europe (other)", "India", "International Transport","Middle East", "United States", "Rest of World"]

graph_co2_pie_layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown-graph_co2_pie',
        options=[

            {'label': '2017', 'value': '2017'},
            {'label': '2005', 'value': '2005'},
            {'label': '1995', 'value': '1995'},
            {'label': '1965', 'value': '1965'},
            

        ],
        multi = False,
        value = "2017",
        
    ),
    dcc.Graph(
        id='graph-graph_co2_pie',
        style={
            'top':'55px',
            'left':'0px',
            'right':'5px',
            'bottom':'0px',
            'height':'320px'
        },
        config={
            'showSendToCloud': True,
            'plotlyServerURL': 'https://plot.ly'
        }
    )
])


