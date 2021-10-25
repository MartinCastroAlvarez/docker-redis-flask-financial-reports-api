"""
Mocking Redis.
"""

from unittest.mock import Mock

from flask import Flask


class RedisMock(Mock):
    """
    Redis mock
    """

    def get(self, cache_key: str) -> str:
        """
        Redis getter.
        """
        print("Redis GET:", cache_key)
        return cache_key

    def set(self, cache_key: str, value: str) -> None:
        """
        Redis setter.
        """
        print("Redis SET:", cache_key, value)

    def init_app(self, app: Flask) -> None:
        """
        Flask integration.
        """
        print("Redis INIT:", app)
