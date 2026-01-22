import csv 
import os
import json
from consultas import cantidad_por_categoria, stock_total, precio_promedio, producto_mas_caro_barato

def exportar_reportes_csv(productos, ruta_salida):
    try:
        with open(ruta_salida ,'w', newline="", encoding='utf-8') as file:
            fieldnames = ['nombre','precio','stock','categoria']
            writer = csv.DictWriter(file, fieldnames = fieldnames)
            
            writer.writeheader()

            for prod in productos:
                row = {clave: str(prod[clave]) for clave in fieldnames}
                writer.writerow(row)

        return True

    except Exception as e:
        print('Error: ',e)

        return False


def exportar_reportes_json(productos, ruta_salida) :
    try:
        with open(ruta_salida ,'w', newline="", encoding='utf-8') as files:
           json.dump(productos, files, indent = 4, ensure_ascii= False)
        
        return True
    
    except Exception as e:
        print('Error', e)
        return False
    

def exportar_reportes_txt(productos, ruta_salida):
    try:
        with open(ruta_salida, 'w', encoding='utf-8') as file:
            
            file.write("REPORTE DE PRODUCTOS\n")
            file.write("---------------------\n\n")

            # Obtener datos
            cantidad = cantidad_por_categoria(productos)
            stock = stock_total(productos)
            precio = precio_promedio(productos)
            caro, barato = producto_mas_caro_barato(productos)

            # Escribir datos simples
            file.write(f"Precio promedio: ${precio:.2f}\n")
            file.write(f"Stock total acumulado: {stock} unidades\n\n")

            # Escribir categorías
            file.write("Productos por categoría:\n")
            for cat, cant in cantidad.items():
                file.write(f"  - {cat}: {cant}\n")

            file.write("\n")

            # Producto más caro
            file.write("Producto más caro:\n")
            file.write(f"  Nombre: {caro['nombre']}\n")
            file.write(f"  Precio: ${caro['precio']}\n\n")

            # Producto más barato
            file.write("Producto más barato:\n")
            file.write(f"  Nombre: {barato['nombre']}\n")
            file.write(f"  Precio: ${barato['precio']}\n\n")

        return True
    
    except Exception as e:
        print("Error:", e)
        return False




