class Formulario:
    def __init__(self):
        self._datos = {}
        self._errores = {}

    def validar(self, datos):
        """Método público para validar todos los datos del formulario."""
        self._datos = datos.copy()
        self._errores = {}

        # Usar métodos privados para cada tipo de validación
        self.__validar_campos_requeridos()
        self.__validar_email()
        self.__validar_contraseña()
        self.__validar_edad()

        return len(self._errores) == 0

    def obtener_errores(self):
        """Método público para obtener los errores de validación."""
        return self._errores.copy()

    def __validar_campos_requeridos(self):
        """Método privado para validar campos obligatorios."""
        campos_requeridos = ['nombre', 'email', 'contraseña']
        for campo in campos_requeridos:
            if campo not in self._datos or not self._datos[campo]:
                self._errores[campo] = f"El campo {campo} es obligatorio"

    def __validar_email(self):
        """Método privado para validar formato de email."""
        if 'email' in self._datos and self._datos['email']:
            import re
            patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(patron, self._datos['email']):
                self._errores['email'] = "El formato del email no es válido"

    def __validar_contraseña(self):
        """Método privado para validar seguridad de contraseña."""
        if 'contraseña' in self._datos and self._datos['contraseña']:
            contraseña = self._datos['contraseña']
            if len(contraseña) < 8:
                self._errores['contraseña'] = "La contraseña debe tener al menos 8 caracteres"
            elif not any(c.isupper() for c in contraseña):
                self._errores['contraseña'] = "La contraseña debe contener al menos una mayúscula"
            elif not any(c.isdigit() for c in contraseña):
                self._errores['contraseña'] = "La contraseña debe contener al menos un número"

    def __validar_edad(self):
        """Método privado para validar la edad."""
        if 'edad' in self._datos:
            try:
                edad = int(self._datos['edad'])
                if edad < 18:
                    self._errores['edad'] = "Debes ser mayor de edad"
                elif edad > 120:
                    self._errores['edad'] = "La edad ingresada no es válida"
            except ValueError:
                self._errores['edad'] = "La edad debe ser un número"

formulario = Formulario()

datos_incorrectos = {
    'nombre': '',
    'email': 'correo-malo',
    'contraseña': 'abc',
    'edad': '15'
}
formulario.validar(datos_incorrectos)
print("Errores encontrados:", formulario.obtener_errores())

datos_correctos = {
    'nombre': 'Ana',
    'email': 'ana@email.com',
    'contraseña': 'Clave1234',
    'edad': '25'
}
if formulario.validar(datos_correctos):
    print("¡Formulario válido!")