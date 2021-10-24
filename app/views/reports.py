"""
Flask Admin Blueprint
https://flask.palletsprojects.com/en/2.0.x/blueprints/
"""

# pylint: disable=broad-except

import json
import logging
import typing

from flask import Blueprint, request

from app.controllers import reports as reports_controllers
from app.models.report import Report

logger: logging.Logger = logging.getLogger(__name__)

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
        logger.debug("Reports: %ss", request.method)
        return {
            "reports": [
                report.to_json()
                for report in reports_controllers.get_all_reports()
            ]
        }
    except Exception as error:  # noqa
        logger.exception("Error: '%s/'", blue)
        return {
            "error": str(type(error)),
            "code": getattr(error, "CODE", "unknown"),
            "message": str(error).split("\n"),
        }


@blue.route("/<report_id>", methods=["GET", "PUT", "DELETE"])
def report_by_id(report_id: str) -> dict:
    """
    Returns a previously generated report.
    """
    try:
        logger.error(
            "Report By ID: %s %s %s",
            request.method,
            report_id,
            request.data,
        )
        reports: typing.Generator[Report, None, None]
        if request.method == "DELETE":
            reports = reports_controllers.delete_reports_by_report_id(
                report_id=report_id
            )
        elif request.method == "PUT":
            payload: dict = json.loads(request.data.decode("utf-8"))
            reports = reports_controllers.create_reports_by_report_id(
                report_id=report_id, financials=payload["financials"]
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
        logger.exception("Error: '%s/<report_id>'", blue)
        return {
            "error": str(type(error)),
            "code": getattr(error, "CODE", "unknown"),
            "message": str(error).split("\n"),
        }


logger.info("Reports Blueprint initialized: %s", blue)
