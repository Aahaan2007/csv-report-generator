# CSV Sales Report Generator

A Python automation project that reads sales data from a CSV file, processes paid transactions, and generates a summarized sales report.

## Features

- Reads CSV files using Python's `csv` module.
- Validates required CSV columns.
- Aggregates paid transactions by customer.
- Ignores pending transactions.
- Handles invalid amounts, missing customer names, and invalid statuses.
- Supports negative adjustments to transaction totals.
- Generates a summarized CSV report.
- Uses logging to report skipped records and application events.
- Includes unit tests for important scenarios and edge cases.

## Project Structure

```text
csv-report-generator/
├── learningcsv.py
├── sales.csv
├── test_sales_report.py
├── tests/
│   └── test_data/
├── .gitignore
└── README.md
```

## Requirements

- Python 3
- No external Python packages required.

## Usage

1. Clone the repository.
2. Navigate into the project directory.
3. Place your input data in `sales.csv`.
4. Run the application:

```bash
python sales_report.py
```

The generated report will be saved as `paid_sales_report.csv`.

## Running Tests

Run the unit tests using:

```bash
python -m unittest -v
```

The test suite covers paid sales aggregation, pending transactions, invalid amounts, missing names, negative amounts, missing headers, empty CSV files, invalid statuses, logging, and missing input files.

## Technologies Used

- Python
- CSV module
- Logging
- Unittest
- File handling

## Project Status

Completed as a practical Python automation project.