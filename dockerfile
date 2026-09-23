# imagem que vai utilizar
FROM python:3.12-slim
# qual pasta a aplicação vai morar dentro do container
WORKDIR /app
# copia os arquivos de dependencia e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# copia o resto do codigo fonte
COPY . .
# qual porta a aplicação usa
EXPOSE 5000
# comando para ligar a aplicação
CMD ["python", "app.py"]