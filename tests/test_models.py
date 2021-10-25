"""
Unit Tests.
https://pythonhosted.org/Flask-Testing/
"""

import os
from unittest.mock import patch

from flask import Flask
from flask_testing import TestCase

import app
from app import db
from app.models.report import Report
from tests.mocks.cache import RedisMock


class ReportModelsTest(TestCase):
    """
    Testing Report Model.
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

    def test_score(self) -> None:
        """
        Testing Altman Z-Score.
        """
        report: Report = Report()
        report.company_id = "lorem"
        report.year = 2010
        report.sales = 30
        report.total_assets = 20
        report.total_liabilities = 10
        report.ebit = 50
        report.equity = 20
        report.retained_earnings = 1
        self.assertEquals(report.score, 11.62)

    def test_working_capital(self) -> None:
        """
        Testing Working Capital (approximation).
        """
        report: Report = Report()
        report.total_assets = 20
        report.total_liabilities = 8
        self.assertEquals(report.working_capital, 12)

    def test_liquid_assets(self) -> None:
        """
        Testing Liquid Assets ratio.
        """
        report: Report = Report()
        self.assertEquals(report.liquid_assets, 0)
        report.total_liabilities = 8
        report.total_assets = 0
        self.assertEquals(report.liquid_assets, 0)
        report.total_assets = 20
        self.assertEquals(report.liquid_assets, 0.6)

    def test_profitability(self) -> None:
        """
        Testing Profitability ratio.
        """
        report: Report = Report()
        self.assertEquals(report.profitability, 0)
        report.retained_earnings = 8
        report.total_assets = 0
        self.assertEquals(report.profitability, 0)
        report.total_assets = 20
        self.assertEquals(report.profitability, 0.4)

    def test_return_of_total_assets(self) -> None:
        """
        Testing Return of Total Assets ratio.
        """
        report: Report = Report()
        self.assertEquals(report.return_of_total_assets, 0)
        report.ebit = 8
        report.total_assets = 0
        self.assertEquals(report.return_of_total_assets, 0)
        report.total_assets = 20
        self.assertEquals(report.return_of_total_assets, 0.4)

    def test_financial_leverage(self) -> None:
        """
        Testing Return of Financial Leverage ratio.
        """
        report: Report = Report()
        self.assertEquals(report.financial_leverage, 0)
        report.equity = 8
        report.total_liabilities = 0
        self.assertEquals(report.financial_leverage, 0)
        report.total_liabilities = 20
        self.assertEquals(report.financial_leverage, 0.4)

    def test_asset_turnover(self) -> None:
        """
        Testing Asset Turnover ratio.
        """
        report: Report = Report()
        self.assertEquals(report.asset_turnover, 0)
        report.sales = 8
        report.total_assets = 0
        self.assertEquals(report.asset_turnover, 0)
        report.total_assets = 20
        self.assertEquals(report.asset_turnover, 0.4)

    def test_json_serializer(self) -> None:
        """
        Testing Report JSON serializer.
        """
        report: Report = Report()
        report.company_id = "lorem"
        report.year = 2010
        report.sales = 30
        report.total_assets = 20
        report.total_liabilities = 10
        report.ebit = 50
        report.equity = 20
        report.retained_earnings = 1
        serialized: dict = report.to_json()
        self.assertEquals(serialized["score"], report.score)
        self.assertEquals(serialized["id"], report.company_id)
        self.assertEquals(serialized["year"], report.year)
        self.assertEquals(serialized["equity"], report.equity)
        self.assertEquals(serialized["retained_earnings"], report.retained_earnings)
        self.assertEquals(serialized["sales"], report.sales)
        self.assertEquals(serialized["total_assets"], report.total_assets)
        self.assertEquals(serialized["total_liabilities"], report.total_liabilities)

    def test_string_serializer(self) -> None:
        """
        Testing Report String serializer.
        """
        report: Report = Report()
        report.company_id = "lorem"
        report.year = 2010
        report.sales = 30
        report.total_assets = 20
        report.total_liabilities = 10
        report.ebit = 50
        report.equity = 20
        report.retained_earnings = 1
        print(report)

    def tearDown(self) -> None:
        """
        Running after tests.
        """
        db.session.remove()
        db.drop_all()
