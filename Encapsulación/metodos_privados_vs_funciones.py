class Ejemplo1:
    def método_público(self, datos):
        # Función auxiliar definida dentro del método
        def función_auxiliar(x):
            return x * 2

        resultado = [función_auxiliar(x) for x in datos]
        return resultado

class Ejemplo2:
    def método_público(self, datos):
        resultado = [self.__función_auxiliar(x) for x in datos]
        return resultado

    def __función_auxiliar(self, x):
        return x * 2
    
e1 = Ejemplo1()
e2 = Ejemplo2()
print("Ejemplo1 (función interna):", e1.método_público([1, 2, 3]))
print("Ejemplo2 (método privado):", e2.método_público([1, 2, 3]))