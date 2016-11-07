from tornado import ioloop
import tornado.web
#import ocumare
import json
import requests
#from ocumare.lutheria import tsco

class MainHandler(tornado.web.RequestHandler):
    def get(self):
    	#url = "http://192.168.12.82/proyectos/listar.json"
    	#url2 = "http://192.168.12.64/ocumare/"
    	#lutheria = requests.get(url)
    	#lutheria = requests.get(url2)

    	#if lutheria.status_code == 200:
    		#results = lutheria.json()
    		#print(results)
    		#self.write(results)
    	#octs = lutheria.tsco('/etc/cumaco/ocumare.conf')
    	#lst = octs.obt_serv_md()
    	#opciones = ()
    	#for x in lst:
    		#opciones += (x['codigo'], x['n'])
    		#servicios = json.dumps(opciones)
    	#self.write(servicios)
    	self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
