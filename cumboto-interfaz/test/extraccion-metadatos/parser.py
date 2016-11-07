#Python 2.7
import re, ConfigParser

f = 'metadatos.conf'

def r_v(d, s):
	for i, j in s.iteritems():
		d = d.replace(i, j)
	return d

def f_p(f):
        lp_cfg=[]
        cfg = open(f, 'r').read() 
        p = cfg.split('\n')
        configParser = ConfigParser.RawConfigParser()
	cfp = r""+f+""
	configParser.read(cfp)
        for pmt  in range (len(p)-1):
	    if pmt == 0:
                clh = {'[':'',']':''}
                dh = r_v(p[0], clh)
            if pmt > 0:
                cl = {':':'','=':'','\\n':''}
                d = r_v(p[pmt], cl)
                c= d.split()
                e = configParser.get(dh, c[0])
                lp_cfg.append(c[0]+' : '+e)
        return lp_cfg          
         

for cf in f_p(f):
  print cf
