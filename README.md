# GA1-220501093-04-AA1-EV04 – Fundamentos de Python: Clases, Objetos y Encapsulación

## Conceptos teóricos de Clase y Objeto – Primera parte

### Explicación de cada ejemplo

#### 1. Una clase vacía y creación de objetos

Se crea la clase `Coche` sin atributos ni métodos, solo con `pass`. Aunque esté vacía, ya podemos crear objetos de tipo `Coche`.

![Clase coche](images/clase_coche.png)

#### 2. El constructor `__init__` y `self`

La clase `Persona` tiene un método especial llamado `__init__`. Este método se ejecuta automáticamente cuando creamos una persona nueva. El parámetro `self` representa al objeto que se está creando; con `self.nombre = nombre` le estamos asignando el valor que recibimos al atributo `nombre` de ese objeto.

Creamos dos personas (`ana` y `juan`) y cada una guarda su propio nombre y edad. Al imprimirlos se comprueba que son independientes.

![Persona](images/persona_constructor.png)

#### 3. Valores por defecto en el constructor
La clase `Producto` tiene un parámetro `stock` con valor por defecto `0`. Si al crear un producto no le decimos cuánto stock tiene, automáticamente se pone en cero. Si sí le damos un valor, se usa ese.

Esto sirve para que algunos datos sean opcionales y el objeto tenga siempre un valor razonable.

![Producto](images/producto_default.png)

#### 4. Calcular atributos al crear el objeto

La clase `Rectangulo` recibe el ancho y el alto, y dentro del constructor calcula el área y el perímetro. Esos valores calculados se guardan en atributos normales (`self.area`, `self.perimetro`) y luego los usamos sin tener que volver a calcularlos.

![Rectangulo](images/rectangulo_calculos.png)

#### 5. Validar datos en el constructor

La clase `Cuenta` no permite que se cree una cuenta con saldo negativo. Si alguien lo intenta, lanza un error (`ValueError`). Esto evita que existan objetos en un estado incorrecto.

Primero creamos una cuenta válida y luego intentamos crear una inválida, capturando el error para que el programa no se Detenga.

![Captura 05](images/cuenta_validacion.png)

#### 6. Modelar un libro con varios atributos

La clase `Libro` guarda título, autor, páginas, ISBN y disponibilidad. El parámetro `disponible` es opcional (por defecto `True`). Al crear dos libros, uno se marca como prestado (`False`) y el otro queda disponible. Luego imprimimos su estado.

Este ejemplo muestra cómo una clase puede representar algo del mundo real agrupando toda la información importante.

![libros biblioteca](images/libro_biblioteca.png)

#### 7. Distintas formas de crear un objeto

La clase `Fecha` tiene el constructor normal, pero además dos métodos de clase que funcionan como fábricas de objetos:

- `desde_texto`: recibe una cadena "DD-MM-AAAA" y devuelve una `Fecha`.
- `hoy`: devuelve una `Fecha` con el día actual.

Esto permite crear objetos de manera más cómoda sin tocar el constructor original.

![fechas](images/fecha_constructores.png)

#### 8. Atributos de instancia

Cada objeto creado a partir de la clase `Estudiante` tiene sus propias copias de `nombre`, `edad` y `activo`. Si cambio los datos de un estudiante, el otro no se entera. Son independientes.

![instancia estudiante](images/instancia_estudiante.png)

#### 9. Atributos de clase

El atributo `universidad` está definido en la clase, no en cada objeto. Todos los estudiantes comparten la misma universidad. Si cambio `Estudiante.universidad`, el cambio se refleja en todas las instancias.

![Atributos clase](images/atributos_clase.png)

#### 10. Acceder a los atributos

Usamos la notación `objeto.atributo` para leer tanto atributos de instancia como de clase. También podemos leer el atributo de clase directamente desde la clase misma (`Producto.impuesto`).

![Acceso atributos](images/acceso_atributos.png)

#### 11. Modificar atributos

Después de crear un objeto podemos cambiar sus atributos asignándoles un nuevo valor. Aquí pintamos un coche de rojo y le ponemos kilometraje 1500.

![Modificacion atributos](images/modificacion_atributos.png)

#### 12. Atributos dinámicos
Python permite agregar atributos a un objeto "sobre la marcha". A `juan`, que originalmente solo tenía `nombre`, le añadimos `edad` y `profesion`. Es flexible, pero hay que tener cuidado de no olvidar inicializar los atributos importantes en el constructor.

![Atributos Dinamicos](images/atributos_dinamicos.png)

#### 13. Atributos privados y protegidos

Por convención, un guion bajo (`_saldo`) indica que el atributo es "protegido" y no debería tocarse desde fuera. Dos guiones bajos (`__pin`) activan un mecanismo que cambia el nombre del atributo para que sea más difícil acceder a él por error. Aun así, Python no bloquea el acceso de forma absoluta.

