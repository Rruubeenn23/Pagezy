import os
from flask import Blueprint, render_template, request, jsonify
from sqlalchemy import create_engine, MetaData, Table
from app.models_publicos import TiendaPublica, TiendaEnProceso
import random
import json
from sqlalchemy.orm import sessionmaker
from app.models_publicos import TiendaPublica
from app.models_tienda import Cliente, Pedido, Compra, Producto
from app import db
from datetime import datetime
import os
import json

# Crear blueprint para las tiendas públicas
tienda_bp = Blueprint('tienda_publica', __name__, url_prefix="/pages")

@tienda_bp.route("/<nombre_tienda>")
def ver_tienda(nombre_tienda):
    tienda_publica = TiendaPublica.query.filter_by(nombre_tienda=nombre_tienda).first_or_404()
    tienda_proceso = TiendaEnProceso.query.filter_by(nombre_tienda=nombre_tienda).first()

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
                            imagenes=imagenes,
                            telefono=tienda_proceso.telefono,
                            email=tienda_proceso.email)
                            


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


@tienda_bp.route("/<nombre_tienda>/info")
def ver_info(nombre_tienda):
    tienda_publica = TiendaPublica.query.filter_by(nombre_tienda=nombre_tienda).first_or_404()
    tienda_proceso = TiendaEnProceso.query.filter_by(nombre_tienda=nombre_tienda).first()

    engine = create_engine(f"sqlite:///{tienda_publica.ruta_db}")
    metadata = MetaData()
    metadata.reflect(bind=engine)

    config_table = metadata.tables["configuracion_visual"]

    with engine.connect() as connection:
        config_data = connection.execute(config_table.select()).mappings().fetchone()
        configuracion = {
            "color_principal": config_data["color_principal"],
            "color_secundario": config_data["color_secundario"],
            "color_fondo": config_data["color_fondo"],
            "logo_url": config_data["logo_url"],
            "plantilla": config_data.get("plantilla", "info_1"),
            "descripcion_portfolio": config_data.get("descripcion_portfolio"),
            "imagen_portfolio": config_data.get("imagen_portfolio"),
            "sobre_nosotros": config_data.get("sobre_nosotros"),
            "servicios_portfolio": config_data.get("servicios_portfolio"),
        }
        if config_data.get("plantilla") == "info_1":
            plantilla_base = "PaginasTiendas/plantillas/info_1.html"
        else:
            plantilla_base = "PaginasTiendas/plantillas/info_2.html"


    return render_template("PaginasTiendas/plantillas/info/extra_info.html",
                           config=configuracion,
                           nombre_tienda=tienda_publica.nombre_tienda,
                           telefono=tienda_proceso.telefono,
                           email=tienda_proceso.email,
                            plantilla_base=plantilla_base)

@tienda_bp.route("/<nombre_tienda>/producto/<int:producto_id>")
def ver_producto(nombre_tienda, producto_id):
    tienda_publica = TiendaPublica.query.filter_by(nombre_tienda=nombre_tienda).first_or_404()
    tienda_proceso = TiendaEnProceso.query.filter_by(nombre_tienda=nombre_tienda).first()

    engine = create_engine(f"sqlite:///{tienda_publica.ruta_db}")
    metadata = MetaData()
    metadata.reflect(bind=engine)

    producto_table = metadata.tables["producto"]
    config_table = metadata.tables["configuracion_visual"]

    with engine.connect() as connection:
        producto = connection.execute(
            producto_table.select().where(producto_table.c.id == producto_id)
        ).mappings().fetchone()

        if not producto:
            return "Producto no encontrado", 404

        config_data = connection.execute(config_table.select()).mappings().fetchone()
        configuracion = {
            "color_principal": config_data["color_principal"],
            "color_secundario": config_data["color_secundario"],
            "color_fondo": config_data["color_fondo"],
            "logo_url": config_data["logo_url"],
            "plantilla": config_data.get("plantilla", "tienda_1"),
        }

    return render_template(
        "PaginasTiendas/plantillas/tiendas/pdp.html",
        producto=producto,
        nombre_tienda=nombre_tienda,
        config=configuracion,
        tienda=tienda_proceso)

@tienda_bp.route("/<nombre_tienda>/api/guardar_pedido", methods=["POST"])
def guardar_pedido(nombre_tienda):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No se recibieron datos"}), 400

    tienda = TiendaPublica.query.filter_by(nombre_tienda=nombre_tienda).first_or_404()

    # Acceder a su base de datos individual
    engine = create_engine(f"sqlite:///{tienda.ruta_db}")
    metadata = MetaData()
    metadata.reflect(bind=engine)

    # Obtener tablas reflejadas
    cliente_table = metadata.tables["cliente"]
    pedido_table = metadata.tables["pedido"]
    compra_table = metadata.tables["compra"]

    try:
        with engine.begin() as conn:
            # Insertar cliente
            result = conn.execute(
                cliente_table.insert().values(
                    nombre=data["nombre"],
                    email=data["email"],
                    telefono=data["telefono"],
                    direccion=data["direccion"]
                )
            )
            cliente_id = result.inserted_primary_key[0]

            # Insertar pedido
            total = sum(p["precio"] * p["cantidad"] for p in data["carrito"])
            pedido_result = conn.execute(
                pedido_table.insert().values(
                    cliente_id=cliente_id,
                    estado="pendiente",
                    total=total
                )
            )
            pedido_id = pedido_result.inserted_primary_key[0]

            # Insertar cada producto
            for p in data["carrito"]:
                conn.execute(
                    compra_table.insert().values(
                        pedido_id=pedido_id,
                        producto_id=int(p["id"]),
                        cantidad=int(p["cantidad"])
                    )
                )

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"mensaje": "Pedido guardado correctamente"})