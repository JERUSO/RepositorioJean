import clases

persona = clases.Persona()
persona.setNombre("Jean")
persona.setApellidos("Rueda")
persona.setAltura ("1.65 cm")
persona.setEdad("44 años")

print(f"La persona es {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())

informatico = clases.Informatico()

informatico.setNombre("Carlos")
informatico.setApellidos("Martines")

print(f"El informativo es {informatico.getNombre()} {informatico.getApellidos()}")

print(informatico.hablar())
print(informatico.programar())
print(informatico.repararPC())
print(informatico.experiencia)

tecnico = clases.TecnicoRedes()
print(tecnico.auditoria())
print(tecnico.getlenguajes())
tecnico.setNombre("Juan")
print(tecnico.getNombre())