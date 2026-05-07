class Autenticador:
    def __init__(self, usuario, contraseña):
        self._usuario = usuario
        self._contraseña_hash = self.__generar_hash(contraseña)

    def __generar_hash(self, contraseña):
        """Método privado para generar un hash de la contraseña."""
        import hashlib
        return hashlib.sha256(contraseña.encode()).hexdigest()

    def verificar_contraseña(self, contraseña_ingresada):
        """Método público que utiliza el método privado internamente."""
        hash_ingresado = self.__generar_hash(contraseña_ingresada)
        return hash_ingresado == self._contraseña_hash

# Prueba
auth = Autenticador("admin", "secreto123")
print(f"¿Contraseña correcta? {auth.verificar_contraseña('secreto123')}")
print(f"¿Contraseña incorrecta? {auth.verificar_contraseña('clave_equivocada')}")