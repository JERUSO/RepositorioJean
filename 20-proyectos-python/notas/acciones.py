import notas.nota as modelonota

class Acciones:
    def crear (self,usuario):
        print(f"\nOK {usuario[1]} !! vamos a crear una nueva nota")
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Ingresa el contenido de tu nota: ")
        
        nota = modelonota.Nota(usuario[0],titulo,descripcion)
        guardar = nota.guardar()
        
        if guardar[0] >=1 :
            print(f"\nPerfecto haz guardado la nota: {nota.titulo}")
        else:
            print(f"\nNose ha guardado la nota, lo siento {usuario[0]}")
    
    def mostrar (self, usuario):
        print(f"\nVale {usuario[1]}!! aqui tienes tus notas")
        nota = modelonota.Nota(usuario[0],"","")
        notas = nota.listar()
        for minota in notas:
            print("*******************************************************")
            print(f"Titulo de Nota: {minota[2]}")
            print(f"Descripcion de la Nota: {minota[2]}")
    def borrar (self,usuario):
        print(f"Okey {usuario[1]}!! vamos a borrar notas")
        titulo = input("Introduce el titulo a borrar: ")
        
        nota = modelonota.Nota(usuario[0],titulo,"")
        eliminar = nota.eliminar()
        
        if eliminar[0] >=1 :
            print("se ha borrado la nota")
        else:
            print("No se ha borrado la nota")