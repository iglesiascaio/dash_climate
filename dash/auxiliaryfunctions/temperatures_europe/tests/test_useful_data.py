import sys
sys.path.append('')

from temperatures_europe.load_city_codes import load_city_codes
from temperatures_europe.load_one_file import load_one_file
from temperatures_europe.useful_data import find_useful_data


def test_load_city_codes():
    # When
    annotations = find_useful_data()
    #Then
    assert annotations == ([1.450000000000001, 0.6900000000000013, 0.5, 0.8099999999999987, 1.3600000000000003, 1.0, 0.3100000000000005, 0.629999999999999, 2.66, -0.7699999999999996, 1.620000000000001], ['BERLIN-DAHLEM', 'CORFU', 'KIEV', 'MADRID', 'MOSCOW', 'PARIS', 'ROMA', 'SHAWBURY', 'STOCKHOLM', 'VAN', 'WIEN'])

print(test_load_city_codes())