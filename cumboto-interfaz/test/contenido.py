# -*- coding: utf-8 -*-
import  os, fnmatch, re
from os import path
from  datetime  import  datetime

sfc = ['*.conf','*.jpg','*.ncl']
sfc = r'|'.join([fnmatch.translate(x) for x in sfc])

def v_p():
    r_b  =  os.getcwd()
    b =  os.listdir(r_b) 
    for  d  in  b:
        if path.isdir(d):
            t  =  0
            n_f  =  0
            fmt  =  '%d­%m­%y %H:%M:%S'
            l  =  '-'  *  60
            c= os.walk(d, topdown=True) 
            for  pth, dr, f  in  c :
                print('\ndirectorio(s)       :', pth)
                f = [fc for fc in f if re.match(sfc, fc)]
		
                for fname in f:
                	print ("archivo de configuracion :", fname) 
                
                for  e  in  f:
                    n_f  +=  1
                    f   =  pth  +  os.sep  +  e
                    st  =  os.stat(f)
                    tm  =  st.st_size
                    lst =  datetime.fromtimestamp(st.st_atime)
                    mdf =  datetime.fromtimestamp(st.st_mtime)
                    lst =  lst.strftime(fmt)
                    mdf =  mdf.strftime(fmt)
                    t  +=  tm
                    print (l)
                    print('nombre       :', e)
                    print ('modificado   :', mdf)        
                    print ('último acceso:', lst)
                    print('tamaño (Kb)  :', round(tm / 1024, 1))
            print(l)
            print ('Núm. archivos:', n_f)
            print('Total (kb)   :', round(t / 1024, 1))
            print(l) 

v_p()
