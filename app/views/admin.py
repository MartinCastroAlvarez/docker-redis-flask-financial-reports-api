"""
Flask Admin Blueprint
https://flask.palletsprojects.com/en/2.0.x/blueprints/
"""

import logging

from flask import Blueprint

logger: logging.RootLogger = logging.getLogger(__name__)

blue: Blueprint = Blueprint("admin", __name__, url_prefix="/")


@blue.route("/")
def index() -> str:
    """
    Hello world example.
    """
    return "Hello, World!"


logger.info('Admin Blueprint initialized:', blue)
