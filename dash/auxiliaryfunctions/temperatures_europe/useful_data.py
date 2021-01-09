import sys
sys.path.append('')

from temperatures_europe.load_city_codes import load_city_codes
from temperatures_europe.load_one_file import load_one_file
import pandas as pd
import numpy as np 

def find_useful_data():
    '''
    This function calculates the difference of temperatures betweeen the years 1966 and 2000,
    that was the interval of years we could find data for all cities. It's used in the map of 
    the difference of temperatures. It returns a list of the difference of temperatures and 
    the list of the cities ordered. 
    '''

    cities = load_city_codes()
    list_city_code = cities["city_codes"]
    list_city_names = cities['city_names']
    n=len(list_city_code)
    diff=[]
    for i in range(n):
        city = list_city_code[i]
        filename = "../Data/ECA_indexTG/indexTG" + str(city) + ".txt"
        D=load_one_file(filename)
        diff.append(D['2000'] - D['1966'])

    return diff, list_city_names

