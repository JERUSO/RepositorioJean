from logging import exception
import usuarios.usuario as modelo
import notas.acciones


class Acciones:
    def registro(self):
        print("\nok !! vamos a registrate en el sistema")
        nombre = input ("Cual es tu nombre ??:")
        apellidos = input("Cual es tu apellido ??:")
        email=input("ingresa tu email:")
        password=input("ingresa tu contraseña:")  
        
        usuario = modelo.Usuario(nombre,apellidos,email,password)
        registro = usuario.registrar()
        
        if registro[0]>= 1:
            print(f"\nperfecto {registro[1].nombre} te haz registrado correctamente")
        else:
            print("no te haz registrado")
        
    def login(self):
        print ("\nPor favor identificarse en el sistema")
        try:
            email=input("Introduce tu tu email:")
            password=input("Introduce tu contraseña:")
            
            usuario = modelo.Usuario('','',email,password)
            login = usuario.identificar()
            if email == login[3]:
                print(f"Bienvenido {login[1]}, te haz registrado en el {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print("Login incorrecto intentarlo mas tarde")
            
    def proximasAcciones(self,usuario):
        print(
            """
            Acciones disponible
        
            - Crear notas (crear)
            - Mostrar notas (mostrar)
            - Eliminar notas (eliminar)
            - Salir (salir)
            """
        )
        accion = input("¿Que quieres hacer ?")
        
        hazEl = notas.acciones.Acciones()
        
        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
            
        elif accion == "salir":
            exit() 