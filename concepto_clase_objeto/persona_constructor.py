class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Creación de objetos y acceso a atributos
ana = Persona("Ana García", 28)
juan = Persona("Juan López", 35)

print(ana.nombre)  # Imprime: Ana García
print(juan.edad)   # Imprime: 35