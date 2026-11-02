from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.models import db, Usuario

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'clave_secreta_proyecto'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/bd_anuncios'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))

    # Registrar Blueprints
    from app.routes.main_routes import main_bp
    from app.routes.cat_routes import cat_bp
    from app.routes.post_routes import post_bp
    from app.routes.user_routes import user_bp
    from app.routes.auth_routes import auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(cat_bp, url_prefix='/categorias')
    app.register_blueprint(post_bp, url_prefix='/anuncios')
    app.register_blueprint(user_bp, url_prefix='/usuarios')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    with app.app_context():
        db.create_all()

    return app