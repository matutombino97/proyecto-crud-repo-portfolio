from utils import generar_id, pausar
from helpers import validar_texto, validar_numero
from archivos import guardar_csv

def mostrar_producto(producto):
    """Muestra la tarjeta de información de un arma/item"""
    print(f"📜 ID Registro: #{producto['id']}")
    print(f"⚔️  Arma/Item:   {producto['nombre']}")
    print(f"💰 Costo:       {producto['precio']} Ryos")
    print(f"📦 Reservas:    {producto['stock']} unidades")
    print(f"🏷️  Clase:       {producto['categoria']}")
    print("-" * 40)

def agregar_prods(productos: list) -> list:
    """Registra una nueva arma en el inventario"""
    print("\n--- ⚔️ FORJA DE NUEVA ARMA ---")
    try:
        nombre = validar_texto(input("Nombre del Arma/Item: "), "nombre")
        precio = validar_numero(input("Costo de fabricación (Ryos): "), "precio")
        stock = validar_numero(input("Cantidad inicial en almacén: "), "stock")
        categoria = validar_texto(input("Clase (Ej: Arrojadiza, Curativa): "), "categoría").lower()

        nuevo_producto = {
            "id": generar_id(productos),
            "nombre": nombre,
            "precio": precio,
            "stock": stock,
            "categoria": categoria
        }

        productos.append(nuevo_producto)
        print(f"\n✨ ¡{nombre} ha sido registrada en el pergamino!")
        guardar_csv(productos)

    except ValueError as e:
        print("❌ Error en el forjado:", e)

    return productos


def editar_prods(productos: list):
    """Modifica los datos de un arma existente"""
    print("\n--- 🛠️ MESA DE REPARACIONES ---")
    try:
        id_buscar = input("Ingrese el ID del item a modificar: ").strip()

        if not id_buscar.isdigit():
            raise ValueError("El ID debe ser numérico.")

        id_buscar = int(id_buscar)

        for prod in productos:
            if int(prod['id']) == id_buscar:
                print("\nItem identificado:")
                mostrar_producto(prod)

                print("""
    ¿Qué atributo desea modificar?
    [1] Renombrar Arma
    [2] Actualizar Costo (Ryos)
    [3] Ajustar Reservas (Stock)
    [4] Cambiar Clase/Categoría
    [0] Cancelar
                """)

                opcion = input(">> Opción: ").strip()

                if opcion == "1":
                    prod['nombre'] = validar_texto(input("Nuevo nombre: "), "nombre")

                elif opcion == "2":
                    prod['precio'] = validar_numero(input("Nuevo costo (Ryos): "), "precio")

                elif opcion == "3":
                    prod['stock'] = validar_numero(input("Nueva cantidad en reserva: "), "stock")

                elif opcion == "4":
                    prod['categoria'] = validar_texto(input("Nueva clase: "), "categoría").lower()

                elif opcion == "0":
                    print("🛠️ Modificación cancelada.")
                    return productos

                else:
                    print("❌ Opción desconocida.")
                    return productos

                print(f"\n✅ Registro de '{prod['nombre']}' actualizado.")
                guardar_csv(productos)
                return productos

        print("❌ No se encontró ningún item con ese ID en los pergaminos.")

    except ValueError as e:
        print("❌ Error:", e)

    return productos


def eliminar_prods(productos: list):
    """Elimina un arma del inventario"""
    print("\n--- 🔥 DESTRUCCIÓN DE REGISTROS ---")
    id_buscar = input("ID del item a retirar/destruir: ").strip()

    if not id_buscar.isdigit():
        print("❌ El ID debe ser un número.")
        return productos

    id_buscar = int(id_buscar)

    for prod in productos:
        if int(prod['id']) == id_buscar:
            print("\nItem localizado:")
            mostrar_producto(prod)

            opcion = input("¿Seguro que desea QUEMAR este registro? (s/n): ").strip().lower()

            if opcion != 's':
                print("Operación abortada. El item sigue seguro.")
                return productos

            productos.remove(prod)
            print(f"🔥 El registro de '{prod['nombre']}' ha sido reducido a cenizas.")

            guardar_csv(productos)
            return productos

    print("❌ No se encontró ese ID para eliminar.")
    return productos