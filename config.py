

from dataclasses import dataclass
from pathlib import Path
from dotenv import dotenv_values

@dataclass(frozen=True)
class PipelineConfig:
    input_path: Path
    output_dir: Path

def load_config_customers():
    base_dir = Path(__file__).resolve().parent
    env_path = base_dir / ".env"
    with env_path.open("r", encoding="utf-8", newline="") as file:
        properties = dotenv_values(stream=file, interpolate=False)

    input_path = get_required_value(properties, "INPUT_PATH_CUSTOMERS")
    output_dir = get_required_value(properties, "OUTPUT_DIR_CUSTOMERS")
    raw_columns = properties.get("EXPECTED_COLUMNS_CUSTOMERS")
    expected_columns = [column.strip() for column in raw_columns.split(",") if column.strip()]

    return PipelineConfig(
        base_dir / input_path,
        base_dir / output_dir
    ), expected_columns

def load_config_orders():
    base_dir = Path(__file__).resolve().parent
    env_path = base_dir / ".env"
    with env_path.open("r", encoding="utf-8", newline="") as file:
        properties = dotenv_values(stream=file, interpolate=False)

    input_path = get_required_value(properties, "INPUT_PATH_ORDERS")
    output_dir = get_required_value(properties, "OUTPUT_DIR_ORDERS")
    raw_columns = properties.get("EXPECTED_COLUMNS_ORDERS")
    expected_columns = [column.strip() for column in raw_columns.split(",") if column.strip()]

    return PipelineConfig(
        base_dir / input_path,
        base_dir / output_dir
    ), expected_columns

def get_required_value(properties: dict, key: str) -> str:
    value = properties.get(key)
    if value is None or not value.strip():
        raise ValueError(f"in .env {key} is missing")
    return value.strip()