from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from app import db

class Producto(db.Model):
    __tablename__ = "producto"  
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    precio = db.Column(db.Float, nullable=False)
    imagen_url = db.Column(db.String(255))
    stock = db.Column(db.Integer, default=0)
    categoria = db.Column(db.String(50))
    tipo = db.Column(db.String(50))
    caladas = db.Column(db.Integer)

class Cliente(db.Model):
    __tablename__ = "cliente"  
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(255))
    password_hash = db.Column(db.String(255), nullable=False)  # 🔐 Contraseña hasheada

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Administrador(db.Model):
    __tablename__ = "administrador"  
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    contraseña = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), unique=True)


class Pedido(db.Model):
    __tablename__ = "pedido" 
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    estado = db.Column(db.String(50))
    total = db.Column(db.Float)

    cliente = db.relationship('Cliente', backref='pedidos')

class Compra(db.Model):
    __tablename__ = "compra"  
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

    pedido = db.relationship('Pedido', backref='compras')
    producto = db.relationship('Producto')

class ConfiguracionVisual(db.Model):
    __tablename__ = "configuracion_visual"
    id = db.Column(db.Integer, primary_key=True)

    color_principal = db.Column(db.String(7))
    color_secundario = db.Column(db.String(7))
    color_fondo = db.Column(db.String(7))
    logo_url = db.Column(db.String(255))
    plantilla = db.Column(db.String(50))

    # Campos nuevos
    titulo_tienda = db.Column(db.String(255), nullable=True)
    imagenes_tienda = db.Column(db.Text, nullable=True)
    descripcion_portfolio = db.Column(db.Text, nullable=True)
    imagen_portfolio = db.Column(db.String(255), nullable=True)
    sobre_nosotros = db.Column(db.Text, nullable=True)
    servicios_portfolio = db.Column(db.Text, nullable=True)

