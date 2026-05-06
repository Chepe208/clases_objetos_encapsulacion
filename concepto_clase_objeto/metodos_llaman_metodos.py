class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def presentarse(self):
        estado = "mayor" if self.es_mayor_de_edad() else "menor"
        return f"Hola, soy {self.nombre_completo()} y soy {estado} de edad."

persona = Persona("Juan", "Pérez", 25)
print(persona.nombre_completo())  # Juan Pérez
print(persona.es_mayor_de_edad()) # True
print(persona.presentarse())      # Hola, soy Juan Pérez y soy mayor de edad.