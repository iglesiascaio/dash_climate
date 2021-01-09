import sys
sys.path.append('')

from temperatures_europe.load_one_file import load_one_file
from temperatures_europe.load_city_codes import load_city_codes

import pandas as pd
import numpy as np 

def create_list(D):
    '''This function creates a list of temperatures from the year 1756 to 2020. If the data is missing, we put "Nan"
    INPUT: Dictionary with the years and the values of temperature associated
    '''
    list_temp=[]
    for year in range(1756,2020):
        if str(year) in D.keys():
            list_temp.append(D[str(year)])
        else:
            list_temp.append(np.nan)
    return list_temp



def create_dataframe():
    '''    This function creates the dataframe
    OUTPUT: DataFrame with cities as rows and temperatures of the years as columns
    '''
    cities = load_city_codes()
    list_city_name = cities["city_names"]
    list_city_code = cities["city_codes"]

    #creating a Dataframe empty (with all "NaN values")...

    n = len(list_city_code)
    list_dates = list(range(1756, 2020))
    iterables = [list_city_name, list_dates]
    multi_index=pd.MultiIndex.from_product(iterables, names=['city name', 'year'])
    
    list_nan=[np.nan]*2904
    df = pd.DataFrame(list_nan, index=multi_index)
    df_unstack = df.unstack(level=-1)
    
    #putting Data in DataFrame...

    for i in range(n):
        city = list_city_code[i]
        city_name = list_city_name[i]
        filename = "../Data/ECA_indexTG/indexTG" + str(city) + ".txt"
        D = load_one_file(filename)
        list_interm=create_list(D)
        df_unstack.iloc[i]=list_interm

    return df_unstack
