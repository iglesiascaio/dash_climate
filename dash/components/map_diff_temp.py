import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import sys
sys.path.append('../')
from temperatures_europe.useful_data import find_useful_data
from temperatures_europe.load_city_codes import load_lat_long

'''
This file builds a map, using the data used also in 'graph_cities_eu', by showing the 
variation of temperatures for each city represented in the other graph. It's important
to remark that we have constrained the data to the years 1966-2000, because we for that 
years we had the data for all cities. 
'''

# get data from database
diff, list_city_names = find_useful_data()

mapbox_access_token = 'pk.eyJ1IjoiaWdsZXNpYXNjYWlvIiwiYSI6ImNrMzdtcXRsMDAwZWEzY3Bicmc4eDVjbTEifQ.QXmHM3Bpv9rkd165-I8w_A'

lat,long,list_cities_not_ordered = load_lat_long()

lat_ordered = [x for _,x in sorted(zip(list_cities_not_ordered,lat))]
long_ordered = [x for _,x in sorted(zip(list_cities_not_ordered,long))]

map_diff_temp_layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp-map_diff_temp',
        style={
            #'width':'500px',
            'height':'470px',
        },
        figure={
            'data': [
                go.Scattermapbox(
                    lat= lat_ordered,
                    lon= long_ordered,
                    mode='markers',
                    marker=go.scattermapbox.Marker(
                        size= 17,
                        color= diff,
                        autocolorscale = True,
                        colorbar=dict(
                        title="Colorbar"
                        ),
                    ),
        text= list_city_names,
        )
            ],
            'layout': go.Layout(
                title = 'Differences of temperature around Europe' ,
                titlefont={
                    'size':30
                },
                mapbox = dict(accesstoken = mapbox_access_token,
                                 bearing = 0,
                                 center = dict(lat = 48, lon = 17),
                                 pitch = 0,
                                 zoom = 3,
                                 style = 'light'),
                autosize=True,
                width=50,
                margin=go.layout.Margin(
                    l=5,
                    r=5,
                    b=0,
                    t=50,
                    pad=2
                )
            )
        }
    )
])





