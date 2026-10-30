import csv
import unittest as ut
import learningcsv

class TestSalesReport(ut.TestCase):
    def test_paid_sales_aggregation(self):
        self.assertEqual(
            learningcsv.calculate_paid_sales("tests/test_data/test_sales.csv"), {"Alex": 300}
        )

    def test_unpaid_sales_ignored(self):
        self.assertEqual(
            learningcsv.calculate_paid_sales("tests/test_data/test_unpaid_sales.csv"), {"Jordan": 100}
        )

    def test_invalid_amounts(self):
        self.assertEqual(
            learningcsv.calculate_paid_sales("tests/test_data/test_invalid_amounts.csv"), {"Alex": 200, "Jordan": 100}
        )

    def test_missing_names(self):
        self.assertEqual(
            learningcsv.calculate_paid_sales("tests/test_data/test_missing_names.csv"), {"Alex": 200, "Jordan": 300}
        )

    def test_negative_numbers(self):
        self.assertEqual(
            learningcsv.calculate_paid_sales("tests/test_data/test_negative_numbers.csv"), {"Alex": 400, "Sam": 200}
        )

    def test_missing_headers(self):
        with self.assertRaises(ValueError):
            learningcsv.calculate_paid_sales('tests/test_data/test_missing_headers.csv')

    def test_empty(self):
        self.assertEqual(
            learningcsv.calculate_paid_sales("tests/test_data/test_empty.csv"), {}
        )

    def test_invalid_status(self):
        self.assertEqual(
            learningcsv.calculate_paid_sales("tests/test_data/test_invalid_status.csv"), {"Alex": 200}
        )
    def test_invalid_status_log(self):
        with self.assertLogs(level="WARNING") as captured:
            learningcsv.calculate_paid_sales("tests/test_data/test_invalid_status.csv")
        self.assertEqual(
            len(captured.output), 2
        )
        self.assertTrue(any("Jordan" in message for message in captured.output))
        self.assertTrue(any("Priya" in message for message in captured.output))

    def test_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            learningcsv.calculate_paid_sales("non.csv")

if __name__ == "__main__":
    ut.main()