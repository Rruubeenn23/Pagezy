# scripts/crear_tienda_db.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.db_manager import finalizar_tienda

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        if len(sys.argv) != 2:
            print("Uso: python crear_tienda_db.py <id_tienda_en_proceso>")
            sys.exit(1)
        
        tienda_id = int(sys.argv[1])
        try:
            mensaje = finalizar_tienda(tienda_id)
            print(mensaje)
        except Exception as e:
            print(f"Error: {e}")
