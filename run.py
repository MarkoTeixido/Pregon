# run.py
"""
🚀 Script principal de ejecución de Pregon
Sistema de calendario académico UNViMe con IA
"""

import sys
import asyncio
from dotenv import load_dotenv

load_dotenv()

from src.utils.logger import setup_logger

logger = setup_logger("Main")


def mostrar_menu():
    """Muestra el menú principal"""
    print("="*70)
    print("🤖 PREGON - Sistema de Calendario Académico UNViMe")
    print("="*70)
    print()
    print("Selecciona qué ejecutar:")
    print()
    print("1. Bot de Discord (interactivo con IA)")
    print("2. Webhook de WhatsApp (servidor)")
    print("3. MCP Server (Model Context Protocol)")
    print("4. Salir")
    print()
    print("="*70)


def run_discord():
    """Ejecuta el bot de Discord"""
    from src.integrations.discord_bot import PregonDiscordBot
    
    logger.info("🚀 Iniciando bot de Discord...")
    bot = PregonDiscordBot()
    bot.run()


def run_whatsapp():
    """Ejecuta el webhook de WhatsApp"""
    from src.integrations.whatsapp_webhook import run_webhook_server
    
    logger.info("📱 Iniciando webhook de WhatsApp...")
    run_webhook_server(port=5000)


async def run_mcp():
    """Ejecuta el servidor MCP"""
    from src.mcp.server import main as mcp_main
    
    logger.info("="*70)
    logger.info("🔌 PREGON - MCP SERVER")
    logger.info("="*70)
    logger.info("")
    logger.info("Servidor MCP iniciado. Esperando conexiones...")
    logger.info("")
    
    await mcp_main()


def main():
    """Punto de entrada principal"""
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ").strip()
        
        if opcion == "1":
            run_discord()
            break
        
        elif opcion == "2":
            run_whatsapp()
            break
        
        elif opcion == "3":
            asyncio.run(run_mcp())
            break
        
        elif opcion == "4":
            print("👋 ¡Hasta luego!")
            sys.exit(0)
        
        else:
            print("❌ Opción inválida. Intenta de nuevo.\n")


if __name__ == "__main__":
    main()