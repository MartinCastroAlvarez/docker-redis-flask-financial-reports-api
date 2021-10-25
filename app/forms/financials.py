"""
Financial forms.
"""

from app.exceptions import AltmanException


class FinancialsException(AltmanException):
    """Raised when financials are invalid."""

    CODE: int = 3000


def validate_financials(financials: list) -> None:
    """
    Validates a list of financial reports.
    """
    if not isinstance(financials, list):
        raise FinancialsException("Invalid financials.")
    for financial in financials:
        validate_financial(financial)


def validate_financial(financial: dict) -> None:
    """
    Validates a financial report.
    """
    if not isinstance(financial, dict):
        raise FinancialsException("Invalid financials.")
    if (
        "year" not in financial
        or not isinstance(financial["year"], int)
        or financial["year"] < 0
    ):
        raise FinancialsException("Invalid financials year.")
    if (
        "ebit" not in financial
        or not isinstance(financial["ebit"], (int, float))
        or financial["ebit"] < 0
    ):
        raise FinancialsException("Invalid financials ebit.")
    if (
        "equity" not in financial
        or not isinstance(financial["equity"], (int, float))
        or financial["equity"] < 0
    ):
        raise FinancialsException("Invalid financials equity.")
    if (
        "sales" not in financial
        or not isinstance(financial["sales"], (int, float))
        or financial["sales"] < 0
    ):
        raise FinancialsException("Invalid financials sales.")
    if (
        "total_assets" not in financial
        or not isinstance(financial["total_assets"], (int, float))
        or financial["total_assets"] < 0
    ):
        raise FinancialsException("Invalid financials total_assets.")
    if (
        "total_liabilities" not in financial
        or not isinstance(financial["total_liabilities"], (int, float))
        or financial["total_liabilities"] < 0
    ):
        raise FinancialsException("Invalid financials total_liabilities.")
    if (
        "retained_earnings" not in financial
        or not isinstance(financial["retained_earnings"], (int, float))
        or financial["retained_earnings"] < 0
    ):
        raise FinancialsException("Invalid financials retained_earnings.")
