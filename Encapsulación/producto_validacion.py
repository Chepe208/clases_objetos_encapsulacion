class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = precio

# Pequeña demostración de la validación
try:
    producto = Producto("Teclado", -10)
except ValueError as e:
    print(f"Error: {e}")