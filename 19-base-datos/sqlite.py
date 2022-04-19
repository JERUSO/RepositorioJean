#importar el modulo
import sqlite3

#conexion
conexion = sqlite3.connect('pruebas.db')

#crear cursos
cursor = conexion.cursor()

#crear tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo varchar (255),
        descripcion text,
        precio int(255)
        );
""")    

conexion.commit()

#insertar datos
"""
cursor.execute("INSERT INTO productos VALUES(NULL,'Primer producto','descripcion del primer producto',550)")
conexion.commit()
"""
#borrar registros
cursor.execute("DELETE FROM productos")
conexion.commit()

#insertar varios productos
productos =[
    ("Ordenador portatil","buen PC",700),
    ("telefono movil","buen telefono",140),
    ("Placa base","buena placa",80),
    ("tablet 15","buena tablet",300),
]
cursor.executemany("INSERT INTO productos VALUES(null,?,?,?)",productos)
conexion.commit()

#update
cursor.execute("Update productos set precio = 678 where precio=80")
conexion.commit()

#listar datos
cursor.execute ("select * from productos WHERE precio>=100")
productos = cursor.fetchall()
print(productos)

for producto in productos:
    print("ID:",producto[0])
    print("Titulo:",producto[1])
    print("Descripcion:",producto[2])
    print("Precio:",producto[3])
    print("\n")

cursor.execute("select titulo from productos")
producto = cursor.fetchone()
print(producto)

conexion.close()
