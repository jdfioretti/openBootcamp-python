# POO - Clases y objetos

#representan cosas de la vida real. Tienen metodos, que son acciones que realizamos. 
# Son funciones dentro de la clase.
# Tienen propiedades, que pueden mutar. son las variables dentro de la clase. 

from abc import abstractmethod


class Dino:
    encendido = True
    
    def apaga(self):
        apagado = False
        
d = Dino()                          #intanciar una clase-Creo una var y la igualo al nombre de la clase
                                    #podemos usar los metodos de esa clase
d.apaga()                           #podemos usar las props, metodos, etc. Tambien cambiar/sobreescribir los valores
print(d.encendido)

d1 = Dino()
d1.apaga()
print(d1.encendido)
        

#por convencion si un metodo comienza por "_" o valor de la clase, no debemos modificarlo. 
# _encendido
# para hacer referencia a una variable de mi clase, debemos agregar "self." self.encendido


#Clase estatica. No es muy comun usarlas. Comparten un mismo espacio de memoria, no se instancian como las dinamicas

class Estatica:
    numero = 1
    
    def incrementa():
        Estatica.numero += 1
        
Estatica.incrementa()
print(Estatica.numero)

Estatica.incrementa()
print(Estatica.numero)

# Para cambiar una propiedad usar el nombre de su clase, punto su propiedad. No puede haber multiples instancias 
# se pueden usar como numeradores, o placeholders

#Las clases tienen HERENCIA: consiste en que una clase hereda los metodos y propiedades de otra y las utiliza
#Con herencia creamos una clase base con los metodos y propiedades comunes, y luego hacemos clases derivadas
#que implementen la funcionalidad especial de esas clases - Hay herencias multiples. Aconseja no utiliarlas 
""" d = Dino()
print(Dino(d)) """ #nos muestra todas las funciones, la herencia

#constructor: una clase se construye cuando la instanciamos. Se crea usando la fc reservada __init__

""" class Dino(Juguete)
def __init__(self): """

#destructor. Se usa para desalojar memoria. No es necesario en python, ya que hay un recolector de basura

""" def __del__(self): """

# se ejecuta al terminar el programa, cuando nada mas usa la variable. Se puede forzar el uso del destructor

""" del(d) elimina la var "d" """

#las clases en python son diccionarios. Se usa como azucar sintactico, ya que es mas simple y limpio

#---------------------------------------
#Clases - Abstractas y no. No tienen diferencias, solo diferentes cometidos

#debemos importar: form abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod             #cuando usamos este metodo las demas clases deben definir el metodo que hay debajo, si o si 
    def sonido(self):
        pass
    
#las clases abst. no se pueden instanciar
#sirve para definir un conjunto de funciones comunes a otra clase

class Perro(Animal):
    def sonido(self):
        print("guau")
        
class Gato(Animal):
    def sonido(self):
        print("miau")
        
p = Perro()
p.sonido()

p = Gato()
p.sonido()

#Composicion: una clase esta compuesta de otras clases. Tiene una o mas instancias de otra clase. No hereda funciones.



    