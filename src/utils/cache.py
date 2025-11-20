# src/utils/cache.py
"""
💾 Sistema de caché para eventos del calendario
Evita descargar el calendario múltiples veces
"""

import json
import pickle
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Optional, List
from src.utils.logger import setup_logger


class Cache:
    """
    Sistema simple de caché en archivo.
    Guarda eventos en disco para evitar scraping repetido.
    """
    
    def __init__(self, cache_dir: str = "cache", ttl_hours: int = 6):
        """
        Inicializa el sistema de caché.
        
        Args:
            cache_dir: Directorio donde guardar caché
            ttl_hours: Tiempo de vida del caché en horas
        """
        self.logger = setup_logger("Cache")
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
        self.ttl = timedelta(hours=ttl_hours)
    
    def get(self, key: str) -> Optional[Any]:
        """
        Obtiene un valor del caché.
        
        Args:
            key: Clave del caché
            
        Returns:
            Valor guardado o None si no existe o expiró
        """
        cache_file = self.cache_dir / f"{key}.cache"
        
        if not cache_file.exists():
            self.logger.debug(f"Cache miss: {key}")
            return None
        
        try:
            with open(cache_file, 'rb') as f:
                data = pickle.load(f)
            
            # Verificar si expiró
            timestamp = data.get('timestamp')
            if datetime.now() - timestamp > self.ttl:
                self.logger.debug(f"Cache expired: {key}")
                cache_file.unlink()
                return None
            
            self.logger.debug(f"Cache hit: {key}")
            return data.get('value')
            
        except Exception as e:
            self.logger.warning(f"Error leyendo caché {key}: {e}")
            return None
    
    def set(self, key: str, value: Any) -> bool:
        """
        Guarda un valor en el caché.
        
        Args:
            key: Clave del caché
            value: Valor a guardar
            
        Returns:
            True si se guardó correctamente
        """
        cache_file = self.cache_dir / f"{key}.cache"
        
        try:
            data = {
                'timestamp': datetime.now(),
                'value': value
            }
            
            with open(cache_file, 'wb') as f:
                pickle.dump(data, f)
            
            self.logger.debug(f"Cache saved: {key}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error guardando caché {key}: {e}")
            return False
    
    def clear(self, key: Optional[str] = None):
        """
        Limpia el caché.
        
        Args:
            key: Clave específica o None para limpiar todo
        """
        if key:
            cache_file = self.cache_dir / f"{key}.cache"
            if cache_file.exists():
                cache_file.unlink()
                self.logger.info(f"Cache cleared: {key}")
        else:
            for cache_file in self.cache_dir.glob("*.cache"):
                cache_file.unlink()
            self.logger.info("All cache cleared")


# Instancia global de caché
_cache_instance = None


def get_cache() -> Cache:
    """Obtiene la instancia global del caché"""
    global _cache_instance
    if _cache_instance is None:
        _cache_instance = Cache()
    return _cache_instance