
#-*- coding: utf-8 -*-
import os
import zipfile
import re, configparser
from ConfigParser import ConfigParser

FilePath = str("extraccion")

scanned = 0

infected = ".zip" 

for root, dirs, files in os.walk(FilePath):
    scanned = scanned + 1
    for file in files:
        if infected in file:
            #print((root + "/" + file))
            #print("Archivos total escaneados: " + str(scanned))
            print(file)
            x = file
print "\n"

os.chdir(FilePath)


folders = []
files = []
Ids = []
types = []
names = [FilePath]
versions = []
publicKeyTokens = []

z = zipfile.ZipFile(open(x,"rb"))

for name in z.namelist():
    z.extract(name)
    if(name[-1] == "/"):
        folders.append(name)
    else:
        print "file name : ",name

z.extractall(FilePath)
os.chdir(FilePath)

for tup in os.walk(os.getcwd()):
    print "***************************************\n"
    print "directorio : ", tup[0]
    print "archivos en ",tup[0]
    filesList = tup[2]
    for i in range(len(filesList)):
                   print "archivo : ",filesList[i]
                   o = filesList[i]
                   #print(o)
    print "\n"               

#ruta del directorio
path = os.getcwd()


#Lista vacia para incluir los ficheros
lstFiles = []
 

#Lista con todos los ficheros del directorio:
lstDir = os.walk(path)   #os.walk()Lista directorios y ficheros 
 

#Crea una lista de los ficheros conf que existen en el directorio y los incluye a la lista.
for root, dirs, files in lstDir:
    for fichero in files:
        (nombreFichero, extension) = os.path.splitext(fichero)
        if(extension == ".conf"):
            lstFiles.append(nombreFichero+extension)
            z = nombreFichero+extension
            print(z)

             
print(lstFiles)            
print ('*************')
print "metadatos.conf encontrados = ", len(lstFiles)
print "\n"
print "##########metadatos##############"
#print "Ids ", Ids
#print "types ",types
#print "names ",names
#print "publicKeyTokens ",publicKeyTokens
#print "versions ",versions

#######################################################

# instancia de la clase para abrir el archivo
config = ConfigParser()
config.read(z)

# Cantidad de secciones
sections = config.sections() 
print("%d secciones:" % len(sections))

# Imprimimos cada una de ellas
for section in sections:
    print(section)