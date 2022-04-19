"""
Variable local, se define y se usa dentro de la funcion.

variables globales, se definen fuera de la funcion y se usa dentro o fuera de la funcion.

"""

#variables globales

frase = "Ni los genios son tan Genios ni los mediocres tan mediocres."
print(frase)

def holamundo():
    frase = "Hola Mundo"
    print("dentro de la funcion")
    print(frase)

holamundo()

