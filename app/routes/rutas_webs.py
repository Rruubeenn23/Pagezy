import os
from flask import Blueprint, render_template, request, jsonify, flash, url_for, redirect, session
from sqlalchemy import create_engine, MetaData, Table, select
from app.models_publicos import TiendaPublica, TiendaEnProceso
import random
import json
from sqlalchemy.orm import sessionmaker
from app.models_tienda import Cliente, Pedido, Compra, Producto
from app import db
from datetime import datetime
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

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

    email = session.get("cliente_email")
    if not email:
        return jsonify({"error": "Usuario no autenticado"}), 401

    tienda = TiendaPublica.query.filter_by(nombre_tienda=nombre_tienda).first_or_404()

    engine = create_engine(f"sqlite:///{tienda.ruta_db}")
    metadata = MetaData()
    metadata.reflect(bind=engine)

    cliente_table = metadata.tables["cliente"]
    pedido_table = metadata.tables["pedido"]
    compra_table = metadata.tables["compra"]

    try:
        with engine.begin() as conn:
            # Obtener cliente desde sesión
            cliente = conn.execute(
                cliente_table.select().where(cliente_table.c.email == email)
            ).mappings().fetchone()

            if not cliente:
                return jsonify({"error": "Cliente no encontrado"}), 404

            cliente_id = cliente["id"]

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

            # Insertar productos comprados
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




@tienda_bp.route("/<nombre_tienda>/login", methods=["GET", "POST"])
def login(nombre_tienda):
    tienda_publica = TiendaPublica.query.filter_by(nombre_tienda=nombre_tienda).first_or_404()
    engine = create_engine(f"sqlite:///{tienda_publica.ruta_db}")
    metadata = MetaData()
    metadata.reflect(bind=engine)

    config_table = metadata.tables.get("configuracion_visual")
    cliente_table = metadata.tables.get("cliente")
    administrador_table = metadata.tables.get("administrador")

    with engine.connect() as conn:
        config_row = conn.execute(config_table.select()).mappings().fetchone()
        config_data = {
            "color_principal": config_row["color_principal"],
            "color_secundario": config_row["color_secundario"],
            "color_fondo": config_row["color_fondo"],
            "logo_url": config_row["logo_url"],
            "imagenes_tienda": json.loads(config_row["imagenes_tienda"] or "[]"),
            "plantilla": config_row.get("plantilla", "tienda_1")
        }

    if request.method == "GET":
        referer = request.referrer
        if referer and not any(x in referer for x in ["/login", "/register"]):
            session["url_origen"] = referer

        return render_template(
            "PaginasTiendas/plantillas/tiendas/auth/login.html",
            config=config_data,
            nombre_tienda=nombre_tienda
        )

    # POST
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        flash("Por favor, completa todos los campos.", "error")
        return redirect(url_for("tienda_publica.login", nombre_tienda=nombre_tienda))

    with engine.connect() as conn:
        # Primero buscar en la tabla administrador
        admin = None
        if administrador_table is not None:
            stmt = administrador_table.select().where(administrador_table.c.email == email)
            admin = conn.execute(stmt).mappings().fetchone()

        if admin is not None and check_password_hash(admin["contraseña"], password):
            session["admin_email"] = email
            flash("Inicio de sesión como administrador.", "success")
            return redirect(url_for("tienda_publica.admin_panel", nombre_tienda=nombre_tienda))

        # Si no es admin, buscar en cliente
        cliente = conn.execute(
            cliente_table.select().where(cliente_table.c.email == email)
        ).mappings().fetchone()

        if cliente:
            if check_password_hash(cliente.get("password_hash", ""), password):
                session["cliente_email"] = email
                session["cliente_nombre"] = cliente["nombre"]
                session["cliente_id"] = cliente["id"]
                flash("Inicio de sesión correcto.", "success")
                destino = session.pop("url_origen", None)
                return redirect(destino or url_for("tienda_publica.ver_tienda", nombre_tienda=nombre_tienda))
            else:
                flash("Contraseña incorrecta.", "error")
        else:
            flash("Este email no está registrado.", "error")

    return redirect(url_for("tienda_publica.login", nombre_tienda=nombre_tienda))




