def load_city_codes():
    '''This function load the city codes and name codes
    NO INPUT
    OUTPUT: dictionary D 
    {"city_codes": list of city codes,
    "city_names" = list of city names
    '''
    texte = open("../Data/city_codes.txt", "r")
    file = texte.readlines()
    D = {}
    list_tuples=[]
    city_codes = []
    city_names = []
    for lign in file:
        lign_list = lign.split()
        list_tuples.append((lign_list[1],lign_list[0]))
    list_tuples.sort()
    for i in range(len(list_tuples)):
        city_codes.append(list_tuples[i][1])
        city_names.append(list_tuples[i][0])       
    D["city_codes"] = city_codes
    D["city_names"] = city_names
    texte.close()

    return(D)


'''
This function reads a txt file to obtains the latitude and longitude of the cities
and returns the list with the latitudes, longitudes and the list of cities in the order 
that it appears in the txt file (not in alphabetical order)
'''

def load_lat_long():
    texte = open("../Data/city_codes.txt", "r")
    file = texte.readlines()
    lat = []
    long = []
    list_cities_not_ordered = []
    for lign in file:
        lign_list = lign.replace('+','').split()
        list_cities_not_ordered.append(lign_list[1])
        lign_list = lign_list[-2].split(',')
        aux_lat = lign_list[0].split(':')
        aux_long = lign_list[1].split(':')
        lat.append(aux_lat[0] + '.' + aux_lat[1] + aux_lat[2])
        long.append(aux_long[0] + '.' + aux_long[1] + aux_long[2])
        
    return lat,long,list_cities_not_ordered
    texte.close()
