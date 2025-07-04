#!/usr/bin/env bash
set -euo pipefail

echo "=== Running Project Alpha Analysis ==="

# Load configuration
CONFIG_FILE="config/config.yaml"
if [[ ! -f "$CONFIG_FILE" ]]; then
  echo "Config file $CONFIG_FILE not found!"
  exit 1
fi

DATA_PATH=$(python - << 'PYCODE'
import yaml
cfg = yaml.safe_load(open("config/config.yaml"))
print(cfg.get("data_path", "data/input/sample.csv"))
PYCODE
)

echo "Processing data at $DATA_PATH..."
python - << 'PYCODE'
from project_alpha.data_processing import process_data
from project_alpha.analysis import analyze

df = process_data("$DATA_PATH")
analyze(df)
PYCODE

echo "=== Analysis complete ==="
