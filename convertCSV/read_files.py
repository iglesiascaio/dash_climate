import csv
import pandas as pd
import glob
import os

#reads a file in csv and transforms into a dataframe
def read_csv(filename):
    dataframe = pd.read_csv(filename, delimiter=';')
    return dataframe

#take all the csv files and generate a dict of the dataframes
def all_dataframes_generator():
    path = '../Data/'
    filenames = glob.glob(path + "*.csv")

    dataframe_collection = {}
    for file in filenames:
        name = (os.path.basename(file).split('.'))
        dataframe_collection[name[0]] = pd.DataFrame(read_csv(file))

    return dataframe_collection
