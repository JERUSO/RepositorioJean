""""
#programa con lista de numeros enteros

hacer un programa que tenga una lista de 8 numeros y hacer:
recoerer la lista y mostrarla
hacer funcion que recorra listas de numeros
ordenarla y mostrarla
mostar su longitud
buscar algun elemento.

"""
import mimodulo3



def mostrarlista(lista1):
    resultado = ""
    for elemento in lista1:
        resultado += "Elemento :" + str(elemento)
        resultado +="\n"
    return numero


#crear la lista
numeros=[13,54,67,72,12,7,21,58,63]

#recorrer y mostrar
for numero in numeros:
    print(numero);

print(mostrarlista(numeros))

numeros.sort()
print(numeros)

print(len(numeros))

#busqueda en la lista
busqueda = int(input("Introduce el numero:"))
comprobar = isinstance(busqueda,int);

while not comprobar or busqueda <=0:
    busqueda = int(input("Introduce el numero:"))
else:
    print(f"haz introducido")
