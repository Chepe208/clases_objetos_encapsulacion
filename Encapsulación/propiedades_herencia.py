class Producto:
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

    @property
    def info(self):
        return f"{self._nombre}: {self._precio}€"
    
class ProductoDigital(Producto):
    def __init__(self, nombre, precio, tamaño_mb):
        super().__init__(nombre, precio)
        self._tamaño_mb = tamaño_mb

    @property
    def tamaño_mb(self):
        return self._tamaño_mb

    @tamaño_mb.setter
    def tamaño_mb(self, valor):
        if valor <= 0:
            raise ValueError("El tamaño debe ser positivo")
        self._tamaño_mb = valor

    # Sobrescribir la propiedad info
    @property
    def info(self):
        return f"{self._nombre}: {self._precio}€ ({self._tamaño_mb} MB)"

# Crear productos
p1 = Producto("Teclado", 49.99)
p2 = ProductoDigital("Ebook Python", 19.99, 15.5)

# Usar propiedades
print(p1.info)  # Teclado: 49.99€
print(p2.info)  # Ebook Python: 19.99€ (15.5 MB)

# Modificar propiedades
p2.tamaño_mb = 20
p2.precio = 24.99
print(p2.info)  # Ebook Python: 24.99€ (20 MB)