#!/usr/bin/env python3
# entrypoints/whatsapp_service.py
"""
📱 Entry point para el servicio WhatsApp Webhook
Diseñado para ambientes de producción con Gunicorn
"""

import sys
import os
from pathlib import Path

# Agregar el directorio raíz al path
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))

from dotenv import load_dotenv
from src.utils.logger import setup_logger

# Cargar variables de entorno
load_dotenv()

logger = setup_logger("WhatsAppService")


def main():
    """
    Punto de entrada principal para el servicio WhatsApp.
    
    En producción, este servicio usa Gunicorn.
    Para desarrollo local, usa Flask directamente.
    """
    from src.integrations.whatsapp_webhook import app
    from src.config.settings import settings
    
    logger.info("="*70)
    logger.info("📱 PREGON - WHATSAPP WEBHOOK SERVICE")
    logger.info("="*70)
    logger.info(f"Environment: {settings.environment}")
    logger.info(f"Version: {settings.version}")
    logger.info("")
    
    # Validar credenciales Twilio
    if not settings.twilio_account_sid or not settings.twilio_auth_token:
        logger.error("❌ ERROR: Credenciales de Twilio no configuradas")
        logger.error("💡 Configura TWILIO_ACCOUNT_SID y TWILIO_AUTH_TOKEN")
        sys.exit(1)
    
    # Configurar puerto (Railway asigna PORT automáticamente)
    port = int(os.getenv('PORT', 5000))
    
    # Detectar si estamos en Railway/producción
    is_production = os.getenv('RAILWAY_ENVIRONMENT') is not None or settings.environment == 'production'
    
    try:
        if is_production:
            logger.info(f"🚀 Modo PRODUCCIÓN detectado")
            logger.info(f"📡 Puerto asignado: {port}")
            logger.info(f"🔧 Usa Gunicorn para iniciar este servicio")
            logger.info(f"   Comando: gunicorn -w 2 -b 0.0.0.0:{port} src.integrations.whatsapp_webhook:app")
            logger.info("")
            logger.info("⚠️  Este script se ejecutará automáticamente con Gunicorn en Railway")
            
            # En Railway, Gunicorn inicia directamente el app
            # Este script solo sirve para validación inicial
            return app
        else:
            logger.info(f"🔧 Modo DESARROLLO detectado")
            logger.info(f"🚀 Iniciando webhook de WhatsApp en puerto {port}...")
            logger.info(f"📡 Endpoint: /webhook")
            logger.info(f"🏥 Health check: /health")
            logger.info("")
            logger.info("✅ Servidor listo para recibir mensajes")
            
            # Iniciar Flask solo en desarrollo
            app.run(
                host='0.0.0.0',
                port=port,
                debug=False,
                use_reloader=False
            )
        
    except KeyboardInterrupt:
        logger.info("⚠️ Servidor detenido por usuario (Ctrl+C)")
        sys.exit(0)
        
    except Exception as e:
        logger.error(f"❌ Error crítico iniciando servidor: {e}", exc_info=True)
        sys.exit(1)


# Para Gunicorn
app = None
if __name__ != "__main__":
    from src.integrations.whatsapp_webhook import app

if __name__ == "__main__":
    main()