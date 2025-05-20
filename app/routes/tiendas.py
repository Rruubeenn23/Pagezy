from flask import Blueprint, render_template
from app.models_publicos import TiendaPublica

tiendas_bp = Blueprint("tiendas", __name__, url_prefix="/pages")

@tiendas_bp.route("/")
def lista_tiendas():
    tiendas = TiendaPublica.query.all()
    return render_template("PaginasPresentacion/tiendas/lista_tiendas.html", tiendas=tiendas)

