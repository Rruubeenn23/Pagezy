from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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
    sabor = db.Column(db.String(100))
    caladas = db.Column(db.Integer)

class Cliente(db.Model):
    __tablename__ = "cliente"  
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(255))
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

class Administrador(db.Model):
    __tablename__ = "administrador"  
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    contraseña = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), unique=True)

class Vendedor(db.Model):
    __tablename__ = "vendedor"  
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    contraseña = db.Column(db.String(255), nullable=False)

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
