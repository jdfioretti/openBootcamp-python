import pickle  # -->es para serializar: convertir una representacion de un
# programa a una secuencia de datos que podemos escribir en un fichero.


class Juguete:

    nombre = ''
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def getNombre(self):
        return self.nombre


""" j1 = Juguete('Potato', 10.5)
f = open('datos.bin', 'wb')
pickle.dump(j1, f)
f.close() """

f = open('datos.bin', 'wb')  # --> para recuperar el fichero .bin
potato = pickle.load(f)
f.close()

# los datos los serializamos para guardar el estado de un programa


class Estado:
    players = Players()
    status = Status()
    life_remaining = 12
    armor = False


f = open('gamestatus.dat', 'wb') # --> para guardar los datos de un juego
e = Estado()
pickle.dump(f, e)
f.close()

f = open('gamestatus.dat', 'rb') # --> para recuperar los datos de un juego
e = pickle.load(f)
f.close()



# ver pygame

