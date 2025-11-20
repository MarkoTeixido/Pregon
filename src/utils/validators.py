# src/utils/validators.py
"""
✅ Validadores de datos para el sistema
"""

import re
from datetime import datetime
from typing import Optional, Tuple


def validar_fecha(fecha: str, formato: str = "%Y-%m-%d") -> Tuple[bool, Optional[datetime]]:
    """
    Valida una fecha en string.
    
    Args:
        fecha: String de fecha
        formato: Formato esperado
        
    Returns:
        (es_valida, fecha_parseada)
    """
    try:
        fecha_obj = datetime.strptime(fecha, formato)
        return True, fecha_obj
    except ValueError:
        return False, None


def validar_email(email: str) -> bool:
    """
    Valida un email.
    
    Args:
        email: Email a validar
        
    Returns:
        True si es válido
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validar_url(url: str) -> bool:
    """
    Valida una URL.
    
    Args:
        url: URL a validar
        
    Returns:
        True si es válida
    """
    pattern = r'^https?://[^\s/$.?#].[^\s]*$'
    return bool(re.match(pattern, url))


def validar_categoria(categoria: str) -> bool:
    """
    Valida una categoría de evento.
    
    Args:
        categoria: Categoría a validar
        
    Returns:
        True si es válida
    """
    categorias_validas = [
        "academico", "examen", "feriado", 
        "institucional", "receso", "otro"
    ]
    return categoria.lower() in categorias_validas


def validar_rango_fechas(fecha_inicio: str, fecha_fin: str) -> bool:
    """
    Valida que un rango de fechas sea coherente.
    
    Args:
        fecha_inicio: Fecha de inicio
        fecha_fin: Fecha de fin
        
    Returns:
        True si el rango es válido
    """
    valida_inicio, inicio = validar_fecha(fecha_inicio)
    valida_fin, fin = validar_fecha(fecha_fin)
    
    if not valida_inicio or not valida_fin:
        return False
    
    return inicio <= fin


def sanitizar_texto(texto: str) -> str:
    """
    Limpia y sanitiza un texto.
    
    Args:
        texto: Texto a limpiar
        
    Returns:
        Texto sanitizado
    """
    # Eliminar espacios extras
    texto = " ".join(texto.split())
    
    # Eliminar caracteres especiales peligrosos
    texto = re.sub(r'[<>\"\'&]', '', texto)
    
    return texto.strip()