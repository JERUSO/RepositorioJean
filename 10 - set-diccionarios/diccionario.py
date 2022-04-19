"""
Diccionario
Tipo de dato que almacena un conjunto de datos

un formato clave> valor

Es parecido a un array asociativo o un objeto json

"""

persona ={
    "nombre":"Edson",
    "apellidos":"Rueda",
    "web" : "edsonrueda.com"
}
print(persona["web"])

#lista con diccionarios
contactos=[
    {
        "nombre":"Edson",
        "email" : "edsonjeancarlo@gmail.com"   
    },
    {
        "nombre" : "Luis",
        "email" : "luis@luis.com"
    }
]
print(contactos)
contactos[0]["nombre"] ="Edson Jeancarlo"
print(contactos[0]["nombre"])

for contacto in contactos:
    print(f"\nNombre de contactos {contacto['nombre']}")
    print(f"\nemail de contactos {contacto['email']}") 
    print(f"+++++++++++++++++++++++++++++++++++++++++") 
     
