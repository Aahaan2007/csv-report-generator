import csv
import logging
import os

logging.basicConfig(level=logging.INFO)

def calculate_paid_sales(input_file):
    with open(input_file, "r", newline="") as file:
        leads = csv.DictReader(file)
        required_columns = {"customer", "amount", "status"}
        if not required_columns.issubset(leads.fieldnames or []):
            raise ValueError("CSV file missing one or more required columns.")
        paid_sales = {}
        skipped_rows = 0
        for lead in leads:
            name = lead.get("customer", "").strip()
            if not name:
                logging.warning("no name found")
                skipped_rows += 1
                continue
            try:
                amount = int(lead["amount"])
            except (ValueError, TypeError, KeyError):
                logging.warning(f"{name} was skipped because its amount was invalid")
                skipped_rows += 1
                continue
            status = lead.get("status", "").strip().lower()
            if status == "paid":
                if name in paid_sales:
                    paid_sales[name] += amount
                else:
                    paid_sales[name] = amount
            elif status == "pending":
                continue
            else:
                logging.warning(f'{name} skipped as invalid status.')
    logging.info(f"{skipped_rows} rows skipped.")
    return paid_sales

try:
    paid_sales = calculate_paid_sales("sales.csv")
except FileNotFoundError:
    print("file not found")
except ValueError:
    print("wrong headers in file")

def write_report(paid_sales, output_file):
    with open(output_file, "w", newline="") as file:
        fieldnames = ["customer", "total_paid"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for customer, total_paid in paid_sales.items():
            if total_paid > 0:
                writer.writerow({
                    "customer": customer,
                    "total_paid": total_paid
                })

    logging.info(f"{output_file} generated successfully.")

def main():
    input_file = os.path.abspath("sales.csv")
    output_file = os.path.abspath("paid_sales_report.csv")

    try:
        if input_file == output_file:
            raise ValueError("Input and output files cannot be the same.")
    except ValueError as e:
        logging.error(e)
        return

    try:
        paid_sales = calculate_paid_sales(input_file)
    except FileNotFoundError:
        logging.error("file not found")
        return
    except ValueError:
        logging.error("wrong headers in file")
        return

    try:
        write_report(paid_sales, output_file)
    except PermissionError:
        logging.error("Permission to write denied.")
        return

if __name__ == "__main__":
    main()


