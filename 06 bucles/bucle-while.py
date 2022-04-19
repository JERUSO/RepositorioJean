#ejemplo bucle while
"""
Estructura de control
#Itera o repite la ejecución de una serie de instrucciones tantas veces como sea necesario
# hasta que se deje de cumplir la condicion
aqui se controla el contador para que al final la condicion termine.

contador 
while (condicion):
    bloque de instrucciones
    actualizacion del contador

"""

#ejemplo01
print("---------------------------------------")
contador = 1
muestrame = str(0)
while contador<=100:
    muestrame = muestrame + "," + str(contador)
    contador = contador + 1
print(muestrame)

#ejemplo
print("######## ejemplo ############")
numero_usuario = int(input("de que numero quieres la tabla ??"))

contador = 1
while contador <=10:
    print(f"{numero_usuario} x {contador} = {numero_usuario*contador} ")
    contador = contador+1
else:
    print ("\n###### tabla terminada #######")
