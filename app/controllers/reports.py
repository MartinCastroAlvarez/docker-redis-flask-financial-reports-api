"""
Reports Controllers
https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
"""

import typing
import logging

from sqlalchemy import exc

from app.db import db
from app.models.report import Report

logger: logging.RootLogger = logging.getLogger(__name__)


class ReportIdException(Exception):
    """Raised when the report ID is invalid."""


class FinancialsException(Exception):
    """Raised when financials are invalid."""


def create_reports_by_report_id(
    report_id: str, financials: list
) -> typing.Generator[Report, None, None]:
    """
    Creates a new Report.
    """
    if not report_id or not isinstance(report_id, str):
        raise ReportIdException("Invalid Report ID")
    if not isinstance(financials, list):
        raise FinancialsException("Invalid financials.")
    for index, financial in enumerate(financials):
        if not isinstance(financial, dict):
            raise FinancialsException(f"Invalid financials[{index}].")
        if (
            "year" not in financial
            or not isinstance(financial["year"], (int, float))
            or financial["year"] < 0
        ):
            raise FinancialsException(
                f"Invalid financials[{index}] year."
            )
        if (
            "ebit" not in financial
            or not isinstance(financial["ebit"], (int, float))
            or financial["ebit"] < 0
        ):
            raise FinancialsException(
                f"Invalid financials[{index}] ebit."
            )
        if (
            "equity" not in financial
            or not isinstance(financial["equiy"], (int, float))
            or financial["equity"] < 0
        ):
            raise FinancialsException(
                f"Invalid financials[{index}] equity."
            )
        if (
            "sales" not in financial
            or not isinstance(financial["sales"], (int, float))
            or financial["sales"] < 0
        ):
            raise FinancialsException(
                f"Invalid financials[{index}] sales."
            )
        if (
            "total_assets" not in financial
            or not isinstance(financial["total_assets"], (int, float))
            or financial["total_assets"] < 0
        ):
            raise FinancialsException(
                f"Invalid financials[{index}] total_assets."
            )
        if (
            "total_liabilities" not in financial
            or not isinstance(
                financial["total_liabilities"], (int, float)
            )
            or financial["total_liabilities"] < 0
        ):
            raise FinancialsException(
                f"Invalid financials[{index}] total_liabilities."
            )
        report: Report = Report()
        report.report_id = report_id
        report.year = financial["year"]
        report.ebit = financial["ebit"]
        report.equity = financial["equity"]
        report.retained_earnings = financial["retained_earnings"]
        report.sales = financial["sales"]
        report.total_assets = financial["total_assets"]
        report.total_liabilities = financial["total_liabilities"]
        db.session.add(report)
        yield report
    try:
        db.session.commit()
    except exc.SQLAlchemyError:
        db.session.rollback()
        raise


def get_all_reports() -> typing.Generator[Report, None, None]:
    """
    Returns a list of all reports available.
    """
    yield from Report.query.all()


def get_reports_by_report_id(
    report_id: str,
) -> typing.Generator[Report, None, None]:
    """
    Returns a list of all reports by ID.
    """
    if not report_id or not isinstance(report_id, str):
        raise ReportIdException("Invalid Report ID")
    yield from Report.query.filter(report_id=report_id)


def delete_reports_by_report_id(
    report_id: str,
) -> typing.Generator[Report, None, None]:
    """
    Deletes reports from the database by ID.
    """
    if not report_id or not isinstance(report_id, str):
        raise ReportIdException("Invalid Report ID")
    try:
        for report in get_reports_by_report_id(report_id):
            report.delete()
            yield report
    except exc.SQLAlchemyError:
        db.session.rollback()
        raise


logger.info('Report controller initialized.')
