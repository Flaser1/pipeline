

from pathlib import Path
from ingestion import read_csv

def run_pipeline(input_path: Path, output_dir: Path):
    return read_csv(input_path)
