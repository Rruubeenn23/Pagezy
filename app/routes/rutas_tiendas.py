import os
from flask import Blueprint, render_template
from sqlalchemy import create_engine, MetaData, Table
from app.models_publicos import TiendaPublica
import random


# Crear blueprint para las tiendas públicas
tienda_bp = Blueprint('tienda_publica', __name__, url_prefix="/tiendas")

@tienda_bp.route("/<nombre_tienda>")
def ver_tienda(nombre_tienda):
    tienda_publica = TiendaPublica.query.filter_by(nombre_tienda=nombre_tienda).first_or_404()

    engine = create_engine(f"sqlite:///{tienda_publica.ruta_db}")
    metadata = MetaData()
    metadata.reflect(bind=engine)

    config_table = metadata.tables["configuracion_visual"]
    producto_table = metadata.tables["producto"]

    with engine.connect() as connection:
        config_data = connection.execute(config_table.select()).mappings().fetchone()
        configuracion = {
            "color_principal": config_data["color_principal"],
            "color_secundario": config_data["color_secundario"],
            "color_fondo": config_data["color_fondo"],
            "logo_url": config_data["logo_url"],
            "plantilla": config_data.get("plantilla", "tienda_1")
        }

        productos_result = connection.execute(producto_table.select()).mappings().fetchall()
        productos = [dict(row) for row in productos_result]
        productos = random.sample(productos, min(5, len(productos)))  # <-- ALEATORIOS

    return render_template(f"PaginasTiendas/plantillas/{configuracion['plantilla']}.html",
                           config=configuracion,
                           productos=productos,
                           nombre_tienda=tienda_publica.nombre_tienda)


