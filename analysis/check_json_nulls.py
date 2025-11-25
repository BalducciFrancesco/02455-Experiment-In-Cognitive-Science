import json
import math
from pathlib import Path

JSON_PATH = Path(__file__).parent / "experiment_data.json"
REPORT_PATH = Path(__file__).parent / "missing_report.txt"

def is_missing(v):
    if v is None:
        return True
    if isinstance(v, float) and math.isnan(v):
        return True
    if isinstance(v, str) and v.strip().lower() in ("", "nan", "none", "null"):
        return True
    return False

def find_missing(obj, path="root"):
    missing = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            missing += find_missing(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            missing += find_missing(v, f"{path}[{i}]")
    else:
        if is_missing(obj):
            missing.append((path, obj))
    return missing

def main():
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    missing = find_missing(data, "root")
    with REPORT_PATH.open("w", encoding="utf-8") as f:
        if not missing:
            out = "No missing values found.\n"
            print(out.strip())
            f.write(out)
            return
        summary = f"Found {len(missing)} missing values. Showing up to 200 entries:\n\n"
        print(summary.strip())
        f.write(summary)
        for path, val in missing[:200]:
            line = f"{path} -> {repr(val)}\n"
            print(line.strip())
            f.write(line)

if __name__ == "__main__":
    main()