# scripts/crear_main_db.py
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models_publicos import *

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        path_db = os.path.join(app.instance_path, 'main.db')

        # Mostrar dónde se creará
        print(f"Creando base de datos en: {path_db}")

        # Crea todas las tablas de los modelos públicos
        db.create_all()

        print("✅ main.db creada correctamente con todas las tablas.")
