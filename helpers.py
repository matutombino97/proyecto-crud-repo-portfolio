def validar_numero(numero: str, campo: str):
    """Verifica que el dato ingresado sea un número entero positivo."""
    numero = numero.strip()
    if not numero.isdigit():
        raise ValueError(f"❌ El dato '{campo}' debe ser un valor numérico entero.")
    
    numero = int(numero)
    if numero < 0:
        raise ValueError(f"❌ El dato '{campo}' no puede ser negativo.")
    
    return numero

def validar_texto(texto: str, campo: str):
    """Verifica que el campo de texto no esté vacío."""
    texto = texto.strip()
    if texto:
        return texto
    else:
        raise ValueError(f"❌ El campo '{campo}' es obligatorio para el registro.")