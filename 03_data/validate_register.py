"""Check the benchmark data register for missing or inconsistent fields.

Usage (from the repository root):
    python 03_data/validate_register.py

Errors must be fixed before a value is used in the benchmark; warnings are
information that is still missing (for example the access date).
"""
import csv
import re
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parent
ROOT = DATA.parent

REQUIRED = ["obs_id", "topic", "indicator_id", "geo_id", "geo_match", "value",
            "unit", "period", "source_publisher", "source_title",
            "comparability", "collected_by", "status"]
RECOMMENDED = ["source_url", "access_date", "local_file"]

GEO_MATCH = {"exact", "larger", "smaller", "national_proxy"}
COMPARABILITY = {"A", "B", "C"}
STATUS = {"example", "draft", "to_verify", "verified", "rejected"}
PERIOD = re.compile(r"^\d{4}(-\d{2}|-Q[1-4]|/\d{4})?$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def read(name):
    with open(DATA / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    geos = {g["geo_id"]: g for g in read("geographies.csv")}
    indicators = {i["indicator_id"]: i for i in read("indicators.csv")}
    obs = read("observations.csv")
    errors, warnings, seen = [], [], set()

    for n, row in enumerate(obs, start=2):
        where = f"observations.csv line {n} ({row.get('obs_id') or 'no id'})"
        for field in REQUIRED:
            if not (row.get(field) or "").strip():
                errors.append(f"{where}: '{field}' is empty")
        for field in RECOMMENDED:
            if not (row.get(field) or "").strip():
                warnings.append(f"{where}: '{field}' is empty")

        if row["obs_id"] in seen:
            errors.append(f"{where}: duplicate obs_id")
        seen.add(row["obs_id"])

        ind = indicators.get(row["indicator_id"])
        geo = geos.get(row["geo_id"])
        if row["indicator_id"] and not ind:
            errors.append(f"{where}: indicator '{row['indicator_id']}' is not in indicators.csv")
        if row["geo_id"] and not geo:
            errors.append(f"{where}: geo_id '{row['geo_id']}' is not in geographies.csv")
        if row["geo_match"] and row["geo_match"] not in GEO_MATCH:
            errors.append(f"{where}: geo_match must be one of {sorted(GEO_MATCH)}")
        if row["comparability"] and row["comparability"] not in COMPARABILITY:
            errors.append(f"{where}: comparability must be A, B or C")
        if row["status"] and row["status"] not in STATUS:
            errors.append(f"{where}: status must be one of {sorted(STATUS)}")
        if row["period"] and not PERIOD.match(row["period"]):
            errors.append(f"{where}: period '{row['period']}' should look like 2024, 2024-09, 2024-Q3 or 2023/2024")
        if row.get("access_date") and not DATE.match(row["access_date"]):
            errors.append(f"{where}: access_date should be YYYY-MM-DD")
        if row.get("local_file") and not (ROOT / row["local_file"]).exists():
            warnings.append(f"{where}: local_file not found in the repository")
        if row["value"]:
            try:
                float(row["value"])
            except ValueError:
                if ind and ind["unit"] != "yes/no":
                    errors.append(f"{where}: value '{row['value']}' is not a number (use a plain number, no thousands separators)")

        # Comparability rules from 02_methodology/benchmark_methodology.md
        if ind and ind["scope"] == "local" and row["geo_match"] not in ("", "exact") and row["comparability"] == "A":
            errors.append(f"{where}: local indicator on a non-exact territory cannot be grade A")
        if row["comparability"] in ("B", "C") and not row.get("comparability_note", "").strip():
            errors.append(f"{where}: grade {row['comparability']} needs a comparability_note")
        if geo and ind and ind["scope"] == "local" and row["geo_match"] == "exact" and geo["is_benchmark_unit"] != "yes":
            warnings.append(f"{where}: geo_match is 'exact' but {row['geo_id']} is not the benchmark unit")
        year = row["period"][:4]
        if year.isdigit() and int(year) < 2020 and row["comparability"] != "C":
            errors.append(f"{where}: data before 2020 should be grade C")

    for msg in errors:
        print("ERROR  ", msg)
    for msg in warnings:
        print("WARNING", msg)
    print(f"\n{len(obs)} observations checked: {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
