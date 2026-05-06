class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Representación para desarrolladores (detallada)
    def __repr__(self):
        return f"Punto({self.x}, {self.y})"

    # Representación para usuarios (amigable)
    def __str__(self):
        return f"({self.x}, {self.y})"

    # Soporte para el operador +
    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

    # Soporte para el operador ==
    def __eq__(self, otro):
        if not isinstance(otro, Punto):
            return False
        return self.x == otro.x and self.y == otro.y

    # Soporte para len()
    def __len__(self):
        # Distancia Manhattan desde el origen
        return abs(self.x) + abs(self.y)

p1 = Punto(3, 4)
p2 = Punto(1, 2)

# Uso de __str__ (implícito)
print(p1)  # (3, 4)

# Uso de __repr__ (explícito)
print(repr(p1))  # Punto(3, 4)

# Uso de __add__
p3 = p1 + p2
print(p3)  # (4, 6)

# Uso de __eq__
print(p1 == p2)  # False
print(p1 == Punto(3, 4))  # True

# Uso de __len__
print(len(p1))  # 7 (3 + 4)