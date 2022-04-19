#importar el modulo
import sqlite3

#conexion
conexion = sqlite3.connect('pruebas2.db')


cursor = conexion.cursor()

cursor.execute ("""
                CREATE TABLE IF NOT EXISTS productos ( 
                ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                titulo VARCHAR(255), 
                descripcion text,
                precio int(255)
                );
                """
                )

conexion.commit()

cursor.execute ("INSERT INTO productos VALUES (null, 'segundo producto','descripcion de mi producto',255)")
conexion.commit()

#leer datos de la tabla
cursor.execute("select * from productos")
productos =cursor.fetchall()

for producto in productos:
    print("Nombre: :", producto[1])
    print("Descripcion: ", producto[2])
    print("precio: ", producto[3])
    print("\n")
    


conexion.close()
