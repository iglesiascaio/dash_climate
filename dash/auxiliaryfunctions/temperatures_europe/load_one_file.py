def load_one_file(filename):
    ''' Returns a dictionary with the years and the values of temperature associated
    INPUT: filename
    OUTPUT: {year1: temp1, year2: temp2,  ...}
    '''
    texte = open(filename, "r")
    file = texte.readlines()
    file = file[30:]
    D = {}
    for lign in file:
        lign_list = lign.split()
        utile = lign_list[1:3]
        if utile[1]!='-999999':
            D[utile[0]]=int(utile[1])/100
    return(D)

