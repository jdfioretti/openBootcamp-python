class Vehiculo:
    color = "gris"
    ruedas = 4
    puertas = 5


class Coche(Vehiculo):
    velocidad = 120
    cilindrada = 1000


c = Coche()
print(c.velocidad)
print(c.cilindrada)
