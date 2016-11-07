#-*- coding: utf-8 -*-
from os.path import exists
from sys import argv
import os
from django.core.files.base import File
from zipfile import BadZipfile, ZipFile
from zipfile import * 
import zipfile 


def clipShapesZip(zipfile):

    path = tmp
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print('Ya existe una carpeta \'%s\' en el directorio.' % (tmp))
        print('Bórrela o indique otro nombre.')
        sys.exit()

    with ZipFile(zipfile) as myzip:  # Descomprime zip
        myzip.extractall()
    