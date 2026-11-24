FROM python:3.12-slim 

# genera el entorno en donde se va a ejecutar el proyecto
WORKDIR /app

# carga las dependencias a la raiz del proyecto principal
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src/
COPY wsgi.py .

# exposición de un puerto 
EXPOSE 8000

# son ejecutables que el cmd por debajo realiza, aquí se permite inicializar los ejecutables
CMD ["gunicorn", "--workers", "1" "--bind", "0.0.0.0:8000", "wsgi:app"]