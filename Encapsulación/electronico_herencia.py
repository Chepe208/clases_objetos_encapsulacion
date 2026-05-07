class Producto:
    def __init__(self, nombre, precio, stock=0):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock
        self._descuento = 0

    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        return self._precio * (1 - self._descuento)

    def get_precio_base(self):
        return self._precio

    def get_stock(self):
        return self._stock

    def get_descuento(self):
        return self._descuento

    def set_nombre(self, nuevo_nombre):
        if not isinstance(nuevo_nombre, str) or len(nuevo_nombre) == 0:
            raise ValueError("El nombre debe ser una cadena no vacía")
        self._nombre = nuevo_nombre

    def set_precio(self, nuevo_precio):
        if not isinstance(nuevo_precio, (int, float)) or nuevo_precio < 0:
            raise ValueError("El precio debe ser un número positivo")
        self._precio = nuevo_precio

    def set_stock(self, nuevo_stock):
        if not isinstance(nuevo_stock, int) or nuevo_stock < 0:
            raise ValueError("El stock debe ser un entero positivo")
        self._stock = nuevo_stock

    def set_descuento(self, nuevo_descuento):
        if not isinstance(nuevo_descuento, float) or not 0 <= nuevo_descuento <= 1:
            raise ValueError("El descuento debe ser un número entre 0 y 1")
        self._descuento = nuevo_descuento

class Electrónico(Producto):
    def __init__(self, nombre, precio, stock, garantía_meses):
        super().__init__(nombre, precio, stock)
        self._garantía_meses = garantía_meses
        self._activado = False

    def get_garantía_meses(self):
        return self._garantía_meses

    def está_activado(self):
        return self._activado

    def set_garantía_meses(self, meses):
        if not isinstance(meses, int) or meses < 0:
            raise ValueError("Los meses de garantía deben ser un entero positivo")
        self._garantía_meses = meses

    def activar(self):
        self._activado = True

    def desactivar(self):
        self._activado = False

    def set_precio(self, nuevo_precio):
        super().set_precio(nuevo_precio)
        if nuevo_precio > 1000:
            self._garantía_meses = max(self._garantía_meses, 24)

# Prueba rápida
tv = Electrónico("Smart TV", 1500, 5, 12)
print(f"Producto: {tv.get_nombre()}")
print(f"Precio base: ${tv.get_precio_base()}")
print(f"Garantía inicial: {tv.get_garantía_meses()} meses")
# Al ser caro, la garantía se extiende automáticamente al modificar el precio
tv.set_precio(2000)
print(f"Garantía tras cambio de precio: {tv.get_garantía_meses()} meses")