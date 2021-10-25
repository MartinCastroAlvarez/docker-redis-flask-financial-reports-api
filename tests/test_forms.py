"""
Unit Tests.
https://pythonhosted.org/Flask-Testing/
"""

from unittest import TestCase

from app.forms import financials


class FinancialsFormTest(TestCase):
    """
    Testing Financials Form
    """

    def test_validate_financial(self) -> None:
        """
        Testing financials.validate_financial()
        """
        financials.validate_financial(
            {
                "year": 2010,
                "sales": 30,
                "total_assets": 20,
                "total_liabilities": 10,
                "ebit": 50,
                "equity": 20,
                "retained_earnings": 1,
            }
        )

    def test_validate_financials(self) -> None:
        """
        Testing financials.validate_financials()
        """
        financials.validate_financials(
            [
                {
                    "year": 2010,
                    "sales": 30,
                    "total_assets": 20,
                    "total_liabilities": 10,
                    "ebit": 50,
                    "equity": 20,
                    "retained_earnings": 1,
                }
            ]
        )

    def test_validate_financials_list(self) -> None:
        """
        Testing financials.validate_financials()
        """
        with self.assertRaises(financials.FinancialsException):
            financials.validate_financials({})

    def test_validate_financial_dict(self) -> None:
        """
        Testing financials.validate_financial()
        """
        with self.assertRaises(financials.FinancialsException):
            financials.validate_financial([])

    def test_validate_financial_retained_earnings(self) -> None:
        """
        Testing financials.validate_financial()
        """
        with self.assertRaises(financials.FinancialsException):
            financials.validate_financial(
                {
                    "year": 2010,
                    "sales": 30,
                    "total_assets": 20,
                    "total_liabilities": 10,
                    "ebit": 50,
                    "equity": 20,
                }
            )

    def test_validate_financial_equity(self) -> None:
        """
        Testing financials.validate_financial()
        """
        with self.assertRaises(financials.FinancialsException):
            financials.validate_financial(
                {
                    "year": 2010,
                    "sales": 30,
                    "total_assets": 20,
                    "total_liabilities": 10,
                    "ebit": 50,
                    "retained_earnings": 1,
                }
            )

    def test_validate_financial_ebit(self) -> None:
        """
        Testing financials.validate_financial()
        """
        with self.assertRaises(financials.FinancialsException):
            financials.validate_financial(
                {
                    "year": 2010,
                    "sales": 30,
                    "total_assets": 20,
                    "total_liabilities": 10,
                    "equity": 20,
                    "retained_earnings": 1,
                }
            )

    def test_validate_financial_total_liabilities(self) -> None:
        """
        Testing financials.validate_financial()
        """
        with self.assertRaises(financials.FinancialsException):
            financials.validate_financial(
                {
                    "year": 2010,
                    "sales": 30,
                    "total_assets": 20,
                    "ebit": 50,
                    "equity": 20,
                    "retained_earnings": 1,
                }
            )

    def test_validate_financial_total_assets(self) -> None:
        """
        Testing financials.validate_financial()
        """
        with self.assertRaises(financials.FinancialsException):
            financials.validate_financial(
                {
                    "year": 2010,
                    "sales": 30,
                    "total_liabilities": 10,
                    "ebit": 50,
                    "equity": 20,
                    "retained_earnings": 1,
                }
            )

    def test_validate_financial_sales(self) -> None:
        """
        Testing financials.validate_financial()
        """
        with self.assertRaises(financials.FinancialsException):
            financials.validate_financial(
                {
                    "year": 2010,
                    "total_assets": 20,
                    "total_liabilities": 10,
                    "ebit": 50,
                    "equity": 20,
                    "retained_earnings": 1,
                }
            )

    def test_validate_financial_year(self) -> None:
        """
        Testing financials.validate_financial()
        """
        with self.assertRaises(financials.FinancialsException):
            financials.validate_financial(
                {
                    "sales": 30,
                    "total_assets": 20,
                    "total_liabilities": 10,
                    "ebit": 50,
                    "equity": 20,
                    "retained_earnings": 1,
                }
            )
