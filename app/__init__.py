"""
Flask application
https://flask.palletsprojects.com/en/2.0.x/tutorial/factory/
"""

import logging
import os

from flask import Flask

from app.db import db
from app.views.reports import blue as reports

logger: logging.Logger = logging.getLogger(__name__)


def create_app() -> Flask:
    """
    App factory.
    https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/
    """
    app: Flask = Flask(__name__, instance_relative_config=True)
    app.config.from_object(os.environ)
    app.register_blueprint(reports)

    db.init_app(app)

    @app.before_first_request
    def before() -> None:
        """
        Creating SQL Schema.
        """
        db.create_all()

    logger.info("App initialized: %s", app)
    return app
