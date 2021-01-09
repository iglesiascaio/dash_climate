import os
import pathlib
import numpy as np
import datetime as dt
import dash
import dash_core_components as dcc
import dash_html_components as html

import sys
sys.path.insert(1, 'components/')
# import callback functions and other elements from each graph
from dash.dependencies import Input, Output, State
from graph_temp_france import graph_temp_france_layout
from graph_cities_eu import graph_cities_eu_layout, temp_values
from graph_co2_temp import graph_co2_temp_layout, corr
from map_diff_temp import map_diff_temp_layout
from map_co2 import map_co2_layout
from graph_co2_pie import graph_co2_pie_layout, df_1965, df_1995, df_2005, df_2017, labels
from graph_meteo_france import graph_meteo_france_layout, data_temperature,data_pression,data_precipitation,data_humidity,years
import plotly.graph_objs as go

sys.path.insert(1, 'auxiliaryfunctions/')
from dataframe_years import separate_means_years

'''
This file builds the final page, with all the graphs made. It contains also the appcallbacks, 
that are essential to the interactive functionality of the graphics. It uses a stylesheet, where
the classes used are defined. 
'''

external_stylesheets = ['stylesheet.css']
GRAPH_INTERVAL = os.environ.get("GRAPH_INTERVAL", 5000)

app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    external_stylesheets=external_stylesheets
)

server = app.server
dict_years = separate_means_years()
app_color = {"graph_bg": "#FFFFFF", "graph_line": "#007ACE", "graph_text": "#000000"}


# placement of the components of the page
# and setting of their style
app.layout = html.Div(
    [
        # header
        html.Div(
            [
                html.Div(
                    [
                        html.H1("Évolution météorologique en France et dans le Monde", className="app__header__title"),
                        html.P(
                            "Using data from Open Data Paris-Saclay, DataHub, CDIAC and other government fonts, about the temperature in France and in cities around the world, we were able to analyze patterns and tendencies related to the past years",
                            style={
                                'fontSize': 20
                            },
                            className="app__header__title--grey",
                        ),
                    ],
                    className="app__header__desc",
                ),
                html.Div(
                    [
                        html.Img(
                            src=app.get_asset_url("1200px-Logo_CentraleSupélec.png"),
                            style={
                                'width': '10%',
                                'height': '10%',
                                'position': 'absolute',
                                'right': '0',
                                'top': '0',
                            },
                            className="app__menu__img",
                        )
                    ],
                    className="app__header__logo",
                ),
            ],
            className="app__header",
        ),

        #graphs
        html.Div(
            [
                html.Div([
                    html.Div([
                        html.Div([
                            graph_co2_temp_layout
                        ],
                        )
                    ],
                    style = {
                        'position': 'relative',
                        'top': '20px',
                        'height': '700px',
                    },
                    className="graph-co2-temp column pretty_container",
                    ),

                    html.Div([
                        html.Div([
                            map_co2_layout
                        ],
                        style = {
                            'position': 'relative',
                            'top': '20px',
                            'height': '280px',
                        },
                        className="row pretty_container first",
                        ),

                        html.Div([
                            graph_co2_pie_layout
                        ],
                        style = {
                            'position': 'relative',
                            'top': '40px',
                            'height': '390px',
                        },
                        className="row pretty_container second",
                        ),
                    ],
                    className="graphs-co2 column",
                    ),
                ],
                style={
                    'position': 'relative',
                    'right': '20px',
                    'left': '20px'
                },
                className="row"
                ),

                html.Div([
                    html.Div([
                        graph_cities_eu_layout
                    ],
                    style = {
                        'position': 'relative',
                        'top': '20px',
                        'height': '500px'
                    },
                    className="graphs-co2 column pretty_container first"
                    ),

                    html.Div([
                        map_diff_temp_layout
                    ],
                    style = {
                        'position': 'relative',
                        'top': '20px',
                        'height': '500px'
                    },
                    className="graph-co2-temp column pretty_container second"
                    )
                ],
                style={
                    'position': 'relative',
                    'top': '40px',
                    'right': '20px',
                    'left': '20px'
                },
                className="row"
                ),

                html.Div([
                    html.Div([
                        graph_meteo_france_layout
                    ],
                    className="graph-france column pretty_container first"
                    ),
                    html.Div([
                        graph_temp_france_layout
                    ],
                    className="graph-france column pretty_container second"
                    ),
                ],
                style={
                    'position': 'relative',
                    'top': '80px',
                },
                className="row"
                ),
            ],
            className="app__content",
        ),
    ],
    className="app__container",
)

