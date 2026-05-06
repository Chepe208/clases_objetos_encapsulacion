class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
        self.encendido = False
        self.velocidad_maxima = 200

    def encender(self):
        if not self.encendido:
            self.encendido = True
            return f"{self.marca} {self.modelo} encendido"
        return f"{self.marca} {self.modelo} ya estaba encendido"

    def acelerar(self, incremento):
        if not self.encendido:
            return f"No se puede acelerar: {self.marca} {self.modelo} está apagado"

        nueva_velocidad = self.velocidad + incremento

        if nueva_velocidad > self.velocidad_maxima:
            self.velocidad = self.velocidad_maxima
            return f"Velocidad máxima alcanzada: {self.velocidad} km/h"

        self.velocidad = nueva_velocidad
        return f"Velocidad actual: {self.velocidad} km/h"

    def frenar(self, decremento):
        if self.velocidad == 0:
            return "El coche ya está detenido"

        nueva_velocidad = self.velocidad - decremento

        if nueva_velocidad < 0:
            self.velocidad = 0
            return "Coche detenido"

        self.velocidad = nueva_velocidad
        return f"Velocidad actual: {self.velocidad} km/h"

mi_coche = Coche("Toyota", "Corolla")
print(mi_coche.encender())     # Toyota Corolla encendido
print(mi_coche.acelerar(50))   # Velocidad actual: 50 km/h
print(mi_coche.acelerar(30))   # Velocidad actual: 80 km/h
print(mi_coche.frenar(20))     # Velocidad actual: 60 km/h
print(mi_coche.frenar(60))     # Coche detenido