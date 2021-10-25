"""
Unit Tests.
https://pythonhosted.org/Flask-Testing/
"""

import os
from unittest.mock import patch

import werkzeug.test
from flask import Flask
from flask.testing import FlaskClient
from flask_testing import TestCase

import app
from app import db
from tests.mocks.cache import RedisMock


class ApiClientTest(TestCase):
    """
    Testing API Client.
    """

    @patch.object(app, "cache", RedisMock())
    def create_app(self) -> Flask:
        """
        Flask application factory.
        """
        os.environ["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
        os.environ["SECRET_KEY"] = "mock"
        os.environ["REDIS_HOST"] = "0.0.0.0"
        os.environ["REDIS_PORT"] = "6379"
        os.environ["REDIS_DB"] = "0"
        os.environ["TESTING"] = "true"
        os.environ["DEBUG"] = "true"
        return app.create_app()

    def setUp(self) -> None:
        """
        Running before tests.
        """
        db.create_all()

    def test_index(self) -> None:
        """
        Testing GET /
        """
        client: FlaskClient = self.app.test_client()
        response: werkzeug.test.TestResponse = client.get("/")
        self.assertEquals(response.status_code, 404)

    def test_companies(self) -> None:
        """
        Testing GET /company/gb
        """
        client: FlaskClient = self.app.test_client()
        response: werkzeug.test.TestResponse = client.get("/company/gb")
        self.assertEquals(response.status_code, 308)
        response = client.get("/company/gb/")
        self.assertEquals(response.status_code, 200)

    def test_companies_reports_get(self) -> None:
        """
        Testing GET /company/gb/<id>
        """
        client: FlaskClient = self.app.test_client()
        response: werkzeug.test.TestResponse = client.get("/company/gb/123")
        self.assertEquals(response.status_code, 200)

    def test_companies_reports_delete(self) -> None:
        """
        Testing DELETE /company/gb/<id>
        """
        client: FlaskClient = self.app.test_client()
        response: werkzeug.test.TestResponse = client.delete("/company/gb/123")
        self.assertEquals(response.status_code, 200)

    def test_companies_reports_put(self) -> None:
        """
        Testing PUT /company/gb/<id>
        """
        client: FlaskClient = self.app.test_client()
        response: werkzeug.test.TestResponse = client.put("/company/gb/123")
        self.assertEquals(response.status_code, 200)

    def test_companies_reports_post(self) -> None:
        """
        Testing POST /company/gb/<id>
        """
        client: FlaskClient = self.app.test_client()
        response: werkzeug.test.TestResponse = client.post("/company/gb/123")
        self.assertEquals(response.status_code, 405)

    def tearDown(self) -> None:
        """
        Running after tests.
        """
        db.session.remove()
        db.drop_all()
