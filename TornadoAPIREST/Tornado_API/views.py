# -*- coding: utf-8 -*-
###################################################################################################
#   ######## #####      ###              ###   #####  ##       #  #####  ###### ###### ########   #
#      ##    ##   ##  ##   ##          ##   ## ##   # ##      #   ##   # ##     ##        ##      #
#      ##    ##    ## #######  ######  ####### #####  ##     #    #####  ####   ######    ##      #
#      ##    ##    ## ##   ##          ##   ## ##     ##    #     ##  ## ##         ##    ##      #
#      ##    #####    ##   ##          ##   ## ##     ##   #      ##  ## ###### ######    ##      #
###################################################################################################
## @namespace Tornado_API.views
#
# Contiene las clases y los metodos de respuestas a las peticiones al SERVICE WEB
# @author Hugo Alejandro Ramirez Moreno (hramirez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
# Sistema para transmisión de aplicaciones desde las salas de control maestro de TV (CUMBOTO)
# https://cumaco.cenditel.gob.ve/desarrollo/wiki/ftransporte

from django.shortcuts import render
from tornado import ioloop
import tornado.web
import json
import requests
#import ocumare
#from ocumare.lutheria import tsco
# Create your views here.

class MainHandler(tornado.web.RequestHandler):
    def get(self):
    	#url = "http://192.168.12.82/proyectos/listar.json"
    	#url2 = "http://192.168.12.64/ocumare/"
    	#lutheria = requests.get(url)
    	#lutheria = requests.get(url)

    	"""if lutheria.status_code == 200:
    		results = lutheria.json()
    		print(results)
        octs = lutheria.tsco('/etc/cumaco/ocumare.conf')
        lst = octs.obt_serv_md()
        opciones = ()
        for x in lst:
            opciones += (x['codigo'], x['n'])
            servicios = json.dumps(opciones)
        return servicios
    		self.write(results)"""
    	#self.write(servicios)
    	self.write("Hello, world")

"""def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()"""