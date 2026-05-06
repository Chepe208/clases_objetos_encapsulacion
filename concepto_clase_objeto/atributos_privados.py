class CuentaBancaria:
    tasa_interes = 0.03  # Atributo de clase público

    def __init__(self, titular, saldo_inicial, pin):
        self.titular = titular        # Atributo público
        self._saldo = saldo_inicial   # Atributo "protegido"
        self.__pin = pin              # Atributo "privado"

    def verificar_pin(self, pin_ingresado):
        return self.__pin == pin_ingresado

# Creamos una cuenta
cuenta = CuentaBancaria("Ana López", 1000, "1234")

# Acceso a atributos según su visibilidad
print(cuenta.titular)  # Funciona: atributo público
print(cuenta._saldo)   # Funciona, pero no deberíamos hacerlo por convención
# print(cuenta.__pin)  # Error: no existe tal atributo debido al name mangling

# El atributo privado existe, pero con un nombre modificado
print(cuenta._CuentaBancaria__pin)  # Funciona, pero es una mala práctica