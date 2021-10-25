# [Unit Tests](https://en.wikipedia.org/wiki/Unit_testing)

> In computer programming, unit testing is a software testing method by which individual units of source code—sets of one or more computer program modules together with associated control data, usage procedures, and operating procedures—are tested to determine whether they are fit for use.

## Usage
Run the test script.
```bash
./bin/test.sh
```
Returns:
```bash
.......................................
Name                          Stmts   Miss  Cover   Missing
-----------------------------------------------------------
app/__init__.py                  26      0   100%
app/cache.py                      5      0   100%
app/controllers/__init__.py       0      0   100%
app/controllers/reports.py       55      0   100%
app/db.py                         5      0   100%
app/exceptions.py                 2      0   100%
app/forms/financials.py          25      0   100%
app/models/__init__.py            0      0   100%
app/models/report.py             63      0   100%
app/views/__init__.py             0      0   100%
app/views/reports.py             33      0   100%
-----------------------------------------------------------
TOTAL                           214      0   100%
----------------------------------------------------------------------
Ran 39 tests in 0.322s

OK
```

## Test Framework

- [API](./test_api.py): Testing API endpoints.
- [Views](./test_views.py): Testing Views.
- [Controllers](./test_controllres.py): Testing Controller functions.
- [Models](./test_models.py): Testing Model classes.
- [Forms](./test_forms.py): Testing Form functions.
