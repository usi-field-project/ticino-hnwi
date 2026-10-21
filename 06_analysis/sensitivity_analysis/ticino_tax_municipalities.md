# Tax sensitivity within Ticino

Status: draft for team review; values `to_verify` in the data register.

## Question

Lugano is the reference municipality for Ticino tax profiles (agreed 19.10.2026). How much would the result change if a client chose another Ticino municipality?

## Data and method

- Source: ESTV/FTA, *Steuerbelastung in den Gemeinden 2026*, all municipalities (files in `04_benchmark/contributor_data/elena/zurigo/07_tasse e residenza/onere fiscale e aliquote (ESTV)/`).
- Reference case: single person, no children, no church tax; taxable income CHF 1m and net wealth CHF 10m. Total burden = federal + cantonal + municipal (income) and cantonal + municipal (wealth).
- Same reference case and dataset as the Lugano values (`TI-019`, `TI-020` in `03_data/observations.csv`).
- Script: [`ticino_tax_municipalities.py`](ticino_tax_municipalities.py). Full ranking of all 100 Ticino municipalities: [`ticino_tax_municipalities_2026.csv`](ticino_tax_municipalities_2026.csv).

## Results

| Municipality | Income tax (CHF 1m) | Wealth tax (CHF 10m) | Total vs Lugano (CHF/year) |
|---|---|---|---|
| Porza (lowest) | 29.1% | 0.39% | −30,400 |
| Paradiso | 29.3% | 0.40% | −27,500 |
| Collina d'Oro | 29.6% | 0.40% | −24,600 |
| Ascona / Muralto | 31.4% | 0.44% | −2,900 |
| **Lugano** | **31.6%** | **0.44%** | **0** |
| Locarno | 33.2% | 0.48% | +18,800 |
| Bellinzona | 33.5% | 0.48% | +23,200 |
| Verzasca, Lavertezzo (highest) | 34.4% | 0.50% | +33,300 |

## Reading

- Within Ticino, the choice of municipality moves the burden by about ±CHF 30,000 per year around Lugano for this profile, roughly 2–3 percentage points on income.
- Lugano ranks 30th of 100: in the lower part, but not the lowest. Neighbouring municipalities (Porza, Paradiso, Collina d'Oro) are cheaper and are the natural alternatives for a client relocating to the Lugano area.
- These differences are small compared with the gaps between countries in the international benchmark, so the choice of Lugano as reference municipality does not change the conclusions.

## Limitations

- One profile only (single, no children); married couples and other income/wealth levels are not covered.
- Church tax and lump-sum taxation are excluded.
- The sensitivity values (`TI-029` to `TI-034`) are grade C: context only, not used in scoring.
