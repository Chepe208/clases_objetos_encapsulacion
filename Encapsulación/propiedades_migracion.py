# Versión inicial con atributos públicos
class ProductoV1:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Versión intermedia con getters y setters
class ProductoV2:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, valor):
        self._nombre = valor

    def get_precio(self):
        return self._precio

    def set_precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor

# Versión final con propiedades
class ProductoV3:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor
        
p1 = ProductoV1("Teclado", 49.99)
print(f"V1 - nombre: {p1.nombre}, precio: {p1.precio}")

p3 = ProductoV3("Teclado", 49.99)
print(f"V3 - nombre: {p3.nombre}, precio: {p3.precio}")

try:
    p3.precio = -10
except ValueError as e:
    print(f"Error V3: {e}")