import os

#crear carpeta

if not os.path.isdir("./micarpeta"):
    os.mkdir("./micarpeta")
else:
    print("Directorio ya existe")

#eliminar
#os.rmdir("./micarpeta")

