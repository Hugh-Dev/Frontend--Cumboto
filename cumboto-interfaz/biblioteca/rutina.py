#! /usr/bin/python
import os
import sys
def rmsvn(arg, dirname, names):
    if dirname.endswith(arg):
        print "Borrando directorio %s" % dirname
        """Puede no estar vacio, por tanto borramos hacia
        dentro recursivamente
        """
        for root, dirs, files in os.walk(dirname, topdown=False):
            # borramos los archivos
            for name in files:
                os.remove(os.path.join(root,name))
            # borramos los subdirectorios
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        # ahora podemos borrar el directorio
        os.rmdir(dirname)
if __name__ == "__main__":
    os.path.walk(sys.argv[1],rmsvn, sys.argv[2])