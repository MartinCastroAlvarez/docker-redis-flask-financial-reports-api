# API Examples

## `/company/gb`

### GET
Listing all previous reports
```bash
curl -L -X 'GET' 'http://0.0.0.0:5000/company/gb'
```
Returns:
``` bash
{
  "reports": [
    {
      "equity": 234.56,
      "id": "report1",
      "retained_earnings": 345.67,
      "sales": 1234.56,
      "score": 6.07242023479448,
      "total_assets": 345.67,
      "total_liabilities": 456.78,
      "year": 2020
    }
  ]
}
```

## `/company/gb/<report>`

### GET
Listing a financial report.
```bash
curl -L -X 'GET' 'http://0.0.0.0:5000/company/gb/report1'
```
Returns:
``` bash
{
  "reports": [
    {
      "equity": 234.56,
      "id": "report1",
      "retained_earnings": 345.67,
      "sales": 1234.56,
      "score": 6.07242023479448,
      "total_assets": 345.67,
      "total_liabilities": 456.78,
      "year": 2020
    }
  ]
}
```

### PUT
Generating a new financial report.
``` bash
curl -L \
	-X 'PUT' \
	-H 'content-type: application/json' \
	-d '{
		"financials": [
			{
				"year": 2020,
				"ebit": 123.45,
				"equity": 234.56,
				"retained_earnings": 345.67,
				"sales": 1234.56,
				"total_assets": 345.67,
				"total_liabilities": 456.78
			}
		]
	}' \
	'http://0.0.0.0:5000/company/gb/report1'
```
Returns:
``` bash
{
  "reports": [
    {
      "equity": 234.56,
      "id": "report1",
      "retained_earnings": 345.67,
      "sales": 1234.56,
      "score": 6.07242023479448,
      "total_assets": 345.67,
      "total_liabilities": 456.78,
      "year": 2020
    }
  ]
}
```
If the Report already exists:
``` bash
{
  "code": 2001,
  "error": "<class 'app.controllers.reports.DuplicateException'>",
  "message": [
    "The Report already exists!"
  ]
}
```
If there is any missing value:
```bash
{
  "code": 3000,
  "error": "<class 'app.forms.financials.FinancialsException'>",
  "message": [
    "Invalid financials sales."
  ]
}
```

### DELETE
Deleting a financial report.
```bash
curl -L -X 'DELETE' 'http://0.0.0.0:5000/company/gb/report1'
```
Returns:
``` bash
{
  "reports": [
    {
      "equity": 234.56,
      "id": "report1",
      "retained_earnings": 345.67,
      "sales": 1234.56,
      "score": 6.07242023479448,
      "total_assets": 345.67,
      "total_liabilities": 456.78,
      "year": 2020
    }
  ]
}
```
