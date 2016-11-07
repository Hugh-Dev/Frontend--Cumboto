#-*- coding: utf-8 -*-
import sys
import os
import shutil
from zipfile import ZipFile


def clipShapesZip(zipfile, clipshape, dirclip):

    path = biblioteca

    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print('Ya existe una carpeta \'%s\' en el directorio.' % (dirclip))
        print('Bórrela o indique otro nombre.')
        sys.exit()

    with ZipFile(zipfile) as myzip:  # Descomprime zip
        myzip.extractall()
    zipfilefolder = zipfile[0:-4:]  # Carpeta zip
    print('Descompresión de archivos en carpeta \'%s\' \n' % (zipfilefolder))
    for shapefile in os.listdir(zipfilefolder):
        if shapefile[-4:] == ".shp":
            shapefilename = shapefile[0:-4:]
            clipshapefilename = ''
            clipshapefilename = shapefilename+'_clip.shp'
            ogrclip = 'ogr2ogr -clipsrc %s %s %s' % (clipshape, path+'/'+clipshapefilename, zipfilefolder+"/"+shapefile)
            os.system(ogrclip)  # Clip
            print("Capa %s recortada en la carpeta %s" % (
                clipshapefilename, dirclip))
    shutil.rmtree(zipfilefolder)
    print('\nElimimnación de carpeta\'%s\'' % (zipfilefolder))

if __name__ == '__main__':
    zipfile = sys.argv[1]     # Archivo ZIP
    clipshape = sys.argv[2]  # Archivo DXF de origen
    dirclip = sys.argv[3]    # Archivo GML de salida
    clipShapesZip(zipfile, clipshape, dirclip)