import sys
sys.path.append('')

from convertCSV.read_files import read_csv
from convertCSV.read_files import all_dataframes_generator


def test_load_city_codes():
    # When
    annotations1 = read_csv('Data/observation-meteorologique-historiques-france-synop-orly.csv')
    annotations2 = all_dataframes_generator()
    #Then
    assert len(annotations1) == 28373
    assert len(annotations2) == 1

print(test_load_city_codes())