# --- callback functions ---
# depend on variable parameters the user can set as she wants
# the output (graph) will change according to these parameters

# callback function of graph_temp_france
@app.callback(
    Output('graph', 'figure'), [Input('my-dropdown', 'value')]
)
def show_temp_france(value):
    y_array_dict = {
        '2010': dict_years[2010],
        '2011': dict_years[2011],
        '2012': dict_years[2012],
        '2013': dict_years[2013],
        '2014': dict_years[2014],
        '2015': dict_years[2015],
        '2016': dict_years[2016],
        '2017': dict_years[2017],
        '2018': dict_years[2018],
        '2019': dict_years[2019]
    }
    data = {
        'data': [],
        'layout': dict(
            title='Temperature in France X Months',
            titlefont={
                'size':'25'
            },
            height='500px',
            plot_bgcolor=app_color["graph_bg"],
            paper_bgcolor=app_color["graph_bg"],
            font={"color": "graph_text", "size":"15"},
            autosize=True,
            bargap=0.01,
            bargroupgap=0,
            hovermode="closest",
            legend={
                "orientation": "h",
                "yanchor": "bottom",
                "xanchor": "center",
                "y": 1,
                "x": 0.5,
            },
            xaxis={'title': 'Months', 'titlefont':{'size':20}},
            yaxis={'title': 'Temperature(°C)', 'titlefont':{'size':20}},
        )                 
    }
    for element in value:
        data['data'].append({'type':'scatter', 'x': ['Jan','Feb','Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov', 'Dec'],'y':y_array_dict[element],'name':element})
    return data
    
# callback function of graph_cities_eu
@app.callback(
    Output('graph-graph_cities_eu', 'figure'), [Input('my-dropdown-graph_cities_eu', 'value')]
)
def show_cities_eu(value):
    
    x_array_dict  = {
        'BERLIN-DAHLEM': temp_values(0)['x'],
        'CORFU': temp_values(1)['x'],
        'KIEV': temp_values(2)['x'],
        'MADRID': temp_values(3)['x'],
        'MOSCOW': temp_values(4)['x'],
        'PARIS': temp_values(5)['x'],
        'ROMA': temp_values(6)['x'],
        'SHAWBURY': temp_values(7)['x'],
        'STOCKHOLM': temp_values(8)['x'],
        'VAN': temp_values(9)['x'],
        'WIEN': temp_values(10)['x']
    }


    y_array_dict  = {
        'BERLIN-DAHLEM': temp_values(0)['y'],
        'CORFU': temp_values(1)['y'],
        'KIEV': temp_values(2)['y'],
        'MADRID': temp_values(3)['y'],
        'MOSCOW': temp_values(4)['y'],
        'PARIS': temp_values(5)['y'],
        'ROMA': temp_values(6)['y'],
        'SHAWBURY': temp_values(7)['y'],
        'STOCKHOLM': temp_values(8)['y'],
        'VAN': temp_values(9)['y'],
        'WIEN': temp_values(10)['y']
    }

    
    

    data = {
        'data': [],
        'layout': dict(
            title= 'Temperature X Years for Cities in Europe ',
            titlefont={
                'size':'25'
            },
            xaxis={'title': 'Years', 'titlefont':{'size':20}},
            yaxis={'title': 'Temperature(°C)', 'titlefont':{'size':20}},
            height='400px',
            plot_bgcolor=app_color["graph_bg"],
            paper_bgcolor=app_color["graph_bg"],
            font={"color": "graph_text", "size":"15"},
            autosize=True,
            bargap=0.01,
            bargroupgap=0,
            hovermode="closest",
            legend={
                "orientation": "h",
                "yanchor": "bottom",
                "xanchor": "center",
                "y": 1,
                "x": 0.5,
            },
        )
    }
    for element in value:
        data['data'].append({'type':'scatter','x':x_array_dict[element],'y':y_array_dict[element],'name': element})
        

    return data

# callback function on graph_meteo_france
@app.callback(
    [Output('graph-graph_meteo_france', 'figure'),
    Output('my-dropdown-graph_meteo_france','options')],
    [Input('my-dropdown-graph_meteo_france', 'value')])

def show_meteo_france(value):
    y_array_dict = {
        'Temperature': data_temperature,
        'Pression': data_pression,
        'Precipitation': data_precipitation,
        'Humidity': data_humidity 
    }

    data = {
        'data': [],
        'layout': {
            'title': 'France weather Charts' ,
            'xaxis':{
                'title':'Years'
            },
        }
    }
    
    for element in value:
        if value.index(element)==0:
            data['data'].append(go.Scatter(
                x= years,
                y=y_array_dict[element],
                name=element
            ))
        elif value.index(element)==1:
            data['data'].append(go.Scatter(
                x= years,
                y=y_array_dict[element],
                name=element,
                yaxis='y2'
            ))
        else:
            continue
    
    def define_title():
        if len(value)==0:
            return 'Please select one or two graphics to plot'
        elif len(value)==2:
            return 'Graph of ' + value[0] + ' and ' + value[1] + ' over the years'
        elif len(value) == 1:
            return 'Graph of ' + value[0] + ' over the years'
        
            

    data['layout'] = go.Layout(
    title= define_title(),
    titlefont={
        'size':25
    },
    xaxis=dict(
        title='Years',
        titlefont={
            'size':20
        }
    ),
    yaxis=dict(
        title= value[0] if len(value)>0 else '',
        titlefont=dict(
            size=20
        ),
    ),
    yaxis2=dict(
        title= value[1] if len(value) == 2 else '',
        titlefont=dict(
            size=20
        ),
        tickfont=dict(
            size=15
        ),
        overlaying='y',
        side='right'
    )
    )

    options=[
        {'label': 'Temperature', 'value': 'Temperature'},
        {'label': 'Pression', 'value': 'Pression'},
        {'label': 'Precipitation', 'value': 'Precipitation'},
        {'label': 'Humidity', 'value': 'Humidity'},
    ]

    for element in options:
        if len(value)<2:
            element['disabled'] = False
        elif len(value) == 2 and element['label'] not in value:
            element['disabled'] = True
        elif len(value) == 2 and element['label']  in value:
            element['disabled'] = False
        elif len(value) > 2 and element['label'] not in value :
            element['disabled'] = True

    return data, options

# callback function of graph_co2_pie
@app.callback(
    Output('graph-graph_co2_pie', 'figure'),
    [Input('my-dropdown-graph_co2_pie', 'value')])

def show_co2_pie(value):
    y_array_dict = {
        '2017': df_2017,
        '2005': df_2005,
        '1995': df_1995,
        '1965': df_1965,      
    }

    data = {
        'data': [go.Pie(labels=labels,
                values=y_array_dict[value])],
        'layout': go.Layout(
            title='CO2 Emissions around the World per Year',
            titlefont={
                'size':25
            },
            margin=go.layout.Margin(
                l=5,
                r=5,
                b=0,
                t=50,
                pad=2
            )
        )
    }
    
    return data

# main
if __name__ == "__main__":
    app.run_server(debug=True)
