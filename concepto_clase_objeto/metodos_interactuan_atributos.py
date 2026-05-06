class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial

    def consultar_saldo(self):
        return f"Saldo actual de {self.titular}: ${self._saldo}"

    def depositar(self, cantidad):
        if cantidad <= 0:
            return "La cantidad a depositar debe ser positiva"

        self._saldo += cantidad
        return f"Depósito de ${cantidad} realizado. Nuevo saldo: ${self._saldo}"

    def retirar(self, cantidad):
        if cantidad <= 0:
            return "La cantidad a retirar debe ser positiva"

        if cantidad > self._saldo:
            return "Fondos insuficientes"

        self._saldo -= cantidad
        return f"Retiro de ${cantidad} realizado. Nuevo saldo: ${self._saldo}"

cuenta = CuentaBancaria("Ana López", 1000)
print(cuenta.consultar_saldo())  # Saldo actual de Ana López: $1000
print(cuenta.depositar(500))     # Depósito de $500 realizado. Nuevo saldo: $1500
print(cuenta.retirar(200))       # Retiro de $200 realizado. Nuevo saldo: $1300
print(cuenta.retirar(2000))      # Fondos insuficientes