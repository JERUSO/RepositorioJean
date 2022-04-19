#programacion orientada a objetos (POO ó OOP)

#Definir una clase (molde para crear mas objetos de ese tipo)
# (Coche) con características similares

class Coche:
    #atributos o variables 
    #caracteristicas del coche
    color = "rojo"
    marca = "Ferrary"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas =2

    #métodos son acciones que hace el objeto (coche) (funciones)
    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad(self):
        return self.velocidad
    
    def setColor(self,color):
        self.color = color

    def getColor(self):
        return self.color  

    def setModelo(self,modelo1):
        self.modelo = modelo1

    def getModelo(self):
        return self.modelo
    

          

#fin definición clase
# crear objeto o instanciar la clase
coche=Coche()
coche.setColor ("Amarillo")
coche.setModelo ("Mustan")
print("COCHE1")
print(coche.marca,coche.getColor(),coche.getModelo())
print("Velocidad actual:", coche.velocidad )

#crear mas objetos
coche2 = Coche()

print("COCHE2")
print(coche2.marca,coche2.getColor(),coche2.getModelo())
