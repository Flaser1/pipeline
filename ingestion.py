

import csv
from pathlib import Path


def read_csv(path: Path, expected_columns: list[str]) -> list[dict]:
    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")
        if reader.fieldnames is None:
            raise ValueError(f"{path} is empty")
        missing_columns = [column for column in expected_columns if column not in reader.fieldnames]
        if missing_columns:
            raise ValueError(f"Columns: {', '.join(missing_columns)} are missing in {path}")
        rows = list(reader)
    return rows