class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad      # Atributo de instancia
        self.activo = True    # Atributo de instancia con valor predeterminado

# Creamos dos estudiantes
estudiante1 = Estudiante("María", 20)
estudiante2 = Estudiante("Carlos", 22)

# Cada estudiante tiene sus propios valores para los atributos
print(estudiante1.nombre)  # Imprime: María
print(estudiante2.nombre)  # Imprime: Carlos