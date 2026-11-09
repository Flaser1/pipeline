

from pathlib import Path
from ingestion import read_orders, read_customers

def run_pipeline_customers(input_path: Path, output_dir: Path):
    return read_customers(input_path)

def run_pipeline_orders(input_path: Path, output_dir: Path):
    return read_orders(input_path)