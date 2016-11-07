# -*- coding: utf-8 -*-

###############################################################
#   ## ## #### #######  #    ###     #  ####### ####  #####   #  
#   # # # #       #    # #   #  #   # #    #    #  #  #       #
#   #   # ###     #   #   #  #   # #   #   #    #  #  #####   #
#   #   # #       #   #####  #  #  #####   #    #  #      #   #
#   #   # ####    #   #   #  ###   #   #   #    ####  #####   #
###############################################################

import re, configparser

metadata = 'metadatos.conf'


def leerDict(diccionario, elemento):
	for i, j in elemento.items():
		diccionario = diccionario.replace(i, j)
	return diccionario
def limpieza(l):
    v = True
    while v == True:
    	try:
          c= l.index ('')
    	except ValueError:
           c = -1
           v= False
    	if c > 0:
           c = l.remove ('')   
def parsearFile(metadata):
	libreria=[]
	parserFile = open(metadata, 'r').read() 
	p = parserFile.split('\n')
	configP = configparser.RawConfigParser()
	parse = r""+metadata+""
	configP.read(parse)
	limpieza(p)
	for parsemeta  in range (len(p)):
            if parsemeta == 0:
                elementos = {'[':'',']':''}
                result = leerDict(p[0], elementos)
            if parsemeta > 0:
                indicadores = {':':'','=':''}
                dictParser = leerDict(p[parsemeta], indicadores)
                c= dictParser.split()
                e = configP.get(result, c[0])
                e = e.split()  
                libreria.append({c[0] : e[0]})
	return libreria      
md = parsearFile(metadata)
#print(md)
for conf in md:
	print (conf)
#print (parsearFile(metadata))
