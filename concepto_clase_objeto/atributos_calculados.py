class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @property
    def area(self):
        """Área del rectángulo, calculada dinámicamente"""
        return self.ancho * self.alto

    @property
    def perimetro(self):
        """Perímetro del rectángulo, calculado dinámicamente"""
        return 2 * (self.ancho + self.alto)

# Creamos un rectángulo
rect = Rectangulo(5, 3)

# Accedemos a los atributos calculados
print(f"Área: {rect.area}")        # Imprime: Área: 15
print(f"Perímetro: {rect.perimetro}")  # Imprime: Perímetro: 16

# Si modificamos el rectángulo, los atributos calculados se actualizan automáticamente
rect.ancho = 7
print(f"Nueva área: {rect.area}")  # Imprime: Nueva área: 21