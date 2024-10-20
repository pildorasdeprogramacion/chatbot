# Usar una imagen base de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requerimientos
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Exponer el puerto donde Django correrá
EXPOSE 8000

# Comando para correr la aplicación en modo desarrollo
CMD ["sh", "-c", "python pildoras/manage.py migrate && python pildoras/manage.py runserver 0.0.0.0:8000"]
