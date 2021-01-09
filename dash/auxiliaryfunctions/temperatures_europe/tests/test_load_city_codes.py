import sys
sys.path.append('')

from temperatures_europe.load_city_codes import load_city_codes
from temperatures_europe.load_city_codes import load_lat_long
from temperatures_europe.load_one_file import load_one_file


def test_load_city_codes():
    # When
    annotations1 = load_city_codes()
    annotations2 = load_lat_long()
    #Then
    assert annotations1 == {'city_codes': ['000041', '000059', '000252', '000230', '000087', '000038', '000176', '001633', '000010', '001439', '000016'], 'city_names': ['BERLIN-DAHLEM', 'CORFU', 'KIEV', 'MADRID', 'MOSCOW', 'PARIS', 'ROMA', 'SHAWBURY', 'STOCKHOLM', 'VAN', 'WIEN']}
    assert annotations2 == (['59.2100', '48.1359', '48.4918', '40.2442', '52.2750', '39.3700', '55.4959', '41.4659', '52.4800', '38.2700', '50.2400'], ['018.0300', '016.2100', '002.2016', '-003.4041', '013.1806', '019.5500', '037.3700', '012.3459', '-002.4012', '043.1912', '030.3159'], ['STOCKHOLM', 'WIEN', 'PARIS', 'MADRID', 'BERLIN-DAHLEM', 'CORFU', 'MOSCOW', 'ROMA', 'SHAWBURY', 'VAN', 'KIEV'])


print(test_load_city_codes())