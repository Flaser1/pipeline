

import csv
from pathlib import Path


def read_csv(path: Path, expected_columns: list[str]) -> list[dict]:
    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")
        for column in expected_columns:
            if column not in reader.fieldnames:
                raise ValueError(f"Column: {column} is missing in {path}")

        rows = list(reader)
    return rows