# src/mcp/server.py
"""
🔌 MCP Server para Pregon
Expone herramientas del calendario académico vía MCP Protocol
"""

import asyncio
import json
from typing import Any, Dict, List, Optional
from dataclasses import dataclass, asdict

from src.mcp.tools.eventos import EventosTools
from src.mcp.tools.calendario import CalendarioTools
from src.mcp.tools.notificaciones import NotificacionesTools
from src.utils.logger import setup_logger


@dataclass
class MCPTool:
    """Definición de una herramienta MCP"""
    name: str
    description: str
    input_schema: Dict[str, Any]


@dataclass
class MCPResponse:
    """Respuesta de una herramienta MCP"""
    content: List[Dict[str, str]]
    isError: bool = False


class PregonMCPServer:
    """
    Servidor MCP que expone funcionalidades del calendario académico.
    
    Implementa el protocolo MCP para permitir que LLMs accedan
    a los datos del calendario de manera estandarizada.
    """
    
    def __init__(self):
        self.logger = setup_logger("MCPServer")
        
        # Inicializar herramientas
        self.eventos_tools = EventosTools()
        self.calendario_tools = CalendarioTools()
        self.notificaciones_tools = NotificacionesTools()
        
        # Definir herramientas disponibles
        self.tools = self._define_tools()
        
        self.logger.info(f"MCP Server inicializado con {len(self.tools)} herramientas")
    
    def _define_tools(self) -> List[MCPTool]:
        """Define todas las herramientas disponibles"""
        return [
            MCPTool(
                name="get_eventos_semana",
                description="Obtiene los eventos de la próxima semana del calendario académico UNViMe",
                input_schema={
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            ),
            MCPTool(
                name="buscar_eventos",
                description="Busca eventos por texto, categoría o rango de fechas",
                input_schema={
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Texto a buscar en título o descripción"
                        },
                        "categoria": {
                            "type": "string",
                            "description": "Categoría de evento",
                            "enum": ["examen", "academico", "feriado", "institucional", "receso", "otro"]
                        },
                        "desde": {
                            "type": "string",
                            "description": "Fecha desde (YYYY-MM-DD)"
                        },
                        "hasta": {
                            "type": "string",
                            "description": "Fecha hasta (YYYY-MM-DD)"
                        }
                    }
                }
            ),
            MCPTool(
                name="get_proximos_examenes",
                description="Obtiene los próximos exámenes programados",
                input_schema={
                    "type": "object",
                    "properties": {
                        "dias": {
                            "type": "integer",
                            "description": "Número de días a futuro (default: 30)",
                            "default": 30
                        }
                    }
                }
            ),
            MCPTool(
                name="agregar_a_google_calendar",
                description="Agrega un evento específico a Google Calendar del usuario",
                input_schema={
                    "type": "object",
                    "properties": {
                        "evento_id": {
                            "type": "integer",
                            "description": "ID del evento a agregar (del 1 al N)"
                        }
                    },
                    "required": ["evento_id"]
                }
            ),
            MCPTool(
                name="generar_link_calendar",
                description="Genera un link público de Google Calendar para un evento",
                input_schema={
                    "type": "object",
                    "properties": {
                        "evento_id": {
                            "type": "integer",
                            "description": "ID del evento"
                        }
                    },
                    "required": ["evento_id"]
                }
            ),
            MCPTool(
                name="enviar_recordatorio",
                description="Envía un recordatorio de un evento por Discord o WhatsApp",
                input_schema={
                    "type": "object",
                    "properties": {
                        "evento_id": {
                            "type": "integer",
                            "description": "ID del evento"
                        },
                        "canal": {
                            "type": "string",
                            "description": "Canal de notificación",
                            "enum": ["discord", "whatsapp", "ambos"]
                        }
                    },
                    "required": ["evento_id", "canal"]
                }
            ),
        ]
    
    def list_tools(self) -> List[Dict[str, Any]]:
        """
        Lista todas las herramientas disponibles.
        
        Returns:
            Lista de herramientas en formato MCP
        """
        return [asdict(tool) for tool in self.tools]
    
    async def call_tool(self, name: str, arguments: Optional[Dict[str, Any]] = None) -> MCPResponse:
        """
        Ejecuta una herramienta por su nombre.
        
        Args:
            name: Nombre de la herramienta
            arguments: Argumentos de la herramienta
            
        Returns:
            Respuesta de la herramienta
        """
        if arguments is None:
            arguments = {}
        
        self.logger.info(f"Ejecutando herramienta: {name} con args: {arguments}")
        
        try:
            # Ejecutar herramienta correspondiente
            if name == "get_eventos_semana":
                result = await self.eventos_tools.get_eventos_semana()
            
            elif name == "buscar_eventos":
                result = await self.eventos_tools.buscar_eventos(
                    query=arguments.get("query"),
                    categoria=arguments.get("categoria"),
                    desde=arguments.get("desde"),
                    hasta=arguments.get("hasta")
                )
            
            elif name == "get_proximos_examenes":
                result = await self.eventos_tools.get_proximos_examenes(
                    dias=arguments.get("dias", 30)
                )
            
            elif name == "agregar_a_google_calendar":
                result = await self.calendario_tools.agregar_evento(
                    evento_id=arguments["evento_id"]
                )
            
            elif name == "generar_link_calendar":
                result = await self.calendario_tools.generar_link(
                    evento_id=arguments["evento_id"]
                )
            
            elif name == "enviar_recordatorio":
                result = await self.notificaciones_tools.enviar_recordatorio(
                    evento_id=arguments["evento_id"],
                    canal=arguments["canal"]
                )
            
            else:
                raise ValueError(f"Herramienta desconocida: {name}")
            
            # Formatear respuesta
            return MCPResponse(
                content=[{
                    "type": "text",
                    "text": json.dumps(result, indent=2, ensure_ascii=False)
                }],
                isError=False
            )
            
        except Exception as e:
            self.logger.error(f"Error ejecutando {name}: {e}", exc_info=True)
            return MCPResponse(
                content=[{
                    "type": "text",
                    "text": f"Error: {str(e)}"
                }],
                isError=True
            )
    
    def get_capabilities(self) -> Dict[str, Any]:
        """
        Retorna las capacidades del servidor MCP.
        
        Returns:
            Diccionario con capacidades
        """
        return {
            "tools": True,
            "resources": False,  # Por ahora no implementamos resources
            "prompts": False,     # Por ahora no implementamos prompts
            "logging": True
        }
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Serializa el servidor a diccionario para export.
        
        Returns:
            Representación en diccionario
        """
        return {
            "name": "pregon-calendario",
            "version": "1.0.0",
            "description": "MCP Server para calendario académico UNViMe",
            "capabilities": self.get_capabilities(),
            "tools": self.list_tools()
        }


# Instancia global del servidor
_server_instance = None


def get_mcp_server() -> PregonMCPServer:
    """
    Obtiene la instancia global del servidor MCP (Singleton).
    
    Returns:
        Instancia del servidor
    """
    global _server_instance
    if _server_instance is None:
        _server_instance = PregonMCPServer()
    return _server_instance