"""
Flask Admin Blueprint
https://flask.palletsprojects.com/en/2.0.x/blueprints/
"""

import typing
import logging

from flask import Blueprint, request

from app.models.report import Report

from app.controllers import reports as reports_controllers

logger: logging.RootLogger = logging.getLogger(__name__)

blue: Blueprint = Blueprint(
    "reports", __name__, url_prefix="/company/gb"
)


@blue.route(
    "/",
    methods=[
        "GET",
    ],
)
def all_reports() -> dict:
    """
    Returns a list of all the Reports or creates one.
    """
    try:
        return {
            "reports": [
                report.to_json()
                for report in reports_controllers.get_all_reports()
            ]
        }
    except Exception as error:  # noqa
        logger.exception(f"Error: '{blue}/'")
        return {
            "code": type(error),
            "message": str(error),
        }


@blue.route("/<report_id>", methods=["GET", "PUT", "DELETE"])
def report_by_id(report_id: str) -> dict:
    """
    Returns a previously generated report.
    """
    try:
        reports: typing.Generator[Report, None, None]
        if request.method == "DELETE":
            reports = reports_controllers.delete_reports_by_report_id(
                report_id=report_id
            )
        elif request.method == "PUT":
            financials: typing.Union[
                typing.List, typing.Any
            ] = request.args.get("financials", [])
            reports = reports_controllers.create_reports_by_report_id(
                report_id=report_id, financials=financials
            )
        elif request.method == "GET":
            reports = reports_controllers.get_reports_by_report_id(
                report_id=report_id
            )
        response: dict = {
            "reports": [report.to_json() for report in reports]
        }
        return response
    except Exception as error:  # noqa
        logger.exception(f"Error: '{blue}/<report_id>'")
        return {
            "code": type(error),
            "message": str(error),
        }


logger.info('Reports Blueprint initialized:', blue)
