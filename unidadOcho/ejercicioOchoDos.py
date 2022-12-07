import pickle

class Vehiculo:

    tipo = ''
    precio = 0.0

    def __init__(self, tipo, precio):
        self.tipo = tipo
        self.precio = precio

    def getNombre(self):
        return self.nombre


v1 = Vehiculo('auto', 12.5)
f = open('datos.bin', 'wb')
pickle.dump(v1, f)
f.close()