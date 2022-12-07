import sqlite3

conn = sqlite3.connect('miaplicacion.db')
cursor = conn.cursor()

rows = cursor.execute('SELECT * FROM users') #selecciona todos los registros
#rows = cursor.execute('SELECT * FROM users WHERE username="javier"') # para seleccionar uno
for row in rows:
    print(row)

cursor.close()
conn.close()
