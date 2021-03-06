import sys
sys.path.append('')

from temperatures_europe.load_one_file import load_one_file


def test_load_one_file():
    filename = "../Data/ECA_indexTG/indexTG000007.txt"
    # When
    annotations = load_one_file(filename)
    #Then
    assert annotations == {'1950': 6.39, '1951': 5.96, '1952': 4.85, '1953': 6.98, '1954': 5.61, '1955': 5.25, '1956': 4.35, '1957': 5.86, '1958': 5.03, '1959': 6.72, '1960': 5.55, '1961': 6.86, '1962': 4.82, '1963': 4.62, '1964': 5.93, '1965': 4.98, '1966': 4.79, '1967': 6.25, '1968': 5.12, '1969': 5.52, '1970': 4.59, '1971': 6.34, '1972': 6.48, '1973': 6.32, '1974': 7.25, '1975': 7.87, '1976': 5.74, '1977': 5.79, '1978': 5.38, '1979': 4.65, '1980': 5.12, '1981': 5.07, '1982': 6.36, '1983': 6.92, '1984': 6.56, '1985': 3.62, '1986': 4.98, '1987': 3.53, '1988': 6.05, '1989': 7.45, '1990': 7.59, '1991': 6.71, '1992': 7.3, '1993': 5.81, '1994': 6.56, '1995': 6.04, '1996': 5.34, '1997': 6.88, '1998': 5.86, '1999': 6.38, '2000': 7.33, '2001': 5.83, '2002': 6.6, '2003': 6.23, '2004': 6.4, '2005': 6.66, '2006': 7.01, '2007': 6.83, '2008': 7.3, '2009': 6.15, '2010': 3.94, '2011': 7.08, '2012': 5.95, '2013': 6.21, '2014': 7.67, '2015': 7.37, '2016': 6.89, '2017': 6.74, '2018': 7.29}


print(test_load_one_file())