@tienda_bp.route("/<nombre_tienda>/register", methods=["GET", "POST"])
def register(nombre_tienda):
    tienda_publica = TiendaPublica.query.filter_by(nombre_tienda=nombre_tienda).first_or_404()

    engine = create_engine(f"sqlite:///{tienda_publica.ruta_db}")
    metadata = MetaData()
    metadata.reflect(bind=engine)

    config_table = metadata.tables.get("configuracion_visual")
    cliente_table = metadata.tables.get("cliente")

    if cliente_table is None or config_table is None:
        return "Tablas necesarias no encontradas", 500

    # Cargar configuración visual
    with engine.connect() as conn:
        config_row = conn.execute(config_table.select()).mappings().fetchone()
        configuracion = {
            "color_principal": config_row.get("color_principal", "#303f9f"),
            "color_secundario": config_row.get("color_secundario", "#1a237e"),
            "color_fondo": config_row.get("color_fondo", "#ffffff"),
            "logo_url": config_row.get("logo_url", ""),
            "imagenes_tienda": [],
            "plantilla": config_row.get("plantilla", "tienda_1"),
        }

        if config_row.get("imagenes_tienda"):
            try:
                configuracion["imagenes_tienda"] = json.loads(config_row["imagenes_tienda"])
            except Exception:
                configuracion["imagenes_tienda"] = []

    # POST: Registro
    if request.method == "POST":
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        telefono = request.form.get("telefono")
        direccion = request.form.get("direccion")
        password = request.form.get("password")

        # Hashear la contraseña
        password_hash = generate_password_hash(password)

        with engine.begin() as conn:
            existente = conn.execute(
                cliente_table.select().where(cliente_table.c.email == email)
            ).fetchone()

            if existente:
                flash("Este email ya está registrado. Inicia sesión.", "error")
                return redirect(url_for("tienda_publica.login", nombre_tienda=nombre_tienda))

            # Insertar cliente
            conn.execute(cliente_table.insert().values(
                nombre=nombre,
                email=email,
                telefono=telefono,
                direccion=direccion,
                fecha_registro=datetime.utcnow(),
                password_hash=password_hash  # ✅ Usamos el campo correcto
            ))

        flash("Registro exitoso. Ya puedes iniciar sesión.", "success")
        return redirect(url_for("tienda_publica.login", nombre_tienda=nombre_tienda))

    return render_template(
        "PaginasTiendas/plantillas/tiendas/auth/register.html",
        nombre_tienda=nombre_tienda,
        config=configuracion
    )


@tienda_bp.route("/<nombre_tienda>/admin")
def admin_panel(nombre_tienda):
    if "admin_email" not in session:
        flash("Acceso denegado. Inicia sesión como administrador.", "error")
        return redirect(url_for("tienda_publica.login", nombre_tienda=nombre_tienda))

    tienda_publica = TiendaPublica.query.filter_by(nombre_tienda=nombre_tienda).first_or_404()
    tienda_proceso = TiendaEnProceso.query.filter_by(nombre_tienda=nombre_tienda).first()

    engine = create_engine(f"sqlite:///{tienda_publica.ruta_db}")
    metadata = MetaData()
    metadata.reflect(bind=engine)

    config_table = metadata.tables["configuracion_visual"]
    cliente_table = metadata.tables["cliente"]
    pedido_table = metadata.tables["pedido"]
    compra_table = metadata.tables["compra"]
    producto_table = metadata.tables["producto"]
    vendedor_table = metadata.tables.get("vendedor")  # opcional

    with engine.connect() as conn:
        config_data = conn.execute(config_table.select()).mappings().fetchone()
        config = {
            "color_principal": config_data["color_principal"],
            "color_secundario": config_data["color_secundario"],
            "color_fondo": config_data["color_fondo"],
            "logo_url": config_data["logo_url"],
            "plantilla": config_data.get("plantilla", "tienda_1")
        }

        clientes = conn.execute(cliente_table.select()).mappings().fetchall()
        pedidos = conn.execute(pedido_table.select()).mappings().fetchall()
        compras = conn.execute(compra_table.select()).mappings().fetchall()
        productos = conn.execute(producto_table.select()).mappings().fetchall()
        vendedores = []
        if vendedor_table is not None:
            stmt = vendedor_table.select()
            vendedores = conn.execute(stmt).mappings().fetchall()

    return render_template("PaginasTiendas/plantillas/tiendas/cuenta/admin.html",
                           nombre_tienda=nombre_tienda,
                           config=config,
                           clientes=clientes,
                           pedidos=pedidos,
                           compras=compras,
                           productos=productos,
                           vendedores=vendedores)

