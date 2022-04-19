#funciones predefenidas en listas

cantantes =["2pac","Drake","Bad Bunny","Julio Iglesias"]

numeros = [1,2,5,8,3,4]

#ordenar la listas

print(numeros)
numeros.sort()
print(numeros)

#añadir elementos
#cantantes.append("Juan Manuel")
#print(cantantes)
#cantantes.insert(1,"David Bisbal")
#print(cantantes)

#eliminar elementos de una lista
#cantantes.pop(1)
#cantantes.remove("Bad Bunny")
#print(cantantes)

#dar la vuelta de lista
#print(numeros)
numeros.reverse()
#print(numeros)

#buscar dentro de una lista
print("Drake" in cantantes)

print(cantantes)
print(len(cantantes))

#cuantas veces aparece en una lista
print(numeros.count(8))

#conseguir indice
print(cantantes.index("Drake"))

#Unir listas
cantantes.extend(numeros)
print(cantantes)