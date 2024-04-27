from flask import Flask
from flask_login import LoginManager
from config import Config
from app.extensions import db, login_manager
import os


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY

    # Initialize Flask extensions here
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        db.create_all()

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.account import bp as account_bp
    app.register_blueprint(account_bp, url_prefix='/account')

    from app.game import bp as game_bp
    app.register_blueprint(game_bp, url_prefix='/game')

    from app.statistics import bp as statistics_bp
    app.register_blueprint(statistics_bp, url_prefix='/statistics')

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app

