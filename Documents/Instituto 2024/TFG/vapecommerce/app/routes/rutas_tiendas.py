import os
from flask import Blueprint, render_template
from sqlalchemy import create_engine, MetaData, Table
from app.models_publicos import TiendaPublica
import random
import json


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
        imagenes = []
        if config_data["imagenes_tienda"]:
            try:
                imagenes = json.loads(config_data["imagenes_tienda"])
            except Exception:
                imagenes = []
        configuracion = {
            "color_principal": config_data["color_principal"],
            "color_secundario": config_data["color_secundario"],
            "color_fondo": config_data["color_fondo"],
            "logo_url": config_data["logo_url"],
            "plantilla": config_data.get("plantilla", "tienda_1"),
            "descripcion_portfolio": config_data.get("descripcion_portfolio"),
            "imagen_portfolio": config_data.get("imagen_portfolio"),
            "sobre_nosotros": config_data.get("sobre_nosotros"),
            "servicios_portfolio": config_data.get("servicios_portfolio")
        }

        productos_result = connection.execute(producto_table.select()).mappings().fetchall()
        productos = [dict(row) for row in productos_result]
        productos = random.sample(productos, min(8, len(productos)))  # <-- ALEATORIOS

    return render_template(f"PaginasTiendas/plantillas/{configuracion['plantilla']}.html",
                            config=configuracion,
                            productos=productos,
                            nombre_tienda=tienda_publica.nombre_tienda,
                            imagenes=imagenes)
                            


@tienda_bp.route("/<nombre_tienda>/productos")
@tienda_bp.route("/<nombre_tienda>/productos/<int:pagina>")
def ver_productos(nombre_tienda, pagina=1):
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
            "plantilla": config_data.get("plantilla", "tienda_1"),
            "descripcion_portfolio": config_data.get("descripcion_portfolio"),
            "imagen_portfolio": config_data.get("imagen_portfolio"),
            "sobre_nosotros": config_data.get("sobre_nosotros"),
            "servicios_portfolio": config_data.get("servicios_portfolio"),
        }

        productos_result = connection.execute(producto_table.select()).mappings().fetchall()
        todos_los_productos = [dict(row) for row in productos_result]

    # PAGINACIÓN
    productos_por_pagina = 16
    total_productos = len(todos_los_productos)
    total_paginas = (total_productos + productos_por_pagina - 1) // productos_por_pagina

    if pagina < 1 or pagina > total_paginas:
        pagina = 1

    inicio = (pagina - 1) * productos_por_pagina
    fin = inicio + productos_por_pagina
    productos = todos_los_productos[inicio:fin]

    plantilla_base = f"PaginasTiendas/plantillas/tiendas/{configuracion['plantilla']}.html"

    return render_template("PaginasTiendas/plantillas/tiendas/plp.html",
                           config=configuracion,
                           productos=productos,
                           nombre_tienda=tienda_publica.nombre_tienda,
                           plantilla_base=plantilla_base,
                           pagina_actual=pagina,
                           total_paginas=total_paginas)



