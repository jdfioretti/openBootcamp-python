from django.db import models


class Directores(models.Model):

    nombre = models.CharField(max_length=64, default="Nombre del director")
    apellido = models.CharField(max_length=64, default="Apellido del director")
    titulo = models.CharField(
        max_length=64, help_text="Escriba el Titulo de la pelicula aqui")
    descipcion = models.TextField(
        help_text="Escriba la descripcion de la pelicula aqui")

    def __str__(self):
        cadena = self.nombre + " " + self.apellido + ", " + "pelicula: " + \
            self.titulo + " " + ", " + "descripcion: " + " " + self.descipcion

        return cadena
