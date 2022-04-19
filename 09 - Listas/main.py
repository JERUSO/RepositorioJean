# listas o arrays son colecciones de datos bajo un unico nombre
# podemos usar un indice numerico 

# variable que puede contener un conjunto de datos

pelicula="Batman"

print(pelicula)

#definir lista
peliculas = ["batman","spiderman","el señor de los anillos"]
cantantes = list(("2pack","Drake","Jennifer lopez"))
years = list(range(2021,2050))
variada = ["victor",30,4.4,"texto",True]

#print(peliculas)
#print(cantantes)
#print(years)
#print(variada)
#indices de las listas

peliculas[1] = "Gran Torino"
#print(peliculas)
#print(peliculas[1])
#print(peliculas[-2])
#print(cantantes[1:3])
#print(cantantes[0:1])
#print(cantantes[0:2])
#print(peliculas[1:])

#añadir elementos a lista

cantantes.append("Kase O")
cantantes.append("Olga Tañon")

#print(cantantes)

#recorrer lista


nueva_pelicula=""
#while nueva_pelicula != "parar":
#    nueva_pelicula = input("introduce la nueva pelicula:")
#    if nueva_pelicula != "parar":
#        peliculas.append(nueva_pelicula)

#print ("\n========== listado de pelicilas =========")
#for pelicula in peliculas:
#    print(f"{peliculas.index(pelicula)} . {pelicula}")

#lista multidimensional
# lista dentro de otra lista

print("+++++++++++++ Listado de contactos ++++++++++++++++")

contactos = [
    [
        'Antonio',
        'Antonio@antonio.com'
    ],
    [ 'luis',
        'luis@luis.com'
    ],
    [
        'Salvador',
        'Salvador@salvador.com'
    ]
]

print(contactos)

for contacto in contactos:
    print(contacto[0])


for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento)== 0:
            print("Nombre:" + elemento)
        else:
            print("Email:" +elemento)



