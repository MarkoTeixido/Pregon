# src/mcp/tools/calendario.py
"""
📆 Herramientas MCP para Google Calendar
"""

from typing import Dict
from src.integrations.google_calendar_service import GoogleCalendarService
from src.integrations.calendar_link_generator import CalendarLinkGenerator
from src.scrapers.unvime_scraper import UNVimeScraper
from src.utils.logger import setup_logger


class CalendarioTools:
    """
    Herramientas MCP para integración con Google Calendar.
    """
    
    def __init__(self):
        self.logger = setup_logger("CalendarioTools")
        self.google_calendar = GoogleCalendarService()
        self.link_generator = CalendarLinkGenerator()
        self.scraper = UNVimeScraper()
    
    def _obtener_todos_eventos(self):
        """Obtiene todos los eventos"""
        contenido_html = self.scraper.descargar_contenido()
        return self.scraper.extraer_eventos(contenido_html)
    
    async def agregar_evento(self, evento_id: int) -> Dict:
        """
        Agrega un evento a Google Calendar.
        
        Args:
            evento_id: ID del evento a agregar
            
        Returns:
            Resultado de la operación
        """
        try:
            # Obtener todos los eventos
            eventos = self._obtener_todos_eventos()
            
            if evento_id < 1 or evento_id > len(eventos):
                return {"error": f"ID inválido. Debe ser entre 1 y {len(eventos)}"}
            
            evento = eventos[evento_id - 1]
            
            # Agregar a Google Calendar
            resultado = self.google_calendar.agregar_evento(evento)
            
            if resultado:
                return {
                    "success": True,
                    "evento": evento.titulo,
                    "fecha": evento.fecha.strftime("%Y-%m-%d"),
                    "link": resultado.get("link")
                }
            else:
                return {"error": "No se pudo agregar el evento"}
                
        except Exception as e:
            self.logger.error(f"Error agregando evento: {e}", exc_info=True)
            return {"error": str(e)}
    
    async def generar_link(self, evento_id: int) -> Dict:
        """
        Genera un link público de Google Calendar.
        
        Args:
            evento_id: ID del evento
            
        Returns:
            Link generado
        """
        try:
            eventos = self._obtener_todos_eventos()
            
            if evento_id < 1 or evento_id > len(eventos):
                return {"error": f"ID inválido. Debe ser entre 1 y {len(eventos)}"}
            
            evento = eventos[evento_id - 1]
            
            link = self.link_generator.generar_link(evento)
            
            return {
                "success": True,
                "evento": evento.titulo,
                "fecha": evento.fecha.strftime("%Y-%m-%d"),
                "link": link
            }
            
        except Exception as e:
            self.logger.error(f"Error generando link: {e}", exc_info=True)
            return {"error": str(e)}