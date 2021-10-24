"""
Flask application
https://flask.palletsprojects.com/en/2.0.x/tutorial/factory/
"""

import logging
import os

from redis import Redis

logger: logging.Logger = logging.getLogger(__name__)

cache: Redis = Redis(
    host=os.environ["REDIS_HOSTNAME"],
    port=int(os.environ["REDIS_PORT"]),
)

logger.info("Cache initialized: %s", cache)
