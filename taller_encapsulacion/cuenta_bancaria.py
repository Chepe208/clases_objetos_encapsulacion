class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular   # atributo privado (convención)
        self._saldo = saldo_inicial

    # Propiedad titular (solo lectura)
    @property
    def titular(self):
        """Obtiene el titular de la cuenta."""
        return self._titular

    # Propiedad saldo (lectura y escritura con validación)
    @property
    def saldo(self):
        """Obtiene el saldo actual de la cuenta."""
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        """Establece el saldo, no permite valores negativos."""
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = valor

    def depositar(self, cantidad):
        """
        Incrementa el saldo si la cantidad es positiva.
        Devuelve True si se realizó el depósito, False en caso contrario.
        """
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False

    def retirar(self, cantidad):
        """
        Disminuye el saldo si hay suficiente dinero y la cantidad es positiva.
        Devuelve True si se realizó el retiro, False en caso contrario.
        """
        if cantidad > 0 and self._saldo >= cantidad:
            self._saldo -= cantidad
            return True
        return False


# --- Prueba completa de la clase ---
def main():
    print("=== Creación de cuenta ===")
    cuenta = CuentaBancaria("Ana López", 1000)
    print(f"Titular: {cuenta.titular}")
    print(f"Saldo inicial: ${cuenta.saldo}")

    print("\n=== Intentar leer titular (solo lectura) ===")
    print(f"Titular: {cuenta.titular}")
    # cuenta.titular = "Otro"  # Descomentar daría AttributeError: can't set attribute

    print("\n=== Modificar saldo con propiedad (válido) ===")
    cuenta.saldo = 1500
    print(f"Nuevo saldo: ${cuenta.saldo}")

    print("\n=== Intentar saldo negativo ===")
    try:
        cuenta.saldo = -200
    except ValueError as e:
        print(f"Error: {e}")

    print("\n=== Depósito exitoso ===")
    resultado = cuenta.depositar(500)
    print(f"¿Depósito exitoso? {resultado}, Saldo actual: ${cuenta.saldo}")

    print("\n=== Depósito con cantidad negativa ===")
    resultado = cuenta.depositar(-100)
    print(f"¿Depósito exitoso? {resultado}, Saldo actual: ${cuenta.saldo}")

    print("\n=== Retiro exitoso ===")
    resultado = cuenta.retirar(200)
    print(f"¿Retiro exitoso? {resultado}, Saldo actual: ${cuenta.saldo}")

    print("\n=== Retiro con fondos insuficientes ===")
    resultado = cuenta.retirar(5000)
    print(f"¿Retiro exitoso? {resultado}, Saldo actual: ${cuenta.saldo}")

    print("\n=== Retiro con cantidad negativa ===")
    resultado = cuenta.retirar(-50)
    print(f"¿Retiro exitoso? {resultado}, Saldo actual: ${cuenta.saldo}")

    print("\n=== Estado final de la cuenta ===")
    print(f"Titular: {cuenta.titular}, Saldo: ${cuenta.saldo}")


if __name__ == "__main__":
    main()