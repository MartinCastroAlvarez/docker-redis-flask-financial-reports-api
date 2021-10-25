"""
Flask application
https://flask.palletsprojects.com/en/2.0.x/tutorial/factory/
"""

import logging
import os

from flask import Flask

from app.cache import cache
from app.db import db
from app.views.reports import blue as reports

logger: logging.Logger = logging.getLogger(__name__)


def create_app() -> Flask:
    """
    App factory.
    https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/
    """
    app: Flask = Flask(__name__, instance_relative_config=True)

    # Loading configuration from Environment variables.
    logger.info("Environment variables:: %s", os.environ)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["DEBUG"] = bool(os.environ.get("DEBUG", ""))
    app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ[
        "SQLALCHEMY_DATABASE_URI"
    ]
    app.config["REDIS_PORT"] = os.environ["REDIS_PORT"]
    app.config["REDIS_HOST"] = os.environ["REDIS_HOST"]
    app.config["REDIS_DB"] = os.environ["REDIS_DB"]
    logger.info("Config:: %s", app.config)

    # Registering Flask Blueprints & routes.
    app.register_blueprint(reports)

    # Initializing database and cache connections.
    db.init_app(app)
    cache.init_app(app)

    @app.before_first_request
    def before() -> None:
        """
        Creating SQL Schema.
        """
        db.create_all()

    logger.info("App initialized: %s %s", app, app.config)
    return app
