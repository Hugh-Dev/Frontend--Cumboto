# -*- coding: utf-8 -*-
###################################################################################################
#   ######## #####      ###              ###   #####  ##       #  #####  ###### ###### ########   #
#      ##    ##   ##  ##   ##          ##   ## ##   # ##      #   ##   # ##     ##        ##      #
#      ##    ##    ## #######  ######  ####### #####  ##     #    #####  ####   ######    ##      #
#      ##    ##    ## ##   ##          ##   ## ##     ##    #     ##  ## ##         ##    ##      #
#      ##    #####    ##   ##          ##   ## ##     ##   #      ##  ## ###### ######    ##      #
###################################################################################################
## @namespace Tornado_API.urls
#
# Contiene las urls del servicio web
# @author Hugo Alejandro Ramirez Moreno (hramirez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>

from django.conf.urls import url
from .views import MainHandler

urlpatterns = [
    url(r'^', MainHandler ,name="list"),
    #url(r'^$', .as_view()) ,name=""),
]