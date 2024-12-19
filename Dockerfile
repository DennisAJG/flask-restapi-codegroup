# Use a imagem oficial leve do Python
FROM python:3.9-slim

# Definir variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Criar um usuário não-root
RUN adduser --disabled-password --gecos '' appuser

# Criar o diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Instalar dependências Python
COPY apps/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação
COPY apps/ /app

# Alterar propriedade do diretório da aplicação
RUN mkdir -p /app && chown -R appuser:appuser /app

# Alternar para o usuário não-root
USER appuser

# Expor a porta da aplicação
EXPOSE 5000

# Executar a aplicação
CMD ["python", "app.py"]
