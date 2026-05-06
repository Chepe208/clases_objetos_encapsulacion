class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p = Persona("Laura", 29)

# Verificar si un objeto tiene un atributo
print(hasattr(p, "nombre"))  # True
print(hasattr(p, "apellido"))  # False

# Obtener el valor de un atributo
print(getattr(p, "nombre"))  # Laura
print(getattr(p, "apellido", "No especificado"))  # No especificado (valor predeterminado)

# Establecer un atributo
setattr(p, "apellido", "García")
print(p.apellido)  # García

# Eliminar un atributo
delattr(p, "apellido")
# print(p.apellido)  # Esto daría error porque ya no existe