"""REPASAR ESTE TEMA - MODULOS - SOBRE TODO LAS IMPORTACIONES"""


#Modulos: son ficheros con extension .py si usaramos la terminal al cerrarla el codigo desapareceria
# para eso usamos modulos

from pprint import pprint


def main():
    print('Hola main')
    
if __name__ == '__main__':
    main()

#Podemos crear multiples modulos. Para importar desde otro modulo usamos "import nombre"
#debemos utilizarlo con el nombre del modulo importado . la operacion
""" ej: import operaciones
operaciones.suma() """

#Si el nombre es muy largo o queremos abreviar usamos "as"
""" import operaciones as o """

#Podemos importar modulos locales, o librerias. ej: PI, math, sys, etc.
#Al importar modulos locales no olvidar modificar ruta. Primero la importacion y luego modificacion

""" import sys
import pprint
pprint.pprint(sys.path)

sys.path.append(../../..) """   #ruta ejemplo

#los modulos se agrupan en paquetes. Es una coleccion de modulos y/o paquetes
#un paquete es un directorio, pero con un fichero especial dentro (__init__.py)
#se crea una carpeta(paquete), se crea el init, y se importa el nombre del paquete
#siempre que estemos en modulos no vamos a tener codigo de ambito global, solo fc, var y class

#ej

""" import Operaciones.suma

def main():
    mp = Operaciones.suma.Multiplicador() // 
    print(mp.multiplica(5,5))
    
if __name__ == '__main__':
    main() """

#Hay muchas formas de importar paquetes, y tener en cuenta el import as "" VER: import *
"""Podemos buscar modulos que ya se han hecho. Hay miles en la web. Casi todo ya esta hecho 
y podemos utilizarlos. Ej: paramiko(libreria por excelencia)-pypi.org-buscador"""

#podemos usar 'dir' dentro de una funcion, para saber todo lo que podemos usar con esta:

""" def main():
    tupla = ()
    pprint.print(dir()) --> click derecho sobre dir --> implementacion: nos da info-doc """

