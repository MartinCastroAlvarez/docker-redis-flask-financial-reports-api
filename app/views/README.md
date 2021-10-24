# API Examples

## `/company/gb`

### GET
Listing all previous reports
```bash
curl -L -X 'GET' 'http://0.0.0.0:5000/company/gb'
```

## `/company/gb/<report>`

### GET
Listing a financial report.
```bash
curl -L -X 'GET' 'http://0.0.0.0:5000/company/gb/report1'
```

### PUT
Generating a new financial report.
```bash
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

### DELETE
Deleting a financial report.
```bash
curl -L -X 'DELETE' 'http://0.0.0.0:5000/company/gb/report1'
```
