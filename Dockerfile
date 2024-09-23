# Utiliza una imagen oficial de Python como base
FROM python:3.12

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requerimientos y el código fuente al contenedor
COPY requirements.txt /app/

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código del proyecto
COPY . /app/

# Exponer el puerto en el que Django corre (8000 por defecto)
EXPOSE 8000

# Definir el comando por defecto para correr la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
