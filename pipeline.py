

from pathlib import Path
from ingestion import read_csv

def run_pipeline_customers(input_path: Path, output_dir: Path, expected_columns: list[str]) -> list[dict]:
    return read_csv(input_path, expected_columns)

def run_pipeline_orders(input_path: Path, output_dir: Path, expected_columns: list[str]) -> list[dict]:
    return read_csv(input_path, expected_columns)