"""Compare a freshly exported summary with reported results. Standard library only."""
import argparse
import csv
import json
import math
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("summary", type=Path)
args = parser.parse_args()
expected = json.loads((Path(__file__).resolve().parents[1] / "results/reported.json").read_text())
observed = {}
with args.summary.open(encoding="utf-8-sig", newline="") as stream:
    for row in csv.DictReader(stream):
        key = row["statistic"].strip()
        if key in observed:
            raise SystemExit(f"Duplicate statistic: {key}")
        observed[key] = float(row["value"])
errors = []
for key, target in expected.items():
    value = observed.get(key, math.nan)
    tolerance = 0 if isinstance(target, int) else 0.000001
    if not math.isclose(value, target, rel_tol=0, abs_tol=tolerance):
        errors.append(f"{key}: expected {target}, found {value}")
if errors:
    raise SystemExit("\n".join(errors))
print("All reported aggregate statistics agree. This check does not verify the pipeline.")
