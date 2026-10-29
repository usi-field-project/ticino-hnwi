"""Fill the topic table of every destination sheet from the data register.

Reads 03_data/observations.csv, geographies.csv and indicators.csv and rewrites
only the table in each 04_benchmark/<destination>/README.md. Run again after
adding or correcting rows in observations.csv:

    python 04_benchmark/build_destination_sheets.py
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "03_data"
SHEETS = {
    "Ticino": "ticino", "Zug": "zug", "Zurich": "zurich", "Geneva": "geneva",
    "Graubünden": "graubuenden", "Monaco": "monaco", "Dubai": "dubai",
    "Lisbon": "lisbon", "Milan": "italy_milan", "London": "london",
    "Singapore": "singapore", "Luxembourg": "luxembourg",
}
SWISS = {"Ticino", "Zug", "Zurich", "Geneva", "Graubünden"}
TOPICS = ["Wealth", "Banking presence and density", "Business presence", "Employment",
          "Stability and institutions", "Quality of life", "Taxation and relocation",
          "Real estate", "Population and migration", "Healthcare", "Education"]
HEADER = ("| Topic | Findings / indicators | Sources | Reference period and geographical coverage "
          "| Gaps / comparability notes |\n|---|---|---|---|---|\n")
STATUS = ("Status: table filled from [`03_data/observations.csv`]({rel}03_data/observations.csv) "
          "with `04_benchmark/build_destination_sheets.py`; values are not verified yet "
          "(`to_verify`). Grades A/B/C are defined in the [benchmark methodology]({rel}02_methodology/benchmark_methodology.md#comparability-grade). Correct the data register, not this table, then run the script again.")

obs = pd.read_csv(DATA / "observations.csv", dtype=str).fillna("")
geo = pd.read_csv(DATA / "geographies.csv", dtype=str).fillna("")
ind = pd.read_csv(DATA / "indicators.csv", dtype=str).fillna("")
geo_name = dict(zip(geo.geo_id, geo.name))
geo_dest = dict(zip(geo.geo_id, geo.destination))
label = dict(zip(ind.indicator_id, ind.label))
obs["destination"] = obs.geo_id.map(geo_dest)


def esc(text):
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def fmt_value(r):
    v = r.value
    try:
        x = float(v)
        v = f"{x:,.0f}" if x.is_integer() and abs(x) >= 1000 else (f"{x:,.2f}".rstrip("0").rstrip(".") if abs(x) >= 1000 else v)
        v = v.replace(",", "'")
    except ValueError:
        pass
    unit = r.unit.replace("currency (million)", f"million {r.currency or 'currency'}")
    unit = unit.replace("currency", r.currency or "currency")
    if unit == "persons" or unit == "count":
        unit = ""
    elif unit == "yes/no":
        unit = ""
    return f"{v} {unit}".strip()


def cell_findings(rows):
    out = []
    for r in rows.itertuples():
        where = "" if r.geo_match == "exact" and r.destination != "Switzerland (national)" else f", {geo_name.get(r.geo_id, r.geo_id)}"
        out.append(f"{esc(label.get(r.indicator_id, r.indicator_id))}: **{esc(fmt_value(r))}** ({r.period}{esc(where)}) `{r.obs_id}`")
    return "<br>".join(out)


def cell_sources(rows):
    seen, out = set(), []
    for r in rows.itertuples():
        key = r.source_publisher
        if key in seen:
            continue
        seen.add(key)
        out.append(f"[{esc(key)}]({r.source_url})" if r.source_url.startswith("http") else esc(key))
    return "<br>".join(out)


def cell_coverage(rows):
    periods = sorted(set(rows.period))
    span = periods[0] if len(periods) == 1 else f"{periods[0]} to {periods[-1]}"
    geos = []
    for g, m in rows[["geo_id", "geo_match"]].drop_duplicates().itertuples(index=False):
        geos.append(f"{geo_name.get(g, g)}" + ("" if m == "exact" else f" ({m.replace('_', ' ')})"))
    return f"{span}; " + ", ".join(dict.fromkeys(geos))


def cell_gaps(rows):
    out = []
    weak = rows[rows.comparability.isin(["B", "C"])]
    for r in weak.itertuples():
        out.append(f"`{r.obs_id}` grade {r.comparability}")
    n_a = (rows.comparability == "A").sum()
    head = f"{n_a} of {len(rows)} values grade A"
    if (rows.status == "example").any():
        head += "; includes sample rows (`example`)"
    return esc(head + ("; " + ", ".join(out) if out else ""))


def build_table(dest):
    rows = obs[obs.destination == dest]
    if dest in SWISS:
        rows = pd.concat([rows, obs[obs.destination == "Switzerland (national)"]])
    lines = [HEADER]
    for t in TOPICS:
        r = rows[rows.topic == t]
        if r.empty:
            lines.append(f"| **{t}** | No data in the register yet |  |  | To collect |\n")
        else:
            lines.append(f"| **{t}** | {cell_findings(r)} | {cell_sources(r)} | {esc(cell_coverage(r))} | {cell_gaps(r)} |\n")
    return "".join(lines)


for dest, folder in SHEETS.items():
    path = ROOT / "04_benchmark" / folder / "README.md"
    text = path.read_text(encoding="utf-8")
    start = text.index("| Topic |")
    end = start
    lines = text[start:].splitlines(keepends=True)
    for line in lines:
        if not line.startswith("|"):
            break
        end += len(line)
    rel = "../" * (folder.count("/") + 2)
    out_lines = []
    for line in text[:start].splitlines(keepends=True):
        out_lines.append(STATUS.format(rel=rel) + "\n" if line.startswith("Status:") else line)
    path.write_text("".join(out_lines) + build_table(dest) + text[end:], encoding="utf-8")
    print(f"{dest}: {len(obs[obs.destination == dest])} values")
