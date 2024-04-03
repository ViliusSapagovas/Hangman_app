from flask import Flask

from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here

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