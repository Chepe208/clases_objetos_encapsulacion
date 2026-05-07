class Círculo:
    def __init__(self, radio):
        self._radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, valor):
        if valor <= 0:
            raise ValueError("El radio debe ser positivo")
        self._radio = valor

    @property
    def área(self):
        """Área del círculo (propiedad de solo lectura)."""
        import math
        return math.pi * self._radio ** 2

    @property
    def perímetro(self):
        """Perímetro del círculo (propiedad de solo lectura)."""
        import math
        return 2 * math.pi * self._radio
c = Círculo(5)
print(f"Radio: {c.radio}")  # 5
print(f"Área: {c.área:.2f}")  # 78.54
print(f"Perímetro: {c.perímetro:.2f}")  # 31.42

# Podemos cambiar el radio
c.radio = 10
print(f"Nuevo radio: {c.radio}")  # 10
print(f"Nueva área: {c.área:.2f}")  # 314.16

# Pero no podemos cambiar el área directamente
try:
    c.área = 100
except AttributeError as e:
    print(f"Error: {e}")  # Error: can't set attribute 'área'