from flask import Flask
from .extensions import db, cache

def create_app():
    app = Flask(__name__)
    

    app.config.from_object('app.config.Config')

    db.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()
        return app