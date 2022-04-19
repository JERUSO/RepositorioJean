import mysql.connector

database = mysql.connector.connect(
    host= "localhost",
    user="root",
    passwd="",
    database= "master_python"
)

cursor = database.cursor(buffered=True)
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

"""
cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
"""
cursor.execute ("""
                CREATE TABLE IF NOT EXISTS vehiculos(
                    id int(10) auto_increment not null,
                    marca varchar(150) not null,
                    modelo varchar(200) not null,
                    precio float (10,2) not null,
                    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
                                      )
                """)

cursor.execute ("SHOW TABLES")

for table in cursor:
    print(table)
    
#cursor.execute("INSERT INTO vehiculos VALUES(null,'nissan','almera',5500)")

COCHES = [
    ('seat','Ibiza',5000),
    ('Renault','Clio',2500),
    ('citroen','Saxo',3000),
    ('TOYOTA','corola',5500)
]

#cursor.executemany ("INSERT INTO vehiculos VALUES (null,%s,%s,%s)",COCHES)

database.commit()

cursor.execute("SELECT * FROM vehiculos WHERE precio <=5000 AND marca='seat'")

resultado = cursor.fetchall()
print ("---- Todos mis coches---------") 
for coche in resultado:
    print(coche[1],coche[3])


cursor.execute("SELECT * FROM vehiculos")

coche = cursor.fetchone()
print(coche)

cursor.execute("DELETE FROM vehiculos where marca='renault'")

database.commit()


