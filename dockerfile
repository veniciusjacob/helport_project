# Imagem base
FROM python:3.9

# Diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar os arquivos para o diretório de trabalho
COPY . /app

# Instalar as dependências
RUN pip install -r requirements.txt

# Executar o script create_database.py para criar o banco de dados
RUN python create_database.py

# Comando para iniciar o bot no contêiner
CMD [ "python", "telegram_bot.py" ]

