"""
Flask application
https://flask-and-redis.readthedocs.io/en/latest/
"""

import logging

from flask_redis import Redis

logger: logging.Logger = logging.getLogger(__name__)

cache: Redis = Redis()

logger.info("Cache initialized: %s", cache)
