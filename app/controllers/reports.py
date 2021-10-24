"""
Reports Controllers
https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
"""

import logging
import typing

from sqlalchemy import exc

from app.db import db
from app.exceptions import AltmanException
from app.forms.financials import validate_financials
from app.models.report import Report

logger: logging.Logger = logging.getLogger(__name__)


class ReportIdException(AltmanException):
    """Raised when the report ID is invalid."""
    CODE: int = 2000


class DuplicateException(AltmanException):
    """Raised when the report already exists."""
    CODE: int = 2001


def create_reports_by_report_id(
    report_id: str, financials: list
) -> typing.Generator[Report, None, None]:
    """
    Creates a new Report.
    """
    logger.debug("New Report: %s %s", report_id, financials)
    if not report_id or not isinstance(report_id, str):
        raise ReportIdException("Invalid Report ID")
    validate_financials(financials)
    for financial in financials:
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
    except exc.IntegrityError as error:
        raise DuplicateException('The Report already exists!') from error
    except exc.SQLAlchemyError:
        db.session.rollback()
        raise


def get_all_reports() -> typing.Generator[Report, None, None]:
    """
    Returns a list of all reports available.
    """
    logger.debug("List all Report")
    yield from Report.query.all()


def get_reports_by_report_id(
    report_id: str,
) -> typing.Generator[Report, None, None]:
    """
    Returns a list of all reports by ID.
    """
    logger.debug("Get Reports: %s", report_id)
    if not report_id or not isinstance(report_id, str):
        raise ReportIdException("Invalid Report ID")
    yield from Report.query.filter_by(report_id=report_id)


def delete_reports_by_report_id(
    report_id: str,
) -> typing.Generator[Report, None, None]:
    """
    Deletes reports from the database by ID.
    """
    logger.debug("Delete Reports: %s", report_id)
    if not report_id or not isinstance(report_id, str):
        raise ReportIdException("Invalid Report ID")
    try:
        for report in get_reports_by_report_id(report_id):
            report.delete()
            yield report
    except exc.SQLAlchemyError:
        db.session.rollback()
        raise


logger.info("Report controller initialized.")
