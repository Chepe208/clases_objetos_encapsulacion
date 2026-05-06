class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.kilometraje = 0

# Creamos un coche nuevo
mi_coche = Coche("Toyota", "Corolla", "Azul")
print(f"Color inicial: {mi_coche.color}")  # Imprime: Color inicial: Azul
print(f"Kilometraje inicial: {mi_coche.kilometraje}")  # Imprime: Kilometraje inicial: 0

# Modificamos sus atributos
mi_coche.color = "Rojo"  # Pintamos el coche
mi_coche.kilometraje = 1500  # Actualizamos el kilometraje

print(f"Nuevo color: {mi_coche.color}")  # Imprime: Nuevo color: Rojo
print(f"Kilometraje actual: {mi_coche.kilometraje}")  # Imprime: Kilometraje actual: 1500