![Atributos privados](images/atributos_privados.png)

#### 14. Propiedades

Con los decoradores `@property` y `@nombre.setter` podemos hacer que al leer o escribir un atributo se ejecute código. La clase `Temperatura` permite usar `celsius` y `fahrenheit` como si fueran atributos normales, pero con validación y conversión automática.

![Propiedades atributos](images/propiedades1.png)
![Propiedades atributos](images/propiedades2.png)

#### 15. Atributos calculados

En lugar de guardar el área y el perímetro, los calculamos cada vez que los pedimos usando `@property`. Así, si cambiamos el ancho, el área y el perímetro se actualizan solos.

![Atributos calculados](images/atributos_calculados.png)

#### 16. Atributos especiales

Python guarda información interna en atributos como `__class__` (la clase del objeto), `__name__` (nombre de la clase), `__doc__` (su documentación) y `__dict__` (los atributos de instancia). Podemos leerlos para inspeccionar objetos.

![Atributos especiales](images/atributos_especiales.png)

#### 17. Funciones para manejar atributos

Las funciones `hasattr`, `getattr`, `setattr` y `delattr` permiten trabajar con atributos de manera dinámica. Útiles cuando no sabemos el nombre del atributo de antemano. Aquí vemos cómo comprobar si existe un atributo, leerlo, crearlo y eliminarlo.

![Funciones para atributos](images/gestion_atributos.png)

#### 18. Definir métodos

La clase `Coche` tiene dos métodos, `encender` y `apagar`. Ambos llevan `self` como primer parámetro, lo que les permite acceder a los atributos del coche (`self.encendido`, `self.velocidad`). Aquí solo se define la clase; el uso está en el siguiente ejemplo.

![Definir metodos](images/definicion_metodos.png)

#### 19. Métodos con parámetros

Los métodos `acelerar` e `frenar` reciben un número (cuánto acelerar o frenar). Validan que el coche esté encendido y que no se supere la velocidad máxima. Siempre devuelven un mensaje con el resultado.

![Metodos con parametros](images/metodos_con_parametros1.png)
![Metodos con parametros](images/metodos_con_parametros2.png)

#### 20. Métodos que modifican atributos

La clase `CuentaBancaria` tiene métodos para consultar saldo, depositar y retirar. Todos leen o modifican `_saldo`, aplicando reglas: no se puede depositar o retirar cantidades negativas y no se puede gastar más de lo que hay.

![Metodos interactuan atributos](images/metodos_interactuan_atributos..png)

#### 21. Métodos que devuelven valores complejos 

La `Calculadora` puede devolver números, mensajes de error y hasta diccionarios con estadísticas. Así el objeto puede entregar información procesada sin necesidad de tratar los datos fuera de la clase.

![Metodos devuelven valores ](images/metodos_devuelven_valores1.png)
![Metodos devuelven valores ](images/metodos_devuelven_valores.png)

#### 22. Métodos que se llaman entre sí

El método `presentarse` de `Persona` invoca a `nombre_completo` y a `es_mayor_de_edad` con `self`. De esta forma, el código se reutiliza y la lógica queda ordenada.

![Metodos llaman metodos](images/metodos_llaman_metodos.png)

#### 23. Métodos especiales o “dunder”

La clase `Punto` define `__str__` (para mostrarse bonito), `__repr__` (para desarrolladores), `__add__` (para sumar dos puntos con `+`), `__eq__` (para comparar con `==`) y `__len__` (para usar `len()`). Estos métodos hacen que nuestros objetos se comporten como los tipos nativos de Python.

![Metodos especiales](images/metodos_especiales.png)
![Metodos especiales](images/metodos_especiales2.png)

#### 24. Métodos estáticos
Los métodos de `MathUtils` llevan `@staticmethod` y no reciben `self`. Son funciones independientes que agrupamos dentro de la clase porque tienen relación lógica. Se llaman directamente desde la clase sin crear una instancia.

![Metodos estaticos](images/metodos_estaticos.png)

#### 25. Métodos de clase 

Los métodos de `Empleado` llevan `@classmethod` y reciben `cls` (la clase) en lugar de `self`. `desde_salario_anual` actúa como un constructor alternativo, y `obtener_num_empleados` sirve para consultar cuántos empleados se han creado.

![Metodos de clase](images/metodos_clase.png)

#### 26. Ejemplo integrador: la biblioteca 

La clase `Libro` junta todo lo aprendido: constructor, métodos que validan el estado (`abrir`, `cerrar`, `leer`), cálculos de avance de lectura y un método especial `__str__`. La simulación muestra cómo el libro pasa de cerrado a leerse por completo y luego se reinicia.

![Ejemplo practico biblioteca](images/ejemplo_practico_biblioteca1.png)
![Ejemplo practico biblioteca](images/ejemplo_practico_biblioteca2.png)


