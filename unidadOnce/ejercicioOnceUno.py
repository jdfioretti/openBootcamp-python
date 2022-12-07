import sqlite3


def crear_tabla():
    conn = sqlite3.connect("alumnos.db")
    conn.commit()
    conn.close()


def insertar_tabla():
    conn = sqlite3.connect("alumnos.db")
    cursor = conn.cursor()
    instruccion = (
        """ CREATE TABLE alumnos(
            id integer,
            nombre text,
            apellido text
        ) """
    )
    
    cursor.execute(instruccion)
    conn.commit()
    conn.close()


def insertalumnos(list):
    conn = sqlite3.connect("alumnos.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO alumnos VALUES (?,?,?)"
    cursor.executemany(instruccion, list)
    conn.commit()
    conn.close()


def search():
    conn = sqlite3.connect("alumnos.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM alumnos WHERE nombre='javier'"
    cursor.execute(instruccion)
    dato = cursor.fetchall()
    conn.commit()
    conn.close()
    print(dato)


lista = [(1, 'juan', 'perez'),
         (2, 'jose', 'sanchez'),
         (3, 'javier', 'rodriguez'),
         (4, 'francisco', 'lopez'),
         (5, 'miguel', 'rios'),
         (6, 'juana', 'loca'),
         (7, 'pedro', 'pica'),
         (8, 'luis', 'castro')]


if __name__ == "__main__":
    search()
