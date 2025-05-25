import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import create_app, db
from app.models_publicos import TiendaPublica

app = create_app()

with app.app_context():
    tienda = TiendaPublica.query.filter_by(nombre_tienda="Testing").first()
    tienda.ruta_db = r"C:\\Users\\Ruben\\Documents\\Instituto 2024\\TFG\\vapecommerce\\app\\instance\\tiendas\\VAPEeCommerce.db"
    db.session.commit()
    print("Ruta actualizada con éxito ✅")