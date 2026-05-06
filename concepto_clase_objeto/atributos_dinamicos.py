class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

# Creamos una persona
juan = Persona("Juan")

# Añadimos atributos dinámicamente
juan.edad = 30
juan.profesion = "Ingeniero"

print(f"{juan.nombre} tiene {juan.edad} años y es {juan.profesion}")
# Imprime: Juan tiene 30 años y es Ingeniero
