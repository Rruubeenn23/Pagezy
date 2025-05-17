# scripts/borrar_tienda_db.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models_publicos import TiendaPublica, TiendaEnProceso

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        if len(sys.argv) != 2:
            print("Uso: python borrar_tienda_db.py <nombre_tienda>")
            sys.exit(1)

        nombre_tienda = sys.argv[1]

        # Buscar y eliminar TiendaPublica
        tienda_pub = TiendaPublica.query.filter_by(nombre_tienda=nombre_tienda).first()
        if tienda_pub:
            ruta_db = tienda_pub.ruta_db
            db.session.delete(tienda_pub)
            print(f"Registro eliminado de TiendaPublica.")

            # Eliminar archivo físico
            if os.path.exists(ruta_db):
                os.remove(ruta_db)
                print(f"Archivo eliminado: {ruta_db}")
            else:
                print(f"No se encontró archivo en: {ruta_db}")
        else:
            print("Tienda no encontrada en TiendaPublica.")

        # Eliminar también si está en proceso
        tienda_tmp = TiendaEnProceso.query.filter_by(nombre_tienda=nombre_tienda).first()
        if tienda_tmp:
            db.session.delete(tienda_tmp)
            print("Registro eliminado de TiendaEnProceso.")

        db.session.commit()
