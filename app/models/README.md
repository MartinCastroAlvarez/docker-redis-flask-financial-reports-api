# Application Models

## [Report](./report.py)

#### Attributes

- `report_id`: `String`
- `year`: `Integer`
- `equity`: `Decimal`
- `retained_earnings`: `Decimal`
- `sales`: `Decimal`
- `total_assets`: `Decimal`
- `total_liabilities`: `Decimal`

#### Computed Attributes

- `score`: The Altman Z-Score
- `working_capital`: Total Assets minus Total Liabilities approximation.
- `liquid_assets`: Working Capital to Total Assets ratio.
- `profitability`: Retained Earnings to Total Assets ratio.
- `return_of_total_assets`:  EBIT to Total Assets ratio.
- `financial_leverage`: Equity to Total Liabilities ratio.
- `asset_turnover`: Sales to Total Assets ratio.
