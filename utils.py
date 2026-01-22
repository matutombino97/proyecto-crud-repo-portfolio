import os

def generar_id(productos: list) -> int:
    """Genera un ID autoincremental basado en el último ID existente."""
    if not productos:
        return 1
    return max(int(p["id"]) for p in productos) + 1

def pausar():
    """Pausa la ejecución hasta que el usuario decida continuar."""
    input("\n🥷 Presione [Enter] para continuar la misión...")
    # Limpia la pantalla según el sistema operativo (Opcional, pero queda pro)
    os.system('cls' if os.name == 'nt' else 'clear')