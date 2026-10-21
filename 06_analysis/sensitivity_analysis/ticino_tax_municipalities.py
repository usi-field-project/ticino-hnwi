"""Tax sensitivity within Ticino: same reference taxpayer in every Ticino municipality.

Source: ESTV, Steuerbelastung in den Gemeinden 2026 (all municipalities),
single person, no children, no church tax. Reference case: taxable income
CHF 1m, net wealth CHF 10m. Output: CSV ranked by total difference vs Lugano.
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
ESTV = ROOT / "04_benchmark/contributor_data/elena/zurigo/07_tasse e residenza/onere fiscale e aliquote (ESTV)"
INCOME, WEALTH = 1_000_000.0, 10_000_000.0


def load(name, col, label):
    df = pd.read_excel(ESTV / name, header=8)
    df = df[df["Cantone"] == "TI"][["ID UST", "Comune", col]]
    return df.rename(columns={"ID UST": "bfs_id", "Comune": "municipality", col: label})


inc = load("onere_reddito_persona-sola_CHF_2026_tutti-comuni.xlsx", INCOME, "income_tax_chf")
wea = load("onere_sostanza_persona-sola_CHF_2026_tutti-comuni.xlsx", WEALTH, "wealth_tax_chf")
df = inc.merge(wea, on=["bfs_id", "municipality"])
df["income_tax_pct"] = (df.income_tax_chf / INCOME * 100).round(2)
df["wealth_tax_pct"] = (df.wealth_tax_chf / WEALTH * 100).round(3)
lug = df[df.municipality == "Lugano"].iloc[0]
df["diff_vs_lugano_chf"] = (df.income_tax_chf - lug.income_tax_chf) + (df.wealth_tax_chf - lug.wealth_tax_chf)
df = df.sort_values(["diff_vs_lugano_chf", "municipality"]).reset_index(drop=True)
df.insert(0, "rank", df.diff_vs_lugano_chf.rank(method="min").astype(int))
df.to_csv(Path(__file__).with_name("ticino_tax_municipalities_2026.csv"), index=False)
print(df.to_string(index=False))
