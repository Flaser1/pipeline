

import csv
from pathlib import Path


EXPECTED_COLUMNS_ORDERS = ["order_id", "customer_id", "amount", "status"]
EXPECTED_COLUMNS_CUSTOMERS = ["customer_id", "name", "country", "email"]

def read_orders(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")
        if reader.fieldnames != EXPECTED_COLUMNS_ORDERS:
            raise ValueError("Columns names do not match")
        rows = list(reader)
    return rows

def read_customers(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")
        if reader.fieldnames != EXPECTED_COLUMNS_CUSTOMERS:
            raise ValueError("Columns names do not match")
        rows = list(reader)
    return rows