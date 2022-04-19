# ejemplo 1

def mostrarNombres():
    print("Jean")
    print("ivon")
    print("vale")

mostrarNombres()

#ejemplo2

nombre = "Jean"

def mostrarTuNombre(nombre1):
    print (f"Tu nombre es: {nombre1}")

#nombre= input("introduce tu nombre : ")
nombre = ""
mostrarTuNombre(nombre)

def getEmpleado (nombre, dni):
    print('Empleado')
    print(f"Nombre : {nombre}")
    print(f"DNI : {dni}")

getEmpleado ("jean","18179729")
#ejemplo3

print ('\n############### EJEMPLO 3 ############### ')

def tabla(numero):
    print(f"tabla de multiplicar de {numero}")
    for contador in range(0,11):
        operacion = numero*contador
        print(f"{numero}*{contador} = {operacion} ")
    
    print("\n")

tabla(3)
tabla(7)
tabla(12)

#ejemplo 3.1

#for numero_tabla in range(1,11):
#    tabla(numero_tabla)

# EJEMPLO 04 -- PARAMETROS OPCIONALES
print ('\n############### EJEMPLO 4 ############### ')

#parametros opcionales

def get_empleado (nombre, dni = None):
    print("Empleado")
    print(f"{nombre}")
    if dni != None:
        print(f"{dni}")

get_empleado("jean","18179729")

#ejemplo 05 : parametros opcionales - return

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"
    print(saludo)
    return(saludo)

saludame ("Edson Rueda")

# ejemplo 6 # calculadora

def calculadora (numero1,numero2,basicas=False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1*numero2
    division=numero1/numero2

    cadena =""
    if (basicas != False): 
        cadena += "Suma:" + str(suma) 
        cadena += "\n"
        cadena += "Resta:" + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicacion:" + str(multi)
        cadena +="\n"
        cadena += "Division:" + str(division)
    return (cadena)
 
print(calculadora(55,5,True))


# ejemplo 7 # 

print("###### ejemplo 7 ############")

def getNombre(nombre):
    texto1=f"El nombre es {nombre}"
    return texto1

def getApellidos(apellido):
    texto2=f"El apellido es {apellido}"
    return texto2

def devuelvetodo (nombres, apellidos):
    texto=getNombre(nombres) + "\n" + getApellidos(apellidos)
    return texto


print(getNombre("Jeancarlo"),getApellidos("Rueda"))

print(devuelvetodo("Edson Jeancarlo","Rueda Sócola"))

dimeelanio= lambda year:f"El año es {year*50}"
print(dimeelanio(2034))


     
    

