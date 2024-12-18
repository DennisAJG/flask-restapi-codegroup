# Usar uma imagem leve e confiável
FROM python:3.10-slim

# Criar e usar um usuário não root
RUN addgroup --system appgroup && adduser --system --group appuser

# Configuração básica
WORKDIR /app

# Instalar dependências necessárias do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Instalar dependências Python com hash fixo
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação
COPY . .

# Definir permissões para o usuário não root
RUN chown -R appuser:appgroup /app

# Alternar para o usuário não root
USER appuser

# Expor a porta da aplicação
EXPOSE 5000

# Comando para executar o app
CMD ["python", "app.py"]
