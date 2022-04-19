
contador = 0
resultado = 0
for contador in range(0,10):
    resultado = resultado + contador
print("El resultado es: " + str(resultado))
    
numero_usuario = int(input(" de que numero quiere la tabla ?"))

if numero_usuario<1:
    numero_usuario=1

print(f"\n############# tabla de multiplicar de {numero_usuario} #####")

for numero_tabla in range (0,11):
    if numero_usuario == 45:
        print("No se puede usar numeros prohibidos !!")
        break
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla} ")
else:
    print("Tabla finalizada")