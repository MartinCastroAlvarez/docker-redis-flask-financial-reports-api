"""
Flask application
https://flask.palletsprojects.com/en/2.0.x/tutorial/factory/
"""

import os
import logging

from redis import Redis

logger: logging.RootLogger = logging.getLogger(__name__)

cache: Redis = Redis(
    host=os.environ["REDIS_HOSTNAME"],
    port=int(os.environ["REDIS_PORT"]),
)

logger.info('Cache initialized:', cache)
