class Alumno:
    nombre = "Javier"
    nota = 7


def aprueba():
    Alumno.aprobado = True


def reprueba():
    Alumno.reprobado = False


a = Alumno()

if Alumno.nota >= 7:
    print(a.nombre, "tiene un:", a.nota, ", está aprobado")
    
else:
    print(a.nombre, "tiene un:", a.nota, ", está reprobado")
