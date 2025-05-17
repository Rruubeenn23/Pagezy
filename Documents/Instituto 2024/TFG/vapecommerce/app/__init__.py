from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Rutas
    from app.routes.crear_tienda import crear_tienda_bp
    from app.routes.tiendas import tiendas_bp
    from app.routes.rutas_tiendas import tienda_bp
    app.register_blueprint(crear_tienda_bp)
    app.register_blueprint(tiendas_bp)
    app.register_blueprint(tienda_bp)

    
    @app.route("/")
    def home():
            return render_template("PaginasPresentacion/home.html")
    return app