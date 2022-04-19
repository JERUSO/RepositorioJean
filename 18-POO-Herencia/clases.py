class Persona:
    """
    nombre
    apellidos
    altura
    edad
    """
    def getNombre (self):
        return self.nombre
    
    def getApellidos (self):
        return self.apellidos

    def getEdad (self):
        return self.edad
    
    def getAltura(self):
        return self.altura

    def setNombre(self,nombre):
        self.nombre = nombre
    
    def setApellidos(self,apellidos):
        self.apellidos = apellidos
    
    def setAltura (self,altura):
        self.altura = altura

    def setEdad (self,edad):
        self.edad = edad
    
    def hablar(self):
        return "Estoy hablando"
    
    def caminar(self):
        return "Estoy caminando"

    def dormin (self):
        return "Estoy durmiento"
    
class Informatico (Persona):
    """
    lenguajes
    experiencias
    """
    def __init__(self):
        self.lenguajes  = "HTML,CS, JavaScript,PHP"
        self.experiencia = 5
    
    def getlenguajes (self):
        return self.lenguajes
    
    def aprender (self,lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes

    def programar(self):
        return "Estoy programando"
    
    def repararPC(self):
        return "He reparado tu computador"

class TecnicoRedes(Informatico):
    def __init__(self):
        super().__init__()
        self.auditarRedes= "Experto"
        self.experienciaRedes = 15
    
    def auditoria(self):
        return "Estoy auditando una red"