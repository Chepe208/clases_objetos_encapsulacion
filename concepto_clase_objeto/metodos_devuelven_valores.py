class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Error: División por cero"
        return a / b

    def calcular_estadisticas(self, numeros):
        if not numeros:
            return {
                "suma": 0,
                "promedio": 0,
                "minimo": None,
                "maximo": None
            }

        return {
            "suma": sum(numeros),
            "promedio": sum(numeros) / len(numeros),
            "minimo": min(numeros),
            "maximo": max(numeros)
        }

calc = Calculadora()
print(calc.sumar(5, 3))        # 8
print(calc.dividir(10, 2))     # 5.0
print(calc.dividir(10, 0))     # Error: División por cero

# Método que devuelve un diccionario
estadisticas = calc.calcular_estadisticas([4, 7, 2, 9, 5])
print(f"Suma: {estadisticas['suma']}")         # Suma: 27
print(f"Promedio: {estadisticas['promedio']}") # Promedio: 5.4
print(f"Mínimo: {estadisticas['minimo']}")     # Mínimo: 2
print(f"Máximo: {estadisticas['maximo']}")     # Máximo: 9