# src/mcp/tools/notificaciones.py
"""
🔔 Herramientas MCP para notificaciones
"""

from typing import Dict
from src.scrapers.unvime_scraper import UNVimeScraper
from src.notifiers.manager import NotificationManager
from src.utils.logger import setup_logger


class NotificacionesTools:
    """
    Herramientas MCP para enviar notificaciones.
    """
    
    def __init__(self):
        self.logger = setup_logger("NotificacionesTools")
        self.scraper = UNVimeScraper()
        self.notification_manager = NotificationManager()
    
    def _obtener_todos_eventos(self):
        """Obtiene todos los eventos"""
        contenido_html = self.scraper.descargar_contenido()
        return self.scraper.extraer_eventos(contenido_html)
    
    async def enviar_recordatorio(self, evento_id: int, canal: str) -> Dict:
        """
        Envía un recordatorio de un evento.
        
        Args:
            evento_id: ID del evento
            canal: Canal de notificación (discord, whatsapp, ambos)
            
        Returns:
            Resultado del envío
        """
        try:
            eventos = self._obtener_todos_eventos()
            
            if evento_id < 1 or evento_id > len(eventos):
                return {"error": f"ID inválido. Debe ser entre 1 y {len(eventos)}"}
            
            evento = eventos[evento_id - 1]
            
            # Enviar según el canal
            resultados = {}
            
            if canal in ["discord", "ambos"]:
                discord_result = self.notification_manager.notificar([evento], ["Discord"])
                resultados["discord"] = "enviado" if discord_result else "error"
            
            if canal in ["whatsapp", "ambos"]:
                whatsapp_result = self.notification_manager.notificar([evento], ["WhatsApp"])
                resultados["whatsapp"] = "enviado" if whatsapp_result else "error"
            
            return {
                "success": True,
                "evento": evento.titulo,
                "fecha": evento.fecha.strftime("%Y-%m-%d"),
                "canal": canal,
                "resultados": resultados
            }
            
        except Exception as e:
            self.logger.error(f"Error enviando recordatorio: {e}", exc_info=True)
            return {"error": str(e)}