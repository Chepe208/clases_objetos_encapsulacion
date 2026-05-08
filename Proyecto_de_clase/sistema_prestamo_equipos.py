"""
Sistema de Préstamos de Equipos
"""

# Diccionario principal: cada equipo tiene estado y lista de préstamos (tuplas)
inventario = {
    "Laptop HP": {
        "disponible": True,
        "prestamos": []  # cada préstamo será una tupla (usuario, fecha)
    },
    "Proyector Epson": {
        "disponible": True,
        "prestamos": []
    },
    "Tablet Samsung": {
        "disponible": True,
        "prestamos": []
    }
}


def mostrar_equipos():
    """Muestra todos los equipos y su estado actual."""
    print("\n--- INVENTARIO DE EQUIPOS ---")
    if not inventario:
        print("No hay equipos registrados.")
        return
    for equipo, datos in inventario.items():
        estado = "Disponible" if datos["disponible"] else "Prestado"
        print(f"• {equipo}: {estado}")
    print("-----------------------------\n")


def registrar_prestamo():
    """Registra un préstamo de un equipo disponible."""
    from datetime import date

    # Mostrar equipos disponibles
    print("\nEquipos disponibles:")
    disponibles = [equipo for equipo, datos in inventario.items() if datos["disponible"]]
    if not disponibles:
        print("No hay equipos disponibles en este momento.")
        return
    for equipo in disponibles:
        print(f"  - {equipo}")

    # Solicitar nombre exacto del equipo
    equipo = input("\nIngrese el nombre exacto del equipo a prestar: ").strip()
    if equipo not in inventario:
        print(" Error: El equipo no existe en el inventario.")
        return
    if not inventario[equipo]["disponible"]:
        print(" Error: El equipo no está disponible actualmente.")
        return

    # Solicitar usuario y fecha
    usuario = input("Nombre del usuario que solicita el préstamo: ").strip()
    if not usuario:
        print(" El nombre de usuario no puede estar vacío.")
        return

    fecha_actual = date.today().strftime("%Y-%m-%d")
    # Guardar préstamo como tupla inmutable (usuario, fecha)
    prestamo = (usuario, fecha_actual)
    inventario[equipo]["prestamos"].append(prestamo)
    inventario[equipo]["disponible"] = False

    print(f" Préstamo registrado: {equipo} prestado a {usuario} el {fecha_actual}.")

def devolver_equipo():
    """Marca un equipo como devuelto."""
    # Mostrar equipos prestados
    prestados = [equipo for equipo, datos in inventario.items() if not datos["disponible"]]
    if not prestados:
        print("\nNo hay equipos prestados actualmente.")
        return
    print("\nEquipos prestados:")
    for equipo in prestados:
        print(f"  - {equipo}")

    equipo = input("\nIngrese el nombre exacto del equipo a devolver: ").strip()
    if equipo not in inventario:
        print(" Error: El equipo no existe.")
        return
    if inventario[equipo]["disponible"]:
        print(" Error: El equipo ya está disponible (no estaba prestado).")
        return

    inventario[equipo]["disponible"] = True
    print(f" {equipo} ha sido devuelto y ahora está disponible.")


def ver_historial():
    """Muestra el historial de préstamos de todos los equipos."""
    print("\n--- HISTORIAL DE PRÉSTAMOS ---")
    if not inventario:
        print("No hay equipos registrados.")
        return

    for equipo, datos in inventario.items():
        print(f"\n {equipo}:")
        if datos["prestamos"]:
            for i, prestamo in enumerate(datos["prestamos"], 1):
                usuario, fecha = prestamo  # desempaquetamos la tupla
                print(f"   {i}. Usuario: {usuario} - Fecha: {fecha}")
        else:
            print("   Sin préstamos registrados.")
    print("-------------------------------\n")


def agregar_equipo():
    """Agrega un nuevo equipo al inventario."""
    nombre = input("Ingrese el nombre del nuevo equipo: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return
    if nombre in inventario:
        print("Error: El equipo ya existe en el inventario.")
        return

    inventario[nombre] = {
        "disponible": True,
        "prestamos": []
    }
    print(f"Equipo '{nombre}' agregado exitosamente.")


def menu():
    """Menú interactivo principal."""
    while True:
        print("\n" + "="*50)
        print("   SISTEMA DE PRÉSTAMOS DE EQUIPOS")
        print("="*50)
        print("1. Ver equipos disponibles")
        print("2. Registrar préstamo")
        print("3. Devolver equipo")
        print("4. Ver historial de préstamos")
        print("5. Agregar nuevo equipo")
        print("6. Salir")
        print("="*50)

        opcion = input("Seleccione una opción (1-6): ").strip()
        if opcion == "1":
            mostrar_equipos()
        elif opcion == "2":
            registrar_prestamo()
        elif opcion == "3":
            devolver_equipo()
        elif opcion == "4":
            ver_historial()
        elif opcion == "5":
            agregar_equipo()
        elif opcion == "6":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    menu()