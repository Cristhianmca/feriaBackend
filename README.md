# django Feria Mañanera
ecommerce api con django y django rest framework

# Para crear el entorno virtual
1. python -m venv venv
2. source venv/Scripts/activate
3. pip install -r requirements.txt

# Para crear el proyecto
1. django-admin startproject ecommerce .
2. python manage.py startapp api

# Despues de haber creado las tablas 
1. python manage.py makemigrations
2. python manage.py migrate