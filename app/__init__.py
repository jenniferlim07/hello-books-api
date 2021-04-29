from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# postgresql+psycopg2://postgres:postgres@localhost:5432/REPLACE_THIS_LAST_PART_WITH_DB_NAME
# postgresql+psycopg2://postgres:postgres@localhost:5432/ada_books_development

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    #DB Config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:postgres@localhost:5432/ada_books_development"

    db.init_app(app)
    migrate.init_app(app, db)
    from app.models.book import Book

    # from .routes import hello_world_bp
    # app.register_blueprint(hello_world_bp)

    from .routes import books_bp
    app.register_blueprint(books_bp)

    return app
