class Empleado:
    # Atributo de clase
    num_empleados = 0

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        Empleado.num_empleados += 1

    @classmethod
    def desde_salario_anual(cls, nombre, salario_anual):
        """Constructor alternativo que recibe salario anual en lugar de mensual"""
        salario_mensual = salario_anual / 12
        return cls(nombre, salario_mensual)

    @classmethod
    def obtener_num_empleados(cls):
        """Devuelve el número total de empleados creados"""
        return cls.num_empleados
    
# Creación normal
emp1 = Empleado("Ana", 3000)

# Usando el método de clase como constructor alternativo
emp2 = Empleado.desde_salario_anual("Carlos", 48000)  # Salario mensual: 4000

print(f"Empleados creados: {Empleado.obtener_num_empleados()}")  # Empleados creados: 2