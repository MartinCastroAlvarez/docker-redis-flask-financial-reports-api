"""
Unit Tests.
https://pythonhosted.org/Flask-Testing/
"""

import os
import typing
from unittest.mock import Mock, patch

from flask import Flask
from flask_testing import TestCase

import app
from app import db
from app.models.report import Report
from app.views import reports as views
from tests.mocks.cache import RedisMock


class ReportViewsTest(TestCase):
    """
    Testing Report Views.
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

    def test_all_reports_get(self) -> None:
        """
        Testing GET views.reports.all_reports()
        """
        response: dict = views.all_reports()
        self.assertEquals(response, {"reports": []})
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
        response = views.all_reports()
        self.assertEquals(
            response,
            {
                "reports": [
                    {
                        "equity": 20.0,
                        "id": "lorem",
                        "retained_earnings": 1.0,
                        "sales": 30.0,
                        "score": 11.62,
                        "total_assets": 20.0,
                        "total_liabilities": 10.0,
                        "year": 2010,
                    }
                ]
            },
        )

    @patch.object(
        views.reports_controllers,
        "get_all_reports",
        side_effect=ValueError(),
    )
    def test_all_reports_get_error_handling(self, controller: Mock) -> None:
        """
        Testing GET views.reports.all_reports()
        All exceptions should be captured.
        """
        response: dict = views.all_reports()
        self.assertEquals(
            response,
            {
                "code": "unknown",
                "error": "<class 'ValueError'>",
                "message": [""],
            },
        )
        controller.assert_called_once()

    @patch.object(views.request, "method", "GET")
    @patch.object(
        views.reports_controllers,
        "get_reports_by_company_id",
        side_effect=ValueError(),
    )
    def test_report_by_id_error_handling(self, controller: Mock) -> None:
        """
        Testing GET views.report_by_id()
        All exceptions should be captured.
        """
        response: dict = views.report_by_id(company_id="123")
        self.assertEquals(
            response,
            {
                "code": "unknown",
                "error": "<class 'ValueError'>",
                "message": [""],
            },
        )
        controller.assert_called_once()

    @patch.object(views.request, "method", "GET")
    def test_report_by_id_get(self) -> None:
        """
        Testing GET views.report_by_id()
        """
        response: dict = views.report_by_id(company_id="lorem")
        self.assertEquals(response, {"reports": []})
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
        response = views.report_by_id(company_id="lorem")
        self.assertEquals(
            response,
            {
                "reports": [
                    {
                        "equity": 20.0,
                        "id": "lorem",
                        "retained_earnings": 1.0,
                        "sales": 30.0,
                        "score": 11.62,
                        "total_assets": 20.0,
                        "total_liabilities": 10.0,
                        "year": 2010,
                    }
                ]
            },
        )

    @patch.object(views.request, "method", "DELETE")
    def test_report_by_id_delete(self) -> None:
        """
        Testing DELETE views.report_by_id()
        """
        response: dict = views.report_by_id(company_id="lorem")
        self.assertEquals(response, {"reports": []})
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
        response = views.report_by_id(company_id="lorem")
        self.assertEquals(
            response,
            {
                "reports": [
                    {
                        "equity": 20.0,
                        "id": "lorem",
                        "retained_earnings": 1.0,
                        "sales": 30.0,
                        "score": 11.62,
                        "total_assets": 20.0,
                        "total_liabilities": 10.0,
                        "year": 2010,
                    }
                ]
            },
        )
        reports = Report.query.all()
        self.assertEquals(len(reports), 0)

    @patch.object(views.request, "method", "PUT")
    @patch.object(views.request, "data", b'{"financials": []}')
    def test_report_by_id_put(self) -> None:
        """
        Testing PUT views.report_by_id()
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
        with patch.object(
            views.reports_controllers,
            "create_reports_by_company_id",
            return_value=[
                report,
            ],
        ):
            response: dict = views.report_by_id(company_id="lorem")
            self.assertEquals(
                response,
                {
                    "reports": [
                        {
                            "equity": 20.0,
                            "id": "lorem",
                            "retained_earnings": 1.0,
                            "sales": 30.0,
                            "score": 11.62,
                            "total_assets": 20.0,
                            "total_liabilities": 10.0,
                            "year": 2010,
                        }
                    ]
                },
            )

    def tearDown(self) -> None:
        """
        Running after tests.
        """
        db.session.remove()
        db.drop_all()
