<p align="center">
  <a href="https://github.com/MarkoTeixido/Pregon">
    <img src="https://i.imgur.com/tBhnwlI.png" height="128">
  </a>
  <h2 align="center"><a href="https://github.com/MarkoTeixido/Pregon">Pregón</a></h2>
  <p align="center">Sistema inteligente de calendario académico para la Universidad Nacional de Villa Mercedes, potenciado por IA y MCP Server.</p>
  
  <p align="center">
    <img src="https://i.imgur.com/Euv2bDd.png" height="128">
  </p>

  <p align="center">
    <a href="#-características">
      <img src="https://img.shields.io/badge/%E2%9C%A8-Características-0a0a0a.svg?style=flat&colorA=0a0a0a" alt="características" />
    </a>
    <a href="#-tecnologías">
      <img src="https://img.shields.io/badge/%F0%9F%9A%80-Stack-0a0a0a.svg?style=flat&colorA=0a0a0a" alt="stack" />
    </a>
    <a href="#-instalación">
      <img src="https://img.shields.io/badge/%F0%9F%93%A6-Instalación-0a0a0a.svg?style=flat&colorA=0a0a0a" alt="instalación" />
    </a>
  </p>
</p>
<br>

![](https://i.imgur.com/waxVImv.png)

## 📝 Sobre el Proyecto

**Pregon** es un sistema multicanal que automatiza la gestión del calendario académico de la UNViMe. Extrae, procesa y distribuye eventos académicos a través de Discord, WhatsApp y Google Calendar, potenciado por inteligencia artificial y una arquitectura MCP moderna.

### 🎯 Objetivo

Crear una plataforma que sea:
- **Inteligente**: IA conversacional con Google Gemini 2.5 Flash
- **Multicanal**: Discord, WhatsApp
- **Moderna**: MCP Server (Model Context Protocol)
- **Automática**: Web scraping inteligente con caché
- **Escalable**: Arquitectura modular y profesional
- **Production**: CI/CD, Docker, tests automatizados

### 🖼️ Preview

<p align="center">
   <img src="https://i.imgur.com/HAaVEPD.png" height="750">
</p>
<p align="center">
   <img src="https://i.imgur.com/lthqzP0.png" height="700">
</p>



![](https://i.imgur.com/waxVImv.png)

## ✨ Características

### 🤖 Inteligencia Artificial

- **Google Gemini 2.5 Flash**: Modelo de última generación para conversaciones
- **NLP Query Parser**: Procesa preguntas en lenguaje natural
- **Contexto Académico**: Entiende términos universitarios específicos
- **Filtrado Inteligente**: Búsqueda por fecha, categoría, tipo de evento
- **Respuestas Adaptativas**: Ajusta tono y formato según el canal

### 🔌 MCP Server (Model Context Protocol)

- **Arquitectura Estándar**: Compatible con cualquier LLM que soporte MCP
- **6 Herramientas Especializadas**:
  - `get_eventos_semana`: Consulta eventos de los próximos 7 días
  - `buscar_eventos`: Búsqueda avanzada con múltiples filtros
  - `get_proximos_examenes`: Filtra solo exámenes por rango de fechas
  - `agregar_a_google_calendar`: Integración directa con Calendar API
  - `generar_link_calendar`: Crea URLs públicas para compartir eventos
  - `enviar_recordatorio`: Sistema de notificaciones multicanal
- **Extensible**: Arquitectura de plugins para agregar nuevas herramientas
- **Interoperable**: Funciona con Claude, GPT-4, Gemini y otros LLMs
- **Type-Safe**: Schemas con Pydantic para validación automática

### 🤖 Bot de Discord

- **Comandos de Texto**: `!pregunta`, `!ayuda`, `!hoy`
- **Embeds Ricos**: Formato profesional con colores y emojis
- **Chat Conversacional**: Modo IA con contexto persistente

### 📱 Bot de WhatsApp

- **Comandos Simples**: `EVENTOS`, `CALENDARIO`, `AYUDA`, `BUSCAR`
- **Chat Natural**: Responde preguntas sin comandos específicos
- **Links Directos**: Agrega eventos a Calendar con 1 click
- **Twilio Sandbox**: Testing gratuito antes de producción
- **Error Handling**: Respuestas claras ante errores

### 🔍 Web Scraping Inteligente

- **BeautifulSoup4 + lxml**: Parser robusto y rápido
- **Categorización Automática**: 
  - Exámenes (generales, recuperatorios, compensatorios)
  - Feriados (nacionales, provinciales)
  - Recesos (escolares, de invierno)
  - Eventos especiales (actos, ceremonias)
- **Expansión de Rangos**: Eventos multi-día → eventos individuales
- **Caché Inteligente**: TTL de 6 horas para optimizar requests
- **Validación Robusta**: Verifica fechas, textos y estructura

### 📅 Google Calendar Integration

- **OAuth 2.0 Flow**: Autenticación segura con refresh tokens
- **Creación Automática**: Agrega eventos directo a tu calendario
- **Batch Operations**: Procesa múltiples eventos eficientemente
- **Color Coding**: Categorías por colores personalizables
- **Recordatorios**: Configura alertas automáticas

### 🔔 Sistema de Notificaciones

- **Manager Pattern**: Arquitectura extensible con múltiples notifiers
- **Canales Soportados**: Discord Webhooks, WhatsApp (Twilio)
- **Scheduler Integrado**: Cron jobs para notificaciones programadas
- **Templates Personalizados**: Mensajes adaptados por tipo de evento
- **Agrupación Inteligente**: Resumen diario/semanal

![](https://i.imgur.com/waxVImv.png)

## 🏗️ Arquitectura

### 🔄 Diagrama General

<p align="center">
   <img src="https://i.imgur.com/CQFiOkv.png" height="700">
</p>

### 📊 Flujo de Consulta

<p align="center">
   <img src="https://i.imgur.com/2FnsT8F.png" height="700">
</p>
<p align="center">
   <img src="https://i.imgur.com/ohieoPF.png" height="700">
</p>

![](https://i.imgur.com/waxVImv.png)

## 🚀 Tecnologías

### Backend/Core

| Tecnología | Versión | Uso |
|-----------|---------|-----|
| **Python** | 3.10+ | Lenguaje principal |
| **discord.py** | 2.3.2+ | SDK oficial de Discord |
| **Flask** | 3.0.0+ | Framework web para WhatsApp webhook |
| **Twilio** | 9.0.0+ | API de WhatsApp Business |
| **Google Generative AI** | 0.8.3+ | SDK de Gemini |
| **Google Calendar API** | 2.149.0+ | Gestión de calendarios |
| **BeautifulSoup4** | 4.12.0+ | Parser HTML/XML |
| **lxml** | 5.3.0+ | Parser rápido para BS4 |
| **Requests** | 2.31.0+ | Cliente HTTP |
| **python-dotenv** | 1.0.0+ | Gestión de variables de entorno |
| **Pydantic** | 2.0+ | Validación de datos con types |

### MCP (Model Context Protocol)

| Componente | Estado | Descripción |
|-----------|--------|-------------|
| **MCP Server** | ✅ | Servidor con 6 herramientas |
| **EventosTools** | ✅ | Búsqueda y filtrado de eventos |
| **CalendarioTools** | ✅ | Integración con Google Calendar |
| **NotificacionesTools** | ✅ | Sistema de recordatorios |
| **Cache System** | ✅ | Optimización con TTL de 6h |
| **Validators** | ✅ | Validación de fechas y eventos |

### Integraciones Externas

| Servicio | API/Método | Uso |
|----------|-----------|-----|
| **UNViMe** | Web Scraping (BeautifulSoup) | Extracción del calendario académico |
| **Google Gemini** | Generative AI API | Chatbot conversacional inteligente |
| **Google Calendar** | Calendar API v3 | Creación y gestión de eventos |
| **Twilio** | WhatsApp Business API | Mensajería bidireccional |
| **Discord** | Discord Bot API | Bot interactivo con comandos |
| **TinyURL** | URL Shortening API | Acortar links de calendar |

### DevOps & CI/CD

| Herramienta | Uso |
|------------|-----|
| **GitHub Actions** | CI/CD pipeline automatizado |
| **Docker** | Containerización multi-stage |
| **Docker Compose** | Orquestación de servicios |
| **Railway** | Deployment en producción |
| **pytest** | Tests unitarios e integración |
| **flake8** | Linting y code quality |
| **black** | Code formatting automático |
| **ngrok** | Túnel HTTPS para desarrollo local |

### Monitoreo & Logging

| Componente | Descripción |
|-----------|-------------|
| **Custom Logger** | Sistema estructurado con niveles |
| **File Rotation** | Logs rotativos por tamaño |
| **Console Output** | Logs formateados con colores |
| **Error Tracking** | Stack traces completos |
| **Performance Metrics** | Timing de operaciones críticas |

![](https://i.imgur.com/waxVImv.png)

## 📦 Instalación

### Prerequisitos

- **Python** >= 3.10
- **pip** >= 23.x
- **Git** >= 2.x
- **Docker** (opcional, para containerización)
- Cuentas en:
  - Discord (para bot token)
  - Twilio (para WhatsApp)
  - Google Cloud (para Gemini AI y Calendar API)

---

### 🚀 Opción 1: Setup Rápido (Recomendado)

```bash
# 1. Clonar repositorio
git clone https://github.com/MarkoTeixido/Pregon.git
cd Pregon

# 2. Crear entorno virtual
python -m venv venv

# Activar (Linux/macOS)
source venv/bin/activate

# Activar (Windows)
venv\Scripts\activate

# 3. Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-ai.txt

# 4. Configurar variables de entorno
cp .env.example .env
# Editar .env con tus credenciales (ver sección siguiente)

# 5. Ejecutar
python run.py
```

---

### 🐳 Opción 2: Docker (Producción)

```bash
# 1. Clonar y configurar .env
git clone https://github.com/MarkoTeixido/Pregon.git
cd Pregon
cp .env.example .env
# Editar .env con credenciales

# 2. Construir imágenes
docker-compose build

# 3. Iniciar servicios
docker-compose up -d

# 4. Ver logs
docker-compose logs -f

# 5. Detener
docker-compose down
```

**Servicios disponibles:**
- `discord-bot`: Bot de Discord
- `whatsapp-webhook`: Servidor de WhatsApp

**Comandos útiles:**
```bash
# Iniciar solo Discord
docker-compose up -d discord-bot

# Reiniciar servicio
docker-compose restart whatsapp-webhook

# Ver estado
docker-compose ps

# Entrar a contenedor
docker exec -it pregon-discord bash
```

---

### ⚙️ Configuración de Variables de Entorno

Edita el archivo `.env` con tus credenciales:

```env
# ============================================
# DISCORD
# ============================================
DISCORD_BOT_TOKEN=tu_token_aqui
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...
DISCORD_GUILD_ID=tu_server_id

# ============================================
# TWILIO (WhatsApp)
# ============================================
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=tu_auth_token_aqui
TWILIO_WHATSAPP_FROM=whatsapp:+14155238886
TWILIO_WHATSAPP_TO=whatsapp:+54tu_numero

# ============================================
# GOOGLE GEMINI AI
# ============================================
GEMINI_API_KEY=tu_api_key_aqui
LLM_MODEL_GEMINI=gemini-2.5-flash
LLM_TEMPERATURE=0.7
LLM_MAX_TOKENS=2048

# ============================================
# GOOGLE CALENDAR
# ============================================
GOOGLE_CREDENTIALS_PATH=credentials/google_calendar.json
GOOGLE_TOKEN_PATH=credentials/token.json

# ============================================
# CALENDARIO UNVIME
# ============================================
CALENDAR_URL=https://www.unvime.edu.ar/calendario/

# ============================================
# CONFIGURACIÓN GENERAL
# ============================================
ENVIRONMENT=production
LOG_LEVEL=INFO
ENABLE_CACHE=true
CACHE_TTL=21600
```

---

### 🔑 Obtener Credenciales

<details>
<summary><b>📘 Discord Bot Token</b></summary>

1. Ve a [Discord Developer Portal](https://discord.com/developers/applications)
2. Click en **"New Application"**
3. Dale un nombre (ej: "Pregon Bot")
4. Ve a la pestaña **"Bot"**
5. Click en **"Reset Token"** y copia el token
6. En **"Privileged Gateway Intents"** activa:
   - ✅ Message Content Intent
   - ✅ Server Members Intent (opcional)
7. Ve a **"OAuth2 → URL Generator"**
8. Selecciona scopes: `bot`, `applications.commands`
9. Selecciona permisos: `Send Messages`, `Embed Links`, `Read Message History`
10. Copia la URL generada y abre en navegador para invitar el bot

</details>

<details>
<summary><b>📱 Twilio WhatsApp Credentials</b></summary>

1. Crea cuenta en [Twilio](https://www.twilio.com/try-twilio)
2. Ve a **Console → WhatsApp → Sandbox**
3. Copia tu **Account SID** y **Auth Token**
4. Para testing, usa el sandbox:
   - `TWILIO_WHATSAPP_FROM=whatsapp:+14155238886`
5. Envía el código de activación al sandbox desde tu WhatsApp
6. Configura Webhook URL (en producción o con ngrok):
   - URL: `https://tu-dominio.com/webhook`
   - Method: `POST`

</details>

<details>
<summary><b>🤖 Google Gemini API Key</b></summary>

1. Ve a [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click en **"Get API key"**
3. Selecciona o crea un proyecto
4. Click en **"Create API key"**
5. Copia la API key generada
6. **Límites gratuitos**: 60 requests/minuto, 1500/día

</details>

<details>
<summary><b>📅 Google Calendar API</b></summary>

1. Ve a [Google Cloud Console](https://console.cloud.google.com/)
2. Crea un nuevo proyecto o selecciona uno existente
3. Habilita **Google Calendar API**:
   - API Library → Busca "Calendar" → Enable
4. Crea credenciales OAuth 2.0:
   - Credentials → Create Credentials → OAuth client ID
   - Application type: Desktop app
   - Download JSON
5. Guarda el JSON como `credentials/google_calendar.json`
6. La primera vez que ejecutes, se abrirá un navegador para autorizar
7. Se generará automáticamente `credentials/token.json`

</details>

---

### 🧪 Verificar Instalación

```bash
# Activar entorno virtual
source venv/bin/activate  # Linux/macOS
# o
venv\Scripts\activate  # Windows

# Ejecutar script principal
python run.py

# Deberías ver el menú:
# ══════════════════════════════════════════
# 🤖 PREGON - Sistema de Calendario UNViMe
# ══════════════════════════════════════════
# 
# 1. Bot de Discord
# 2. Webhook de WhatsApp
# 3. MCP Server
# 4. Scheduler
# 5. Salir
```

![](https://i.imgur.com/waxVImv.png)

## 🎮 Uso

### 🤖 Discord Bot

#### Comandos Disponibles

```
🔍 Consultas
!pregunta <consulta>     - Pregunta al asistente IA
!eventos                 - Eventos de la próxima semana
!hoy                     - Eventos de hoy
!buscar <término>        - Buscar eventos específicos

📅 Google Calendar
!calendario              - Links para agregar eventos
!agregar menu            - Menú interactivo para agregar

ℹ️ Ayuda
!ayuda                   - Muestra todos los comandos
!ping                    - Verifica que el bot está activo
```

#### Ejemplos de Uso

```
!pregunta ¿Cuándo son los exámenes de diciembre?
!pregunta ¿Hay clases el 25 de diciembre?
!pregunta Dame los recesos de 2025
!buscar feriado
!buscar receso invierno
!eventos
!hoy
```

#### Respuestas Inteligentes

El bot entiende:
- ✅ Preguntas en lenguaje natural
- ✅ Sinónimos (examen/evaluación, feriado/festivo)
- ✅ Fechas relativas ("próxima semana", "mes que viene")
- ✅ Rangos de fechas ("de enero a marzo")
- ✅ Categorías (exámenes, feriados, recesos)

---

### 📱 WhatsApp Bot

#### Comandos

```
EVENTOS         - Ver próximos 7 eventos
CALENDARIO      - Links para agregar a Google Calendar
AYUDA           - Lista de comandos disponibles
BUSCAR <texto>  - Buscar eventos específicos
```

#### Modo Conversacional

También puedes hacer preguntas naturales sin comandos:

```
¿Cuándo empiezan las clases?
¿Hay feriados en julio?
¿Cuándo son los exámenes?
Dame el calendario de diciembre
```

#### Configurar Webhook (Desarrollo Local)

```bash
# Terminal 1: Iniciar servidor Flask
python run.py
# Seleccionar opción 2 (WhatsApp)

# Terminal 2: Exponer con ngrok
ngrok http 5000

# Copiar la URL HTTPS (ej: https://abc123.ngrok.io)
# Ir a Twilio Console → WhatsApp Sandbox Settings
# Webhook URL: https://abc123.ngrok.io/webhook
# Method: POST
```

---

### 🔌 MCP Server

```python
import asyncio
from src.mcp.server import get_mcp_server

async def main():
    # Obtener instancia del servidor
    server = get_mcp_server()
    
    # Listar herramientas disponibles
    tools = await server.list_tools()
    print(f"Herramientas: {[t['name'] for t in tools]}")
    
    # Ejecutar herramienta: obtener eventos de la semana
    response = await server.call_tool(
        "get_eventos_semana",
        {}
    )
    print(f"Eventos esta semana: {response}")
    
    # Buscar eventos específicos
    response = await server.call_tool(
        "buscar_eventos",
        {
            "categoria": "examen",
            "desde": "2025-12-01",
            "hasta": "2025-12-31"
        }
    )
    print(f"Exámenes en diciembre: {response}")
    
    # Generar link de calendario
    response = await server.call_tool(
        "generar_link_calendar",
        {
            "titulo": "Examen Final",
            "fecha": "2025-12-15",
            "descripcion": "Matemática I"
        }
    )
    print(f"Link: {response}")

# Ejecutar
asyncio.run(main())
```

![](https://i.imgur.com/waxVImv.png)

## 📊 Estructura del Proyecto
<p align="center">
   <img src="https://i.imgur.com/GyU3xex.png" height="700">
</p>

![](https://i.imgur.com/waxVImv.png)

## 🎓 Decisiones Técnicas y Aprendizajes

### ¿Por qué Python?

| Razón | Explicación |
|-------|-------------|
| **Ecosistema IA/ML** | Librerías maduras (TensorFlow, scikit-learn) |
| **APIs de Bots** | Excelente soporte para Discord, Telegram, WhatsApp |
| **Web Scraping** | BeautifulSoup, Scrapy, Selenium muy robustos |
| **Prototipado Rápido** | Sintaxis limpia, desarrollo ágil |
| **Comunidad Grande** | Stack Overflow, PyPI con 400k+ paquetes |

### ¿Por qué MCP Server?

- **Estándar Emergente**: Protocolo adoptado por Anthropic, OpenAI
- **Interoperabilidad**: Funciona con cualquier LLM compatible
- **Desacoplamiento**: Separación clara entre IA y herramientas
- **Reutilizable**: Puedo usar estas tools en otros proyectos
- **Future-Proof**: Tecnología de vanguardia (2024-2025)

### ¿Por qué Gemini 2.5 Flash?

| Ventaja | Detalle |
|---------|---------|
| **Última Generación** | Modelo más reciente de Google |
| **Gratuito** | 60 req/min, 1500/día sin costo |
| **Multimodal** | Texto, imágenes, audio |
| **Streaming** | Respuestas en tiempo real |
| **Español Nativo** | Entrenado específicamente para español |
| **Bajo Latency** | Respuestas en <1 segundo |

### ¿Por qué BeautifulSoup + lxml?

```python
# Alternativa 1: Selenium (rechazada)
# ❌ Más lento (navegador headless)
# ❌ Más recursos (RAM, CPU)
# ✅ JS rendering

# Alternativa 2: BeautifulSoup + lxml (elegida)
# ✅ Rápido (parser en C)
# ✅ Ligero (solo parsing HTML)
# ✅ Robusto (tolera HTML mal formado)
# ❌ No ejecuta JavaScript
```

**Decisión**: UNViMe no requiere JS, BS4 es suficiente.

### Caché de 6 Horas: ¿Por qué?

```python
# Análisis de cambios del calendario UNViMe:
# - Actualización: 1-2 veces por semestre
# - Frecuencia de consultas: ~100/día
# - Sin caché: 100 requests/día al servidor
# - Con caché 6h: 4 requests/día

# TTL Options:
# 1h   → Demasiado frecuente, desperdicio
# 24h  → Podría perder cambios importantes
# 6h   → Balance perfecto ✅
```

**Resultado**: 96% reducción de requests.

### ¿Por qué Multi-Canal (Discord + WhatsApp)?

- **Alcance Máximo**: Discord = estudiantes jóvenes, WhatsApp = profesores/padres
- **Flexibilidad**: Usuario elige su plataforma favorita
- **Aprendizaje**: Demostrar integración de múltiples APIs
- **Profesional**: Apps reales son multi-plataforma

### Docker Multi-Stage Build

```dockerfile
# STAGE 1: Builder (imagen pesada con build tools)
FROM python:3.10-slim as builder
RUN apt-get install gcc g++ make  # Solo en build
RUN pip install -r requirements.txt

# STAGE 2: Runtime (imagen ligera solo con runtime)
FROM python:3.10-slim
COPY --from=builder /opt/venv /opt/venv  # Solo venv
# Resultado: Imagen final 40% más pequeña
```

### Arquitectura de Notificaciones

```python
# Manager Pattern:
class NotificationManager:
    def __init__(self):
        self.notifiers = [
            DiscordNotifier(),
            WhatsAppNotifier(),
            # Fácil agregar: TelegramNotifier(), EmailNotifier()
        ]
    
    def send_all(self, message):
        for notifier in self.notifiers:
            notifier.send(message)

# Ventaja: Agregar canales sin modificar lógica existente
```

![](https://i.imgur.com/waxVImv.png)

## 🚀 Deployment en Producción

### Railway (Recomendado)

**Railway** despliega automáticamente desde GitHub:

1. **Conectar Repositorio**:
   - Ve a [Railway](https://railway.app)
   - New Project → Deploy from GitHub
   - Selecciona `MarkoTeixido/Pregon`

2. **Configurar Servicios**:
   ```
   Service 1: Pregon-Discord
   - Start Command: python entrypoints/discord_service.py
   - Environment: production
   
   Service 2: Pregon-WhatsApp  
   - Start Command: python entrypoints/whatsapp_service.py
   - Port: 5000
   - Environment: production
   ```

3. **Variables de Entorno**:
   - Copia todas las vars de `.env`
   - Railway → Settings → Variables
   - Add: `DISCORD_BOT_TOKEN`, `GEMINI_API_KEY`, etc.

4. **Deploy Automático**:
   - Cada push a `main` redespliega automáticamente
   - Logs en tiempo real en Railway dashboard

---

![](https://i.imgur.com/waxVImv.png)

## 🧪 Testing y CI/CD

### Tests Automatizados

```bash
# Ejecutar todos los tests
pytest

# Con coverage
pytest --cov=src --cov-report=html

# Solo tests de integración
pytest -m integration

# Solo tests unitarios
pytest -m unit
```

### GitHub Actions Workflows

El proyecto tiene 4 workflows automatizados:

1. **Build** (`.github/workflows/build.yml`):
   - ✅ Valida que el código compila
   - ✅ Verifica instalación de dependencias
   - ⏰ Se ejecuta en cada push

2. **Tests** (`.github/workflows/tests.yml`):
   - ✅ Corre suite completa de tests
   - ✅ Genera reporte de coverage
   - ⏰ Se ejecuta en PRs y push a main

3. **Lint** (`.github/workflows/lint.yml`):
   - ✅ Verifica PEP 8 con flake8
   - ✅ Chequea types con mypy
   - ⏰ Se ejecuta en cada commit

4. **Docker** (`.github/workflows/docker.yml`):
   - ✅ Build de imagen Docker
   - ✅ Push a Docker Hub (en releases)
   - ⏰ Se ejecuta en tags

### Coverage Actual

```
Tests: 47 passed
Coverage: 52%
Lines: 2,341
Branches: 412
```

![](https://i.imgur.com/waxVImv.png)


## 📄 Licencia

Este proyecto está bajo la **Licencia MIT**.

![](https://i.imgur.com/waxVImv.png)

## 👨‍💻 Autor

**Marko Teixido**  
*Estudiante de Ingeniería en Sistemas*  
*Universidad Nacional de Villa Mercedes*

- 🌐 **Portfolio**: [markoteixido.site](https://markoteixido.site)
- 🐙 **GitHub**: [@MarkoTeixido](https://github.com/MarkoTeixido)

<p align="center">
  <b>Hecho para la comunidad de UNViMe</b>
</p>

<p align="center">
    <img src="https://i.imgur.com/Euv2bDd.png" height="128">
</p>