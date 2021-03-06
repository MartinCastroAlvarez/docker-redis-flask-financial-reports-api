"""
Flask SQLAlchemy
"""

import logging

from flask_sqlalchemy import SQLAlchemy

logger: logging.Logger = logging.getLogger(__name__)

db: SQLAlchemy = SQLAlchemy()

logger.info("Database initialized: %s", db)
