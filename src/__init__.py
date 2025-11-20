# src/__init__.py
"""
🎓 Pregon - Sistema de Calendario Académico UNViMe
Sistema inteligente de notificaciones con IA
"""

__version__ = "1.0.0"
__author__ = "Marko Teixido"

# Exports principales
from src.scrapers.unvime_scraper import UNVimeScraper
from src.models.evento import Evento
from src.ai.chatbot import CalendarioChatbot
from src.mcp.server import PregonMCPServer

__all__ = [
    'UNVimeScraper',
    'Evento',
    'CalendarioChatbot',
    'PregonMCPServer',
    '__version__'
]