class Temperatura:
    def __init__(self):
        self._celsius = 0

    # Definimos la propiedad celsius
    @property
    def celsius(self):
        """Obtiene la temperatura en grados Celsius"""
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        """Establece la temperatura en grados Celsius"""
        if valor < -273.15:
            raise ValueError("La temperatura no puede ser menor que el cero absoluto")
        self._celsius = valor

    # Definimos la propiedad fahrenheit
    @property
    def fahrenheit(self):
        """Obtiene la temperatura en grados Fahrenheit"""
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, valor):
        """Establece la temperatura en grados Fahrenheit"""
        self.celsius = (valor - 32) * 5/9

# Creamos un objeto temperatura
temp = Temperatura()

# Usamos las propiedades como si fueran atributos normales
temp.celsius = 25
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")  # Imprime: 25°C = 77.0°F

temp.fahrenheit = 68
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")  # Imprime: 20.0°C = 68.0°F

# La validación funciona
try:
    temp.celsius = -300  # Esto lanzará un error
except ValueError as e:
    print(f"Error: {e}")  # Imprime: Error: La temperatura no puede ser menor que el cero absoluto