def filtrar_por_precio(productos: list, precio_min: int) -> list:
    """
    Filtra los items que cuestan más que el precio base.
    Ideal para encontrar armamento de élite.
    """
    return [p for p in productos if int(p['precio']) > precio_min]


def sin_stock(productos: list) -> list:
    """
    Identifica los items agotados en el almacén.
    ¡Alerta de reabastecimiento necesaria!
    """
    return [p for p in productos if int(p['stock']) == 0]


def filtrar_prod_por_categoria(productos: list, categoria: str) -> list:
    """
    Recupera todos los items de una clase específica (ej: 'arrojadiza').
    """
    return [p for p in productos if p['categoria'].lower() == categoria.lower()]


def buscar_por_nombre(productos: list, texto: str) -> list:
    """
    Jutsu de Rastreo: Busca coincidencias parciales en los nombres.
    """
    texto = texto.lower().strip()
    return [p for p in productos if texto in p["nombre"].lower()]


def buscar_por_rango(productos: list, minimo: int, maximo: int) -> list:
    """
    Encuentra items que se ajusten al presupuesto de la misión.
    """
    return [p for p in productos if minimo <= int(p["precio"]) <= maximo]


def stock_critico(productos: list, limite: int = 5) -> list:
    """
    Detecta items con reservas peligrosamente bajas (por defecto < 5).
    """
    return [p for p in productos if int(p["stock"]) < limite]


def cantidad_por_categoria(productos: list) -> dict:
    """
    Genera un reporte de inteligencia sobre cuántos items hay por clase.
    """
    conteo = {}
    for p in productos:
        cat = p["categoria"].lower()
        # Lógica simplificada: si existe suma 1, si no, empieza en 0 y suma 1
        conteo[cat] = conteo.get(cat, 0) + 1
    return conteo


def precio_promedio(productos: list) -> float:
    """
    Calcula el costo promedio del arsenal de la aldea.
    """
    if not productos:
        return 0.0
    total = sum(int(p["precio"]) for p in productos)
    return total / len(productos)


def stock_total(productos: list) -> int:
    """
    Cuenta la cantidad total de unidades (items físicos) en la aldea.
    """
    return sum(int(p["stock"]) for p in productos)


def producto_mas_caro_barato(productos: list):
    """
    Identifica el Tesoro de la Aldea (Más caro) y el Item Básico (Más barato).
    """
    if not productos:
        return None, None

    mas_caro = max(productos, key=lambda p: int(p["precio"]))
    mas_barato = min(productos, key=lambda p: int(p["precio"]))

    return mas_caro, mas_barato