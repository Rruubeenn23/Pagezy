from flask import Blueprint, render_template, request, redirect, url_for
from app.models_publicos import db, TiendaEnProceso, ProductoBase, TiendaPublica
import json
from app import db
from collections import defaultdict
import os
from werkzeug.security import generate_password_hash
from app.models_tienda import Administrador
from sqlalchemy import create_engine, MetaData, Table


crear_tienda_bp = Blueprint('crear_tienda', __name__, url_prefix="/pages/create")

@crear_tienda_bp.route("/", methods=["GET", "POST"])
def paso1():
    if request.method == "POST":
        tienda = TiendaEnProceso(
            nombre_tienda = request.form.get("nombre_tienda"),
            nombre=request.form["nombre"],
            apellidos=request.form["apellidos"],
            email=request.form["email"],
            telefono=request.form["telefono"],
            paso_actual=2
        )
        db.session.add(tienda)
        db.session.commit()
        return redirect(url_for("crear_tienda.paso2", tienda_id=tienda.id))
    
    return render_template("PaginasPresentacion/crear_tienda/paso1_datos.html", paso=1)

from flask import current_app

@crear_tienda_bp.route("/<int:tienda_id>/colores", methods=["GET", "POST"])
def paso2(tienda_id):
    tienda = TiendaEnProceso.query.get_or_404(tienda_id)

    if request.method == "POST":
        tienda.color_principal = request.form["color_principal"]
        tienda.color_secundario = request.form["color_secundario"]
        tienda.color_fondo = request.form["color_fondo"]

        # Logo
        logo_file = request.files.get("logo")
        if logo_file and logo_file.filename != "":
            filename = f"{tienda.nombre_tienda}_logo.png"
            ruta_static = os.path.join(current_app.root_path, "static", "logos")
            os.makedirs(ruta_static, exist_ok=True)
            ruta_logo = os.path.join(ruta_static, filename)
            logo_file.save(ruta_logo)
            tienda.logo_url = f"/static/logos/{filename}"

        # Tipo y plantilla
        tienda.tipo_web = request.form.get("tipo_web")
        tienda.plantilla = request.form.get("plantilla")

        # Título descriptivo
        tienda.titulo_tienda = request.form.get("titulo_tienda")

        # Imágenes tienda
        imagenes_urls = []
        for key in request.form:
            if key.startswith("imagenes_tienda_"):
                url = request.form[key].strip()
                if url:
                    imagenes_urls.append(url)
        
        tienda.descripcion_portfolio = request.form.get("descripcion_portfolio")
        tienda.imagen_portfolio = request.form.get("imagen_portfolio")
        tienda.sobre_nosotros = request.form.get("sobre_nosotros")
        
        # Recoger servicios individuales
        servicios = []
        for key in request.form:
            if key.startswith("servicios_portfolio_"):
                valor = request.form[key].strip()
                if valor:
                    servicios.append(valor)

        tienda.servicios_portfolio = ", ".join(servicios)


        tienda.imagenes_tienda = json.dumps(imagenes_urls)  # Guardamos como string JSON

        tienda.paso_actual = 3
        db.session.commit()
        return redirect(url_for("crear_tienda.paso3", tienda_id=tienda.id))

    return render_template("PaginasPresentacion/crear_tienda/paso2_colores.html", tienda=tienda, paso=2)

from collections import defaultdict

@crear_tienda_bp.route("/<int:tienda_id>/productos", methods=["GET", "POST"])
def paso3(tienda_id):
    tienda = TiendaEnProceso.query.get_or_404(tienda_id)

    # Si el tipo es "informacion", redirigir a otro paso 3
    if tienda.tipo_web == "informacion":
        return redirect(url_for("crear_tienda.resumen_confirmacion", tienda_id=tienda.id))

    productos = ProductoBase.query.all()

    # Agrupar productos por tipo general y subtipo
    productos_por_categoria = defaultdict(lambda: defaultdict(list))
    for p in productos:
        productos_por_categoria[p.tipo][p.categoria].append(p)

    if request.method == "POST":
        seleccion = request.form.getlist("productos")
        tienda.productos_seleccionados = json.dumps(seleccion)
        tienda.paso_actual = 4
        db.session.commit()
        return redirect(url_for("crear_tienda.resumen_confirmacion", tienda_id=tienda.id))

    return render_template(
        "PaginasPresentacion/crear_tienda/paso3_productos.html",
        tienda=tienda,
        productos_por_categoria=productos_por_categoria,
        paso=3
    )



@crear_tienda_bp.route("/<int:tienda_id>/confirmacion", methods=["GET", "POST"])
def resumen_confirmacion(tienda_id):
    tienda = TiendaEnProceso.query.get_or_404(tienda_id)

    productos_ids = []
    productos = []

    if tienda.productos_seleccionados:
        productos_ids = json.loads(tienda.productos_seleccionados)
        productos = ProductoBase.query.filter(ProductoBase.id.in_(productos_ids)).all()


    # Agrupar productos seleccionados por tipo
    productos_por_tipo = defaultdict(list)
    for p in productos:
        productos_por_tipo[p.tipo].append(p)

    if request.method == "POST":
        # Guardar en TiendaPublica
        tienda_publica = TiendaPublica(
            nombre_tienda=tienda.nombre_tienda,
            email_contacto=tienda.email,
            ruta_db=""  # este se actualizará después de crear la .db real
        )
        db.session.add(tienda_publica)
        db.session.commit()

        # Crear base de datos final de la tienda
        datos_visuales = {
    "color_principal": tienda.color_principal,
    "color_secundario": tienda.color_secundario,
    "color_fondo": tienda.color_fondo,
    "logo_url": tienda.logo_url or "",
    

}


        from app.db_manager import finalizar_tienda
        finalizar_tienda(tienda.id)

        # Crear administrador por defecto
        aruta_db = os.path.join("databases", f"{tienda.nombre_tienda}.db")  # o como esté definido en tu sistema
        engine = create_engine(f"sqlite:///{tienda_publica.ruta_db}")
        metadata = MetaData()
        metadata.reflect(bind=engine)

        if "administrador" in metadata.tables:
            administrador_table = metadata.tables["administrador"]

            with engine.begin() as conn:
                # Verificar si ya existe un admin
                admin_existente = conn.execute(
                    administrador_table.select().where(administrador_table.c.usuario == "admin")
                ).fetchone()

                if not admin_existente:
                    conn.execute(
                        administrador_table.insert().values(
                            usuario="admin",
                            contraseña=generate_password_hash("admin"),
                            email=tienda.email
                        )
                    )

        return redirect(url_for("crear_tienda.tienda_creada", tienda_id=tienda.id))

    return render_template(
        "PaginasPresentacion/crear_tienda/resumen_confirmacion.html",
        tienda=tienda,
        productos_por_tipo=productos_por_tipo,
        paso=4
    )

@crear_tienda_bp.route("/<int:tienda_id>/creada")
def tienda_creada(tienda_id):
    tienda = TiendaEnProceso.query.get_or_404(tienda_id)
    return render_template("PaginasPresentacion/crear_tienda/animacion.html", tienda=tienda)
