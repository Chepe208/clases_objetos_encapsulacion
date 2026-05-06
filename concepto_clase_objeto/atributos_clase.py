class Estudiante:
    # Atributo de clase
    universidad = "Universidad Autónoma"

    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad      # Atributo de instancia

# Creamos dos estudiantes
estudiante1 = Estudiante("María", 20)
estudiante2 = Estudiante("Carlos", 22)

# Ambos comparten el mismo atributo de clase
print(estudiante1.universidad)  # Imprime: Universidad Autónoma
print(estudiante2.universidad)  # Imprime: Universidad Autónoma
print(Estudiante.universidad)   # También podemos acceder desde la clase

# Si modificamos el atributo de clase, afecta a todas las instancias
Estudiante.universidad = "Universidad Complutense"
print(estudiante1.universidad)  # Imprime: Universidad Complutense
print(estudiante2.universidad)  # Imprime: Universidad Complutense