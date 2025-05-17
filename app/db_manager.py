import os
import json
from flask_sqlalchemy import SQLAlchemy
from app import db
from app.models_publicos import TiendaEnProceso, TiendaPublica, ProductoBase
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models_tienda import db as db_tienda_modelo
from app.models_tienda import Producto, Cliente, Administrador, Vendedor, Pedido, Compra, ConfiguracionVisual

# Ruta base para las bases de datos de tiendas
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TIENDAS_DIR = os.path.join(BASE_DIR, "instance", "tiendas")
os.makedirs(TIENDAS_DIR, exist_ok=True)

def finalizar_tienda(tienda_id):
    tienda = TiendaEnProceso.query.get(tienda_id)
    if not tienda or tienda.finalizado:
        raise ValueError("Tienda no encontrada o ya finalizada")

    nombre_db = f"{tienda.nombre_tienda}.db"
    ruta_db = os.path.abspath(os.path.join(TIENDAS_DIR, nombre_db))  # ✅ RUTA ABSOLUTA

    # Crear engine y session
    engine = create_engine(f"sqlite:///{ruta_db}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Crear tablas
    db_tienda_modelo.Model.metadata.create_all(bind=engine)

    # Insertar productos seleccionados
    productos_ids = json.loads(tienda.productos_seleccionados)
    productos_base = ProductoBase.query.filter(ProductoBase.id.in_(productos_ids)).all()

    for p in productos_base:
        producto = Producto(
            nombre=p.nombre,
            tipo=p.tipo,
            descripcion="",
            precio=p.precio,
            imagen_url=p.imagen_url,
            stock=20,
            categoria=p.categoria,
            sabor="",
            caladas=p.caladas
        )
        session.add(producto)

    # Insertar configuración visual
    configuracion = ConfiguracionVisual(
        color_principal=tienda.color_principal,
        color_secundario=tienda.color_secundario,
        color_fondo=tienda.color_fondo,
        logo_url=tienda.logo_url,

    )
    session.add(configuracion)

    # Registrar tienda públicamente si no existe
    tienda_publica = TiendaPublica.query.filter_by(nombre_tienda=tienda.nombre_tienda).first()

    if not tienda_publica:
        tienda_publica = TiendaPublica(
            nombre_tienda=tienda.nombre_tienda,
            email_contacto=tienda.email,
            fecha_creacion=datetime.utcnow(),
            tipo_web=tienda.tipo_web,
            plantilla_seleccionada=tienda.plantilla_seleccionada
        )
        db.session.add(tienda_publica)


    # ✅ SIEMPRE actualiza la ruta
    tienda_publica.ruta_db = ruta_db


    tienda.finalizado = True
    tienda.ruta_db_tienda = ruta_db

    session.commit()
    session.close()
    db.session.commit()

    return f"Tienda '{tienda.nombre_tienda}' finalizada correctamente."