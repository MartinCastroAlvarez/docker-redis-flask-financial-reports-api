# Business Logic

### `create_reports_by_company_id`
Takes a Company ID and a list of financial reports to create a list of Reports in the database. It uses Redis to cache the reports that have been created so that the app does not have to try to write to the database to realse that it already exists.

### `get_all_reports`
Returns a list of all existing reports across all companies.

### `get_reports_by_company_id`
Returns a list of all existing reports related to a specific company.

### `delete_reports_by_company_id`
Deletes all the reports associated with a given company.
