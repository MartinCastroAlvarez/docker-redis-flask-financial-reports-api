"""
Unit Tests.
https://pythonhosted.org/Flask-Testing/
"""

import os
import typing
from unittest.mock import Mock, patch

import sqlalchemy.exc
from flask import Flask
from flask_testing import TestCase

import app
from app import db
from app.controllers import reports as controllers
from app.models.report import Report
from tests.mocks.cache import RedisMock


class ReportControllersTest(TestCase):
    """
    Testing Report Controllers.
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

    def test_delete_reports_by_company_id(self) -> None:
        """
        Testing Reports deletion by ID.
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
        db.session.add(report)
        db.session.commit()
        reports: typing.List[Report] = Report.query.all()
        self.assertEquals(len(reports), 1)
        self.assertEquals(reports[0].company_id, report.company_id)
        with self.assertRaises(controllers.CompanyIdException):
            list(controllers.delete_reports_by_company_id(company_id=""))
        list(controllers.delete_reports_by_company_id(report.company_id))
        reports = Report.query.all()
        self.assertEquals(len(reports), 0)

    def test_get_reports_by_company_id(self) -> None:
        """
        Testing Reports search by ID.
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
        db.session.add(report)
        db.session.commit()
        with self.assertRaises(controllers.CompanyIdException):
            list(controllers.get_reports_by_company_id(company_id=""))
        reports: typing.List[Report] = list(controllers.get_reports_by_company_id(report.company_id))
        self.assertEquals(len(reports), 1)
        self.assertEquals(reports[0].company_id, report.company_id)

    def test_get_all_reports(self) -> None:
        """
        Testing Reports search.
        """
        reports: typing.List[Report] = list(controllers.get_all_reports())
        self.assertEquals(len(reports), 0)
        report: Report = Report()
        report.company_id = "lorem"
        report.year = 2010
        report.sales = 30
        report.total_assets = 20
        report.total_liabilities = 10
        report.ebit = 50
        report.equity = 20
        report.retained_earnings = 1
        db.session.add(report)
        db.session.commit()
        reports = list(controllers.get_all_reports())
        self.assertEquals(len(reports), 1)
        self.assertEquals(reports[0].company_id, report.company_id)

    @patch.object(controllers, "cache", RedisMock())
    def test_create_reports_by_company_id_cached(self) -> None:
        """
        Testing Reports cached creation.
        """
        with self.assertRaises(controllers.DuplicateException):
            list(
                controllers.create_reports_by_company_id(
                    company_id="lorem",
                    financials=[
                        {
                            "year": "2010",
                            "sales": 30,
                            "total_assets": 20,
                            "total_liabilities": 10,
                            "ebit": 50,
                            "equity": 20,
                            "retained_earnings": 1,
                        }
                    ],
                )
            )

    @patch.object(controllers, "validate_financials")
    @patch.object(controllers, "cache", RedisMock())
    def test_create_reports_by_company_id(self, validate_financials: Mock) -> None:
        """
        Testing Reports creation.
        """
        with self.assertRaises(controllers.CompanyIdException):
            list(controllers.create_reports_by_company_id(company_id="", financials=[]))
        with patch.object(controllers.cache, "get", return_value=""):
            reports: typing.List[Report] = list(
                controllers.create_reports_by_company_id(
                    company_id="lorem",
                    financials=[
                        {
                            "year": 2010,
                            "sales": 30,
                            "total_assets": 20,
                            "total_liabilities": 10,
                            "ebit": 50,
                            "equity": 20,
                            "retained_earnings": 1,
                        }
                    ],
                )
            )
            self.assertEquals(len(reports), 1)
            self.assertEquals(reports[0].company_id, "lorem")
            self.assertEquals(reports[0].year, 2010)
            self.assertEquals(reports[0].sales, 30)
            self.assertEquals(reports[0].total_assets, 20)
            self.assertEquals(reports[0].total_liabilities, 10)
            self.assertEquals(reports[0].ebit, 50)
            self.assertEquals(reports[0].equity, 20)
            self.assertEquals(reports[0].retained_earnings, 1)
        validate_financials.assert_called_once()
        reports = Report.query.all()
        self.assertEquals(len(reports), 1)
        self.assertEquals(reports[0].company_id, "lorem")

    @patch.object(
        controllers.db.session,
        "commit",
        side_effect=sqlalchemy.exc.IntegrityError({}, {}, {}),
    )
    @patch.object(controllers, "cache", RedisMock())
    def test_create_reports_by_company_id_duplicate(self, commit: Mock) -> None:
        """
        Testing Reports creation duplicate.
        """
        with self.assertRaises(controllers.DuplicateException):
            with patch.object(controllers.cache, "get", return_value=""):
                list(
                    controllers.create_reports_by_company_id(
                        company_id="lorem",
                        financials=[
                            {
                                "year": 2010,
                                "sales": 30,
                                "total_assets": 20,
                                "total_liabilities": 10,
                                "ebit": 50,
                                "equity": 20,
                                "retained_earnings": 1,
                            }
                        ],
                    )
                )
        commit.assert_called_once()

    @patch.object(controllers, "cache", RedisMock())
    def test_create_reports_by_company_id_empty(self) -> None:
        """
        Testing Reports creation.
        """
        with patch.object(controllers.cache, "get", return_value=""):
            reports: typing.List[Report] = list(
                controllers.create_reports_by_company_id(company_id="lorem", financials=[])
            )
            self.assertEquals(len(reports), 0)
        reports = Report.query.all()
        self.assertEquals(len(reports), 0)

    def tearDown(self) -> None:
        """
        Running after tests.
        """
        db.session.remove()
        db.drop_all()
