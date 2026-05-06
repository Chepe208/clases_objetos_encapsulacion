class Ejemplo:
    """Clase de ejemplo para mostrar atributos especiales"""
    def __init__(self, valor):
        self.valor = valor

# Creamos una instancia
obj = Ejemplo(42)

# Atributos especiales
print(obj.__class__)  # Muestra la clase del objeto
print(Ejemplo.__name__)  # Nombre de la clase
print(Ejemplo.__doc__)  # Documentación de la clase
print(obj.__dict__)  # Diccionario que almacena los atributos de instancia