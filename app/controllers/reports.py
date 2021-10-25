"""
Reports Controllers
https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
"""

import logging
import typing

from sqlalchemy import exc

from app.cache import cache
from app.db import db
from app.exceptions import AltmanException
from app.forms.financials import validate_financials
from app.models.report import Report

logger: logging.Logger = logging.getLogger(__name__)


class CompanyIdException(AltmanException):
    """Raised when the report ID is invalid."""

    CODE: int = 2000


class DuplicateException(AltmanException):
    """Raised when the report already exists."""

    CODE: int = 2001


def create_reports_by_company_id(
    company_id: str, financials: list
) -> typing.Generator[Report, None, None]:
    """
    Creates a new Report.
    """
    logger.debug("New Report: %s %s", company_id, financials)
    if not company_id or not isinstance(company_id, str):
        raise CompanyIdException("Invalid Report ID")
    cache_key: str = f"report-{company_id}"
    if cache.get(cache_key):
        raise DuplicateException("The Report has already been created!")
    validate_financials(financials)
    for financial in financials:
        report: Report = Report()
        report.company_id = company_id
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
        cache.set(cache_key, "1")
    except exc.IntegrityError as error:
        cache.set(cache_key, "1")
        raise DuplicateException("The Report already exists!") from error


def get_all_reports() -> typing.Generator[Report, None, None]:
    """
    Returns a list of all reports available.
    """
    logger.debug("List all Report")
    yield from Report.query.all()


def get_reports_by_company_id(
    company_id: str,
) -> typing.Generator[Report, None, None]:
    """
    Returns a list of all reports by ID.
    """
    logger.debug("Get Reports: %s", company_id)
    if not company_id or not isinstance(company_id, str):
        raise CompanyIdException("Invalid Report ID")
    yield from Report.query.filter_by(company_id=company_id)


def delete_reports_by_company_id(
    company_id: str,
) -> typing.Generator[Report, None, None]:
    """
    Deletes reports from the database by ID.
    """
    logger.debug("Delete Reports: %s", company_id)
    if not company_id or not isinstance(company_id, str):
        raise CompanyIdException("Invalid Report ID")
    for report in get_reports_by_company_id(company_id):
        db.session.delete(report)
        yield report


logger.info("Report controller initialized.")
