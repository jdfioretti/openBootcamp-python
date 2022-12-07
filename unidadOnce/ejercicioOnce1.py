import sqlite3

conn = sqlite3.connect('miaplicacion.db')
cursor = conn.cursor()

rows = cursor.execute('SELECT * FROM users')
for row in rows:
    print(row)

conn.commit()
cursor.close()
conn.close()
