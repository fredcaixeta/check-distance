# Use uma imagem base do Python
FROM python:3.9-slim

# Copie o arquivo de dependências para o diretório de trabalho
COPY requirements.txt requirements.txt

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o conteúdo do diretório atual para o diretório de trabalho no container
COPY . .

# Exponha a porta em que a aplicação Flask vai rodar
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
