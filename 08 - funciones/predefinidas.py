nombre="Edson rueda"

#funciones generales
print(nombre)
print(type(nombre))

#detectar el tipado
comprobar = isinstance(nombre,str)
if comprobar:
    print("Esa variable es una string")
else:
    print("No es una cadena")

#encontrar caracteres
frase = "La vida es bella"

print(frase.find("vida"))

#reemplazar

frase = frase.split()