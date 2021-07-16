from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config
import requests


db = SQLAlchemy()
migrate = Migrate()

def create_app(config=None):
    app = Flask(__name__)
    app.secret_key = "lkjds#2-1j@dsp!ldaskfj"

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///p_app.sqlite3'

    if config is not None:
        app.config.update(config)


    db.init_app(app)
    migrate.init_app(app, db)

    from p_app import route1
    app.register_blueprint(route1.bp)
    # app.register_blueprint(route2.bp)


    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
