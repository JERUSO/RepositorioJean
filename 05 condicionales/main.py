#ejemplo1
print('##### ejemplo 1 #######')

color = 'Rojo'

if (color == 'rojo'):
    print ('el color es rojo')
else:
    print('el color no es rojo')

# ejemplo 02
print("\n###################### ejemplo 02 ################")


#year=int(input("En que año estamos ??"))
year = 2021

if year >= 2021:
    print("Estamos posterior al 2021")
else:
    print("Estamos anterior al 2021")


#ejemplo 03
print("\n###################### ejemplo 03 ################")

nombre ="Edson Rueda"
ciudad = "Tumbes"
continente ="America del Sur"
edad = 44
mayoria_edad = 18

if edad >= mayoria_edad :
    print (f"{nombre} es mayor de edad!!")
    if continente != "America del Sur":
        print(f"No es de america del sur")
    else:
       print(f"Es de america del sur y de la ciudad {ciudad}")
else:
    print(f"{nombre} No es mayor de edad") 


#ejemplo 04
print("\n###################### ejemplo 04 ################")

dia = 1
#dia = int(input('Que dia de la semana es ?? :'))

"""

if dia == 1:
    print('Es lunes')
else:
    if dia == 2:
        print("Martes")
    else:
        if dia == 3:
            print("Miercoles")
        else:
            if dia == 4:
                print("Jueves")
            else:
                if dia == 5:
                    print("Viernes")
                else:
                    print("Es fin de semana")
"""

if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miercoles")
elif dia==4:
    print("Jueves")
elif dia==5:
    print("Vierbes")
else:
    print("Fin de semana")
    
            
#ejemplo 05
print("\n###################### ejemplo 05 ################")

edad_minima = 18
edad_maxima = 65
edad_oficial = 66

if edad_oficial>=18 and edad_oficial<=65 :
    print("Esta en edad de trabajar")
else:
    print("no esta en la edad de trabajar")

"""
# operadores de comparacion
== comparacion
> mayor
< menor
>= mayor igual
<= menor igual
!   not

operador logico
and y
or  O
! negacion
not  no

"""

            
#ejemplo 07
print("\n###################### ejemplo 07 ################")

pais = "Mexico"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia") :
    print(f"{pais} No es un pais de habla hispana")
else:
    print(f"{pais} Es un pais de Habla hispana")


#ejemplo 08
print("\n###################### ejemplo 08 ################")

pais = "Colombia"

if pais != "Mexico" and pais != "España" and pais != "Colombia" :
    print(f"{pais} No es un pais de habla hispana")
else:
    print(f"{pais} Es un pais de Habla hispana")
