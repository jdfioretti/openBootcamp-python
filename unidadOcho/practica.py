# Entrada y salida - input y output

# hay 3 formas de hacerlo
# la antigua - versiones 2 - ejemplo:

import pprint
from unicodedata import name
numero = 511
texto = 'quijote'
otromas = 1.2

# el flotante puedo elegir la cantidad de digitos: %.1f
print("el numero es %d y el texto es %s y tiene %f" % (numero, texto, otromas))

# esto no se usa - es para saber que existe

# ahora la forma habitual de hacerlo hasta 3.6

print("el numero es {} y el texto es {} y tiene {}".format(
    numero, texto, otromas))  # se puede cambiar el orden

# la opcion actual, de hoy

# se puede usar f strings')
# en el texto podemos usar .upper(), como es string
print(f'El numero es {numero} y el texto es {texto.upper()} y tiene {otromas}')

# podedmos usar funciones dentro, ejemplo:


def suma(a, b):
    return a + b


print(
    f'El numero es {suma(numero, numero)} y el texto es {texto.upper()} y tiene {otromas}')

# lo ideal no es tener todo eso en un print, sino hacer una variable y luego imprimir esta: txt = (etc, etc, etc) print(txt)


def __str__(self):  # es para salidas informales - para codigo de produccion
    return f'Mi nombre es {self.nombre} y mi precio {self.precio}'


def __repr__(self):  # para salidas tecnicas - para codigo en desarrollo/depuracion
    return f'Potato {self.nombre}, {self.precio}'

# para ver los metodos que podemos usar en una cadena:


pprint.pprint(dir(''))

cadena = "en algun lugar de la manchA"
print(cadena.capitalize())  # primera letra mayuscula
print(cadena.title())  # primera letra de cada palabra mayuscula
print(cadena.count('a'))  # cuantas veces aparece la letra
print(cadena.lower().count('a'))

numero = '5'
print(numero.isnumeric())
print(numero.isdigit())

print(cadena.strip())  # quita espacios
print(cadena.lstrip())  # quita espacios de la izquierda
print(cadena.rstrip())  # quita espacios de la derecha

print(cadena.split())  # separa por espacios

# https://www.w3schools.com/python/python_ref_string.asp todos los metodos de string


#######################################################################################

# guardar en un fichero o leer de un fichero - Todo empieza con un "open"

f = open('/etc/passwd', 'r')

# r = read
# a = append
# w = write
# x = create

# t = text
# b = binary

# + plus - se agrega a alguna de las letas anteriores para permitir algo mas

# como leer un fichero

f = open('/etc/passwd', 'r')
datos = f.read()  # --> podemos poner el nro de caracteres a leer --> datos = f.read(17) ojo con el \n es 1 mas
f.close()

print(datos)

datos = f.readline()  # --> lee la primera linea
datos = f.readlines()  # --> lee linea a linea y lo muestra en una lista

########
