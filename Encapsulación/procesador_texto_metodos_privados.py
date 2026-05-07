class ProcesadorTexto:
    def __init__(self):
        self._texto = ""
        self._estadísticas = {}

    def procesar_archivo(self, ruta_archivo):
        """Método público que procesa un archivo de texto."""
        try:
            texto = self.__leer_archivo(ruta_archivo)
            self._texto = self.__normalizar_texto(texto)
            self._estadísticas = self.__calcular_estadísticas(self._texto)
            return True
        except Exception as e:
            print(f"Error al procesar el archivo: {e}")
            return False

    def __leer_archivo(self, ruta):
        """Método privado para leer el contenido de un archivo."""
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return archivo.read()

    def __normalizar_texto(self, texto):
        """Método privado para normalizar el texto."""
        # Convertir a minúsculas
        texto = texto.lower()
        # Eliminar caracteres especiales
        import re
        texto = re.sub(r'[^\w\s]', '', texto)
        # Eliminar espacios extra
        texto = re.sub(r'\s+', ' ', texto).strip()
        return texto

    def __calcular_estadísticas(self, texto):
        """Método privado para calcular estadísticas del texto."""
        palabras = texto.split()
        estadísticas = {
            'total_palabras': len(palabras),
            'palabras_únicas': len(set(palabras)),
            'longitud_promedio': sum(len(p) for p in palabras) / len(palabras) if palabras else 0
        }
        return estadísticas

    def obtener_estadísticas(self):
        """Método público para acceder a las estadísticas calculadas."""
        return self._estadísticas.copy()

    def obtener_texto_procesado(self):
        """Método público para obtener el texto procesado."""
        return self._texto
    
procesador = ProcesadorTexto()
exito = procesador.procesar_archivo("no_existe.txt")
print("¿Procesamiento exitoso?:", exito)
print("Estadísticas (vacías):", procesador.obtener_estadísticas())
print("Texto procesado (vacío):", procesador.obtener_texto_procesado())