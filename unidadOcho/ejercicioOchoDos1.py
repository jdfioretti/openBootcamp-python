import pickle


class Vehiculo:

    tipo = ''
    precio = 0.0

    def __init__(self, tipo, precio):
        self.tipo = tipo
        self.precio = precio

    def getNombre(self):
        return self.nombre

f = open('datos.bin', 'rb')
v = pickle.load(f)
f.close()
