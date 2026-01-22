import sys
from time import sleep

# Importaciones de tus módulos (Mantenemos la lógica intacta)
from archivos import convertir_csv_dict, guardar_csv
from crud import agregar_prods, editar_prods, eliminar_prods, mostrar_producto
from utils import pausar, generar_id
from helpers import validar_texto, validar_numero
from consultas import (
    filtrar_por_precio, sin_stock, filtrar_prod_por_categoria, 
    buscar_por_nombre, buscar_por_rango, stock_critico, 
    cantidad_por_categoria, precio_promedio, stock_total, 
    producto_mas_caro_barato
)
from reportes.reportes import exportar_reportes_csv, exportar_reportes_json, exportar_reportes_txt

def mostrar_logo():
    print("""
    KONOHA
    >>> SISTEMA DE LOGÍSTICA SHINOBI <<<
    """)

def mostrar_menu():
    print("\n" + "="*40)
    print(" 📜  PERGAMINO DE OPCIONES (MENÚ)")
    print("="*40)
    print(" [1]  Consultar Armas y Herramientas")
    print(" [2]  Filtrar por Costo (Ryos)")
    print(" [3]  ⚠️  Reporte de Escasez (Sin Stock)")
    print(" [4]  Filtrar por Tipo (Categoría)")
    print("-" * 40)
    print(" [5]  ⚔️  Forjar Nueva Arma (Crear)")
    print(" [6]  🛠️  Modificar Suministros (Editar)")
    print(" [7]  🔥  Destruir/Retirar Arma (Eliminar)")
    print("-" * 40)
    print(" [8]  🔍  Rastrear por Nombre")
    print(" [9]  💰  Búsqueda por Presupuesto (Rango)")
    print(" [10] 🚨  Alerta de Stock Crítico (<5)")
    print("-" * 40)
    print(" [11] 📊  Estadísticas de la Aldea")
    print(" [12] 💾  Exportar Datos (CSV)")
    print(" [13] 💾  Exportar Datos (JSON)")
    print(" [14] 💾  Exportar Datos (TXT)")
    print("="*40)
    print(" [0]  🏃 Escapar (Salir y Guardar)")
    print("="*40)

def salir_del_sistema(inventario):
    """Maneja la salida segura y el guardado de datos"""
    while True:
        confirm = input("\n¿Desea sellar los cambios en el pergamino antes de huir? (s/n): ").strip().lower()
        if confirm == "s":
            guardar_csv(inventario)
            print("\n💾 Progreso guardado. ¡Buen viaje, Ninja! 🍃")
            sys.exit()
        elif confirm == "n":
            print("\n💨 Desapareciendo entre las sombras... (Sin guardar)")
            sys.exit()
        else:
            print("❌ Jutsu inválido. Responda 's' o 'n'.")

