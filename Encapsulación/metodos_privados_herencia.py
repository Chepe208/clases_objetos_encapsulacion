class Base:
    def __init__(self):
        self.público = "Accesible para todos"

    def método_público(self):
        print("Método público llamando a método privado:")
        self.__método_privado()

    def __método_privado(self):
        print("Este es un método privado de Base")

class Derivada(Base):
    def nuevo_método(self):
        print("Intentando llamar al método privado del padre:")
        try:
            self.__método_privado()  # Esto fallará
        except AttributeError as e:
            print(f"Error: {e}")

    def __método_privado(self):
        print("Este es un método privado de Derivada")

base = Base()
base.método_público()  # Funciona correctamente

derivada = Derivada()
derivada.método_público()  # Funciona, llama al __método_privado de Base
derivada.nuevo_método()  # Falla al intentar llamar a __método_privado de Base