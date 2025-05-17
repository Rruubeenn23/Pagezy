# run.py
import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    # Aseguramos que existe la carpeta de instancia
    os.makedirs(app.instance_path, exist_ok=True)

    app.run(debug=True, host="0.0.0.0", port=5000)
