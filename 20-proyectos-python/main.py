import mysql.connector
from usuarios import acciones

print ("""
       Acciones disponibles:
            - Registro
            - Login
       """)

accion= input("Que quieres hacer ??")

hazEl = acciones.Acciones()

if accion == "registro":
   hazEl.registro()
if accion == "login":
    hazEl.login()
    
    
