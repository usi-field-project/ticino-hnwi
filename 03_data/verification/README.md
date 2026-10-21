# Verification pre-check

Status: automatic pre-check of all 319 rows of [`observations.csv`](../observations.csv), run on 21.10.2026 (updated the same day with the original sources downloaded for Luca's values). **No row has been marked `verified`**: the register rule is that a second team member opens the source and fills `verified_by` ([data README](../README.md)). This pre-check tells the reviewer which rows are already traced to their file and which need a closer look.

- Script: [`precheck.py`](precheck.py) (run `python 03_data/verification/precheck.py` from the repository root; it reads only the local files in `local_file`).
- Result, one row per observation: [`precheck.csv`](precheck.csv) (`precheck` and `precheck_note` columns).

## What the script checks

For every row it opens `local_file` (xlsx, csv, pdf, docx) and looks for the recorded value:

| Result | Meaning | Rows |
|---|---|---|
| `found` | The value appears in the source file (same number, at the recorded precision) | 160 |
| `recomputed_ok` | Value is a total or rate over a source table and the script recalculated it with the same result (hospital beds by canton, NOGA 64–66 employment, employment rate 15–64) | 12 |
| `derived_ok` | Value is a sum, difference, ratio or tax share of figures quoted in `comparability_note`, and those figures are in the file | 22 |
| `weak` | Found, but the number is short (one or two digits, e.g. 4 or 2.6) and could match elsewhere in the file: confirm the location | 55 |
| `found_scaled` | Found written in another unit (e.g. "86.0 billion" for 86,000 million): check the unit | 13 |
| `derived_partial` | Calculation checks out, but some inputs are not in the file (e.g. population from another source) | 11 |
| `derived` | Value not in the file, but figures in the note are: check the calculation by hand | 7 |
| `manual` | Yes/no or zero values (tax rules, restrictions): read the source | 33 |
| `no_text` | Source is an image-only PDF: no text to search (checked by eye, see below) | 5 |
| `not_found` | Value not found in the file | 1 (`LIS-023`, see below) |

194 rows (`found`, `recomputed_ok`, `derived_ok`) are ready for a quick second check; the other 125 need a closer look.

## Rows that need a closer look, by collector

| Collected by | Ready for quick check | Closer look |
|---|---|---|
| Elena | 130 | 60 |
| Luca | 36 | 37 |
| Nicole | 7 | 16 |
| Petra | 21 | 12 |

Filter `precheck.csv` by `collected_by` and by the results other than `found`, `recomputed_ok` and `derived_ok` to get each reviewer's list. Under the register rule, the second check is done by someone other than the collector.

## Points found during the check

- **Employment rate 15–64 from the BFS structural survey** (`ZG-007`, `ZH-026`, `TI-023`, `GE-019`, `GR-016`). The team's calculation, (active − unemployed) / population 15–64, is reproduced exactly. The same file also has a column called "Tasso di occupazione netto" (e.g. 72.0% for Ticino): it equals active / population, so it is a participation rate, not an employment rate, and should not be used instead. The structural-survey values remain well below the Eurostat 2025 values for the same cantons (Ticino 66.8% vs 71.5%), as the notes already say: the team should choose one source for scoring.
- **Values from reports rather than statistical tables** (Nicole's `Milano_Ginevra_Londra.docx`, Petra's workbook): the number is in the file, but the file is a summary written by the team, not the original source. The second check should open the original publication named in `source_title`.
- **Approximate values** (`LDN-006` ≈ 9.1 million, `LDN-008`, `LDN-009`, `MI-020` lower bound): traceable, but rounded in the source; keep the grade they have.

## Luca's values against the original sources

Until 21.10.2026 Luca's 73 values pointed to his summary workbook (`Zugo_Dubai_Lisbona_finale.xlsx`), so the pre-check only showed that they had been copied correctly from it. The original sources have now been downloaded into [`04_benchmark/contributor_data/luca/fonti/`](../../04_benchmark/contributor_data/luca/fonti/) and `local_file` points to them for 58 rows. The previous location in the workbook is kept in `comparability_note` ("Location in Luca's workbook").

Each row was also checked by reading the source (including the image-only Pordata PDF): [`luca_sources_check.csv`](luca_sources_check.csv).

| Result | Rows |
|---|---|
| Value confirmed in the original source | 55 |
| Value different from the source | 3 |
| Partly confirmed (value read from a chart) | 1 |
| Consistent with another official source in the repo | 1 |
| Source still missing or the wrong selection was downloaded | 13 |

**Values different from the source** (to correct in the register after the team agrees):

- `LIS-008` crime rate Grande Lisboa 2025: Pordata shows **31.6** (provisional), the register has 31.7; Portugal is 32.1, not 32.0 as in the note. Pordata revised 2021–2024 figures in June 2026.
- `LIS-023` IB schools Grande Lisboa: the saved search shows 5 schools and is not limited to Lisbon (it includes Dili and Madeira); the value 6 is not supported by this file.
- `ZG-006` financial-sector employment Zug 2024: the BFS STATENT file already in the repo gives **10,024** (NOGA 64 + 65 + 66), the register has 10,023.

**Sources still to download** (the file is missing or shows something else):

- `ZG-006`, `ZG-009`: the two PxWeb exports are for the canton of **Zurich**, not Zug (select Zug and export again).
- `LIS-018`: the Eurostat `demo_r_gind3` file shows "Population on 1 January"; select the indicator for net migration.
- `LIS-006`, `LIS-007`: only the Eurostat structure files (`dsd`) were downloaded; download the data (Download → Excel).
- `DXB-017`, `DXB-018`: the Our World in Data pages saved as PDF only show the first rows of the table; download the CSV ("Download full data").
- `ZG-010`, `ZG-011`: save the result of the ESTV tax calculator for the reference case.
- `DXB-007` (Gulf News), `DXB-015` (CBRE price per sq ft), `LIS-015` (INE), `LIS-020` (Eurostat `hlth_rs_bdsrg2`), `LIS-017` (no link in the register).

Files left out of the repository: a document unrelated to the project, a Pordata file for another municipality (Torre de Moncorvo), the Eurostat structure files and the PxWeb exports for Zurich.
