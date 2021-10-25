"""
Flask models
https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
"""

import logging

from app.db import db

logger: logging.Logger = logging.getLogger(__name__)


class Report(db.Model):
    """
    Report Model
    """

    company_id: db.Column = db.Column(db.String(50), primary_key=True)
    year: db.Column = db.Column(db.Integer, primary_key=True)
    ebit: db.Column = db.Column(
        db.Float(precision=10, asdecimal=True),
        nullable=False,
        default=0,
    )
    equity: db.Column = db.Column(
        db.Float(precision=10, asdecimal=True),
        nullable=False,
        default=0,
    )
    retained_earnings: db.Column = db.Column(
        db.Float(precision=10, asdecimal=True),
        nullable=False,
        default=0,
    )
    sales: db.Column = db.Column(
        db.Float(precision=10, asdecimal=True),
        nullable=False,
        default=0,
    )
    total_assets: db.Column = db.Column(
        db.Float(precision=10, asdecimal=True),
        nullable=False,
        default=0,
    )
    total_liabilities: db.Column = db.Column(
        db.Float(precision=10, asdecimal=True),
        nullable=False,
        default=0,
    )

    def __repr__(self) -> str:
        """
        String serializer.
        """
        return f"<Report: {self.company_id} {self.year}>"

    @property
    def working_capital(self) -> float:
        """
        The working capital calculation is: WC = Current Assets - Current Liabilities.

        NOTE: It is assumed that the company has no Non-Current Assets or Liabilities.
        """
        return self.total_assets - self.total_liabilities

    @property
    def liquid_assets(self) -> float:
        """
        Calculates the X1 ratio of the Altman Z-score.
        """
        try:
            return float(self.working_capital / self.total_assets)
        except ZeroDivisionError:
            return 0.0

    @property
    def profitability(self) -> float:
        """
        Calculates the X2 ratio of the Altman Z-score.
        """
        try:
            return float(self.retained_earnings / self.total_assets)
        except ZeroDivisionError:
            return 0.0

    @property
    def return_of_total_assets(self) -> float:
        """
        Calculates the X3 ratio of the Altman Z-score.
        """
        try:
            return float(self.ebit / self.total_assets)
        except ZeroDivisionError:
            return 0.0

    @property
    def financial_leverage(self) -> float:
        """
        Calculates the X4 ratio of the Altman Z-score.
        """
        try:
            return float(self.equity / self.total_liabilities)
        except ZeroDivisionError:
            return 0.0

    @property
    def asset_turnover(self) -> float:
        """
        Calculates the X5 ratio of the Altman Z-score.
        """
        try:
            return float(self.sales / self.total_assets)
        except ZeroDivisionError:
            return 0.0

    @property
    def score(self) -> float:
        """
        Calculates the Altman Z-score.
        """
        return sum(
            [
                1.2 * self.liquid_assets,
                1.4 * self.profitability,
                3.3 * self.return_of_total_assets,
                0.6 * self.financial_leverage,
                1.0 * self.asset_turnover,
            ]
        )

    def to_json(self) -> dict:
        """
        JSON serializer.
        """
        return {
            "id": self.company_id,
            "year": int(self.year),
            "equity": float(self.equity),
            "retained_earnings": float(self.retained_earnings),
            "sales": float(self.sales),
            "total_assets": float(self.total_assets),
            "total_liabilities": float(self.total_liabilities),
            "score": float(self.score),
        }


logger.info("Report model initialized: %s", Report)
