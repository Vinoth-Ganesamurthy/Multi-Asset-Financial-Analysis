from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Outputs
OUTPUT_DIR = PROJECT_ROOT / "outputs"
CHART_DIR = OUTPUT_DIR / "charts"
TABLE_DIR = OUTPUT_DIR / "tables"

# Reports
REPORT_DIR = PROJECT_ROOT / "reports"
FIGURE_DIR = REPORT_DIR / "figures"

# Models
MODEL_DIR = PROJECT_ROOT / "models"

# Create directories if they don't exist
for directory in [
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    CHART_DIR,
    TABLE_DIR,
    REPORT_DIR,
    FIGURE_DIR,
    MODEL_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)