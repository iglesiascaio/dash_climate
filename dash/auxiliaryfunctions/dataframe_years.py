import sys
sys.path.append('../')
from convertCSV.read_files import all_dataframes_generator 
import dateutil.parser
import datetime as dt
import pandas as pd
import datapackage
import numpy as np

""" 
reads a csv file and return a dict with the years as keys and items as lists of 
the values of each month, for the respective year 
""" 

def separate_means_years():
    
    #parameters 
    initial_year = 2010
    final_year = 2019

    df_all_years = all_dataframes_generator()["observation-meteorologique-historiques-france-synop-orly"]
    df_all_years['Date'] = pd.to_datetime(df_all_years['Date'], utc = True)

    dict_year = {}

    for year in range (initial_year, final_year+1):

        data_year = df_all_years[df_all_years['Date'].dt.year == year]
        
        
        data_months = []
        for month in range (1,13):
            data_month = data_year[data_year['Date'].dt.month == month]
            data_months.append(data_month['Température (°C)'].mean())
    
        dict_year[year] = data_months

    return dict_year

         

'''
get the data from datahub.io, selects the data from all the years after 1980, choose the
base years as 1951-1980, using the source GISTEMP. After that, it merges the tow data into
one dataframe and it separates the years in groups, in order to facilitate the visualization.
A column group is also added to facilitate the graph plotting
'''
def get_data_co2_temp():

    data_url = 'https://datahub.io/core/global-temp/datapackage.json'

    # to load Data Package into storage
    package = datapackage.Package(data_url)

    # to load only tabular data
    resources = package.resources
    data_temperature = []

    for resource in resources:
        if resource.tabular:
            data = pd.read_csv(resource.descriptor['path'])
            data_temperature.append(data)

    data_temperature_annual = data_temperature[0]
    data_temperature_annual = data_temperature_annual[data_temperature_annual['Year']>= 1980]
    data_temperature_annual = data_temperature_annual.sort_values(by= ['Year'])
    data_temperature_annual = data_temperature_annual[data_temperature_annual['Source'] == 'GISTEMP']
    

    #get data co2
    data_url = 'https://datahub.io/core/co2-ppm/datapackage.json'

    # to load Data Package into storage
    package = datapackage.Package(data_url)

    # to load only tabular data
    resources = package.resources
    data_co2 = []
    for resource in resources:
        if resource.tabular:
            data = pd.read_csv(resource.descriptor['path'])
            data_co2.append(data)

    data_co2_annual = data_co2[-2]
    data_co2_annual = data_co2_annual[data_co2_annual['Year'] < 2017]


    data_annual_gistemp = data_co2_annual.rename(columns = {'Mean': 'CO2'})
    data_annual_gistemp = pd.merge(data_annual_gistemp, data_temperature_annual, on = 'Year').rename(columns = {'Mean': 'Temperature'})
    data_annual_gistemp['Group'] = 0
    i = 1
    for year in range (1980,2016,6):
        if year != 2010:
            data_annual_gistemp.loc[(data_annual_gistemp['Year']>=year) & (data_annual_gistemp['Year']<= (year+5)),'Group'] = str(year) + '-' + str (year+5)
        else:
            data_annual_gistemp.loc[(data_annual_gistemp['Year']>=year) & (data_annual_gistemp['Year']<= (year+6)),'Group'] = str(year) + '-' + str(year+6)
        i += 1
    return data_annual_gistemp


'''
reads a csv file, passes the data to a datatime and, then, for each year, adds the mean of the 
values of a certain meteo parameter into a list. The function then returns lists with the mean values
of temperature, humidity, precipitation and pression and also a list of the years used

'''
def separate_data_meteo():

    initial_year = 2010
    final_year = 2019

    df_all_years = all_dataframes_generator()["observation-meteorologique-historiques-france-synop-orly"]
    df_all_years['Date'] = pd.to_datetime(df_all_years['Date'], utc = True)


    dict_year = {}
    data_temperature = []
    data_pression = []
    data_precipitation = []
    data_humidity = []
    years = np.arange(initial_year,final_year+1)

    for year in range (initial_year, final_year+1):

        data_year = df_all_years[df_all_years['Date'].dt.year == year]
        data_temperature.append(data_year['Température (°C)'].mean())
        data_pression.append(data_year['Pression au niveau mer'].mean())
        data_precipitation.append(data_year['Précipitations dans les 24 dernières heures'].mean())
        data_humidity.append(data_year['Humidité'].mean())
        

    return data_temperature,data_pression,data_precipitation,data_humidity,years