@tienda_bp.route("/<nombre_tienda>/cuenta")
def cuenta(nombre_tienda):
    cliente_id = session.get("cliente_id")
    if not cliente_id:
        return redirect(url_for("tienda_publica.login", nombre_tienda=nombre_tienda))

    tienda = TiendaPublica.query.filter_by(nombre_tienda=nombre_tienda).first_or_404()
    tienda_proceso = TiendaEnProceso.query.filter_by(nombre_tienda=nombre_tienda).first()

    engine = create_engine(f"sqlite:///{tienda.ruta_db}")
    metadata = MetaData()
    metadata.reflect(bind=engine)

    cliente_table = metadata.tables.get("cliente")
    pedido_table = metadata.tables.get("pedido")
    compra_table = metadata.tables.get("compra")
    producto_table = metadata.tables.get("producto")
    config_table = metadata.tables.get("configuracion_visual")

    with engine.connect() as conn:
        # Obtener configuración visual
        config_data = conn.execute(config_table.select()).mappings().fetchone()
        configuracion = {
            "color_principal": config_data["color_principal"],
            "color_secundario": config_data["color_secundario"],
            "color_fondo": config_data["color_fondo"],
            "logo_url": config_data["logo_url"],
            "plantilla": config_data.get("plantilla", "tienda_1")
        }

        # Obtener cliente
        cliente = conn.execute(
            select(cliente_table).where(cliente_table.c.id == cliente_id)
        ).mappings().fetchone()

        if not cliente:
            return redirect(url_for("tienda_publica.login", nombre_tienda=nombre_tienda))

        # Obtener pedidos
        pedidos = conn.execute(
            select(pedido_table).where(pedido_table.c.cliente_id == cliente_id)
        ).mappings().fetchall()

        # Obtener compras relacionadas
        compras = []
        for pedido in pedidos:
            pedido_id = pedido["id"]
            compras_result = conn.execute(
                select(compra_table, producto_table.c.nombre, producto_table.c.precio)
                .where(compra_table.c.pedido_id == pedido_id)
                .join(producto_table, compra_table.c.producto_id == producto_table.c.id)
            ).mappings().fetchall()

            for compra in compras_result:
                compras.append({
                    "compra_id": compra["id"],
                    "pedido_id": pedido_id,
                    "fecha_pedido": pedido["fecha"],
                    "producto": compra["nombre"],
                    "cantidad": compra["cantidad"],
                    "precio_unitario": compra["precio"],
                    "subtotal": compra["precio"] * compra["cantidad"]
                })

    return render_template(
        "PaginasTiendas/plantillas/tiendas/cuenta/cuenta.html",
        nombre_tienda=nombre_tienda,
        config=configuracion,  # ✅ Agregado aquí
        cliente=cliente,
        pedidos=pedidos,
        compras=compras,
        telefono=tienda_proceso.telefono,
        email=tienda_proceso.email
    )


@tienda_bp.route("/<nombre_tienda>/logout")
def logout(nombre_tienda):
    session.clear()
    return redirect(url_for("tienda_publica.login", nombre_tienda=nombre_tienda))