if __name__ == '__main__':
    # Carga inicial de datos
    try:
        inventario = convertir_csv_dict()
        mostrar_logo()
        print(f"✅ Conexión establecida. Items cargados: {len(inventario)}")
        sleep(1) 
    except Exception as e:
        print(f"❌ Error crítico al cargar la base de datos: {e}")
        sys.exit()

    # Bucle Principal
    while True:
        mostrar_menu()
        opcion = input(">> Elija su misión (Número): ").strip()

        if not opcion.isdigit():
            print("❌ Error: Debe ingresar un número de misión válido.")
            pausar()
            continue

        opcion = int(opcion)

        # Bloque de ejecución seguro (Un solo Try/Except para todo)
        try:
            if opcion == 1: # Listar
                print("\n--- 📜 INVENTARIO COMPLETO ---")
                for item in inventario:
                    mostrar_producto(item)
            
            elif opcion == 2: # Filtro Precio
                precio = input("Ingrese costo mínimo (Ryos): ").strip()
                if precio.isdigit():
                    filtrados = filtrar_por_precio(inventario, int(precio))
                    print(f"\nItems con valor superior a {precio} Ryos: {len(filtrados)}")
                    for item in filtrados: mostrar_producto(item)
                else:
                    print("❌ El costo debe ser numérico.")

            elif opcion == 3: # Sin Stock
                sin = sin_stock(inventario)
                print(f"\n⚠️ ALERTA: {len(sin)} items agotados en la armería.")
                for item in sin: mostrar_producto(item)

            elif opcion == 4: # Categoría
                cat = input("Ingrese tipo de arma/item: ").strip().lower()
                filtrados = filtrar_prod_por_categoria(inventario, cat)
                if filtrados:
                    print(f"\nResultados para '{cat}': {len(filtrados)}")
                    for item in filtrados: mostrar_producto(item)
                else:
                    print("❌ No se encontraron items de ese tipo.")

            elif opcion == 5: # Crear
                agregar_prods(inventario)
                print("✨ ¡Nueva arma forjada y registrada!")

            elif opcion == 6: # Editar
                editar_prods(inventario)
                print("🛠️ Registro actualizado correctamente.")

            elif opcion == 7: # Eliminar
                eliminar_prods(inventario)
                print("🔥 Item eliminado del registro.")

            elif opcion == 8: # Buscar Nombre
                nombre = input("Nombre clave a buscar: ").strip()
                encontrados = buscar_por_nombre(inventario, nombre)
                print(f"\nCoincidencias encontradas: {len(encontrados)}")
                for item in encontrados: mostrar_producto(item)

            elif opcion == 9: # Rango Precios
                try:
                    min_p = int(input("Presupuesto mínimo: "))
                    max_p = int(input("Presupuesto máximo: "))
                    encontrados = buscar_por_rango(inventario, min_p, max_p)
                    print(f"\nItems entre {min_p} y {max_p} Ryos: {len(encontrados)}")
                    for item in encontrados: mostrar_producto(item)
                except ValueError:
                    print("❌ Debes ingresar números enteros.")

            elif opcion == 10: # Stock Crítico
                criticos = stock_critico(inventario)
                print(f"\n🚨 URGENTE: {len(criticos)} items con reservas bajas (<5).")
                for item in criticos: mostrar_producto(item)

            elif opcion == 11: # Estadísticas
                print("\n📊 --- ESTADÍSTICAS DE LA ALDEA ---")
                print(f"Total de reservas: {stock_total(inventario)} unidades")
                print(f"Costo promedio: {precio_promedio(inventario):.2f} Ryos")
                print(f"Distribución por tipo: {cantidad_por_categoria(inventario)}")
                
                caro, barato = producto_mas_caro_barato(inventario)
                if caro and barato:
                    print("\n💎 Item más valioso:")
                    mostrar_producto(caro)
                    print("\n📉 Item más accesible:")
                    mostrar_producto(barato)

            elif opcion == 12: # CSV
                ruta = "proyecto_Crud/reportes/productos_reportes.csv"
                if exportar_reportes_csv(inventario, ruta): print(f"✅ Reporte CSV generado.")
                else: print("❌ Error en la exportación.")

            elif opcion == 13: # JSON
                ruta = "proyecto_Crud/reportes/productos_reportes.json"
                if exportar_reportes_json(inventario, ruta): print(f"✅ Reporte JSON generado.")
                else: print("❌ Error en la exportación.")

            elif opcion == 14: # TXT
                if not inventario: print("❌ Inventario vacío.")
                else:
                    ruta = "proyecto_Crud/reportes/productos_reportes.txt"
                    if exportar_reportes_txt(inventario, ruta): print(f"✅ Reporte TXT generado.")
                    else: print("❌ Error en la exportación.")

            elif opcion == 0: # Salir
                salir_del_sistema(inventario)

            else:
                print("❌ Misión desconocida. Intente nuevamente.")

        except Exception as e:
            print(f"\n💥 Ocurrió un error inesperado en el sistema: {e}")
            print("Contacte al equipo de desarrollo de Konoha.")
        
        pausar()