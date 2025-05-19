from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from app import db

# 🔹 Tiendas ya creadas (registro final)
class TiendaPublica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_tienda = db.Column(db.String(100), unique=True, nullable=False)
    email_contacto = db.Column(db.String(120), nullable=False)
    ruta_db = db.Column(db.String(255), nullable=False)  # Ruta al archivo .db de la tienda
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

# 🔹 Catálogo base de productos que se usan como plantilla inicial
class ProductoBase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)  
    categoria = db.Column(db.String(50), nullable=False)  
    nombre = db.Column(db.String(100), nullable=False)
    caladas = db.Column(db.Integer, nullable=True)
    precio = db.Column(db.Float)
    imagen_url = db.Column(db.String(255))

# 🔹 Proceso de creación de tienda paso a paso
class TiendaEnProceso(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Paso 1: Datos personales
    nombre = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefono = db.Column(db.String(20))

    nombre_tienda = db.Column(db.String(100), unique=True, nullable=False)

    # Paso 2: Estilo visual
    color_principal = db.Column(db.String(7))
    color_secundario = db.Column(db.String(7))
    color_fondo = db.Column(db.String(7))
    logo_url = db.Column(db.String(255))  
    tipo_web = db.Column(db.String(50))
    plantilla = db.Column(db.String(50))

    # Campos nuevos
    
    # Campos nuevos
    titulo_tienda = db.Column(db.String(255), nullable=True)
    imagenes_tienda = db.Column(db.Text, nullable=True)
    descripcion_portfolio = db.Column(db.Text, nullable=True)
    imagen_portfolio = db.Column(db.String(255), nullable=True)
    sobre_nosotros = db.Column(db.Text, nullable=True)
    servicios_portfolio = db.Column(db.Text, nullable=True)



    # Paso 3: Productos seleccionados
    productos_seleccionados = db.Column(db.Text)

    # Estado del progreso
    paso_actual = db.Column(db.Integer, default=1)
    finalizado = db.Column(db.Boolean, default=False)
    ruta_db_tienda = db.Column(db.String(255))

    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
