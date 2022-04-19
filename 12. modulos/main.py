"""
modulos son funcionalidad ya hechas para reutilizar.

en python hay muchos modulos que los puedes consultar aqui

https://docs.python.org/3/py-modindex.html

"""

#importar modulo propio
import mimodulo

#from holamundo import mimodulo

print(mimodulo.holamundo("Jean"))

import datetime

print(datetime.date.today())
fecha_completa=datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada=fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print(fecha_personalizada)

import math

print("La raiz cuadrad de 10:",math.sqrt(10) )
