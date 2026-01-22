import csv
import os

# Ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Ruta correcta al CSV
DATA_PATH = os.path.join(BASE_DIR, "data", "productos.csv")


def convertir_csv_dict():
    """Lee el pergamino CSV y lo convierte en una lista de diccionarios."""
    productos = []

    # Si el archivo no existe, devolvemos lista vacía
    if not os.path.exists(DATA_PATH):
        return productos

    try:
        with open(DATA_PATH, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for fila in reader:
                productos.append(fila)
    except Exception as e:
        print(f"⚠️ Error al leer el pergamino: {e}")

    return productos


def guardar_csv(productos: list):
    """Escribe los datos actuales en el pergamino CSV."""
    try:
        # Aseguramos que la carpeta 'data' exista
        os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)

        with open(DATA_PATH, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "nombre", "precio", "stock", "categoria"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for prod in productos:
                writer.writerow({
                    "id": prod["id"],
                    "nombre": prod["nombre"],
                    "precio": prod["precio"],
                    "stock": prod["stock"],
                    "categoria": prod["categoria"]
                })

        # Mensaje discreto de guardado (opcional, a veces es mejor que sea silencioso)
        # print("💾 Pergamino (CSV) actualizado y sellado correctamente.")
        
    except Exception as e:
        print(f"❌ Error crítico al guardar el pergamino: {e}")