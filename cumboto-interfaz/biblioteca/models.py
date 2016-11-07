# -*- coding: utf-8 -*-
from django.db import models
from django.core.files.base import File
from biblioteca.validators import valid_extension
import os
from sys import argv
from zipfile import BadZipfile, ZipFile
import urllib2, sys, zipfile
from shutil import * 

def generate_path(instance, filename):
 	
 	folder = os.path.join("biblioteca/extraccion", filename)
 	return folder

class registrar_app(models.Model):
    cargar_app = models.FileField(
        blank=True, null=True, upload_to=generate_path,
        validators=[valid_extension])

    def __str__(self):             
        return self.cargar_app

