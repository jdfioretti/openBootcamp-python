import sqlite3
import getpass


def main():
    crear_usuario(4, 'pepe', 'clave1')


def main2():
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    if verifica_credenciales(username, password):
        print("Bienvenido")
    else:
        print("Usuario o contraseña incorrectos")


def verifica_credenciales(username, password):
    conn = sqlite3.connect("miaplicacion.db")
    cursor = conn.cursor()

    query = f"SELECT id FROM users WHERE username='{username}' AND password='{password}'"
    print("Query a ejecutar: ", query)

    rows = cursor.execute(query)
    data = rows.fetchone()

    cursor.close()
    conn.close()

    def crear_usuario(identificador, usuario, password):
        # isolation_level=None --> commitea automaticamente
        conn = sqlite3.connect("miaplicacion.db")
        cursor = conn.cursor()

    query = f"INSERT INTO users (id, username, password) VALUES ({identificador}, '{usuario}', '{password}')"

    rows = cursor.execute(query)
    print(type(rows))

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
