# Dockerfile
# Multi-stage build para imagen optimizada

# ============================================
# STAGE 1: Builder
# ============================================
FROM python:3.10-slim as builder

# Variables de entorno para build
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Directorio de trabajo
WORKDIR /app

# Instalar dependencias de sistema necesarias para build
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    make \
    libxml2-dev \
    libxslt-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements
COPY requirements.txt requirements-ai.txt ./

# Instalar dependencias en venv
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install -r requirements-ai.txt

# ============================================
# STAGE 2: Runtime
# ============================================
FROM python:3.10-slim

# Variables de entorno
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/opt/venv/bin:$PATH" \
    ENVIRONMENT=production

# Crear usuario no-root
RUN useradd -m -u 1000 pregon && \
    mkdir -p /app /app/logs /app/cache /app/credentials && \
    chown -R pregon:pregon /app

# Instalar dependencias de runtime
RUN apt-get update && apt-get install -y --no-install-recommends \
    libxml2 \
    libxslt1.1 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copiar venv desde builder
COPY --from=builder /opt/venv /opt/venv

# Establecer directorio de trabajo
WORKDIR /app

# Copiar código fuente
COPY --chown=pregon:pregon . .

# Cambiar a usuario no-root
USER pregon

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "print('OK')" || exit 1

# Exponer puerto (si se usa webhook)
EXPOSE 5000

# Comando por defecto
CMD ["python", "run.py"]