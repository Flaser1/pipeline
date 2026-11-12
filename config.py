

from dataclasses import dataclass
from pathlib import Path
from dotenv import dotenv_values


@dataclass(frozen=True)
class PipelineConfig:
    input_path: Path
    output_dir: Path


def load_config(dataset: str):
    base_dir = Path(__file__).resolve().parent
    env_path = base_dir / ".env"
    with env_path.open("r", encoding="utf-8", newline="") as file:
        properties = dotenv_values(stream=file, interpolate=False)

    input_path = get_required_value(properties, f"INPUT_PATH_{dataset}")
    output_dir = get_required_value(properties, f"OUTPUT_DIR_{dataset}")
    raw_columns = get_required_value(properties, f"EXPECTED_COLUMNS_{dataset}")
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