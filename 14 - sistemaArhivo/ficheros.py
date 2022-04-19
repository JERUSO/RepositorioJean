import io
import pathlib
import shutil

#abrir archivo
#ruta = str(pathlib.Path().absolute()) + "/ficherotexto.txt"
#archivo = io.open(ruta,"a+")
#print(ruta)
#archivo.write("Soy un texto metido en python\n")
#archivo.close()


#abrir archivo
"""
ruta = str(pathlib.Path().absolute()) + "/ficherotexto.txt"
archivo_lectura = io.open(ruta,"r")
"""
#contenido=archivo_lectura.read()
#print(contenido)
#for elemento in contenido:
#    print(elemento)

#leer contenido y guardarlo en lista
"""
lista1= archivo_lectura.readlines()
archivo_lectura.close()

for frase in lista1:
    print("- " + frase.upper())

"""
"""
ruta_original = str(pathlib.Path().absolute()) + "/ficherotexto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/ficherotexto2.txt"
#shutil.copyfile(ruta_original,ruta_nueva)
"""
#mover
"""
ruta_original = str(pathlib.Path().absolute()) + "/ficherotexto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_nuevo.txt"

shutil.move(ruta_original,ruta_nueva)

"""
import os
import os.path

ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_nuevo.txt"

#os.remove(ruta_nueva)

ruta_comprobar = os.path.abspath("./") + "/ficherotexto2.txt"
print(ruta_comprobar)

if os.path.isfile(ruta_comprobar):
    print("Archivo Existe")
else:
    print("Archivo no existe")
