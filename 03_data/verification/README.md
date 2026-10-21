# Verification pre-check

Status: automatic pre-check of all 319 rows of [`observations.csv`](../observations.csv), run on 21.10.2026. **No row has been marked `verified`**: the register rule is that a second team member opens the source and fills `verified_by` ([data README](../README.md)). This pre-check tells the reviewer which rows are already traced to their file and which need a closer look.

- Script: [`precheck.py`](precheck.py) (run `python 03_data/verification/precheck.py` from the repository root; it reads only the local files in `local_file`).
- Result, one row per observation: [`precheck.csv`](precheck.csv) (`precheck` and `precheck_note` columns).

## What the script checks

For every row it opens `local_file` (xlsx, csv, pdf, docx) and looks for the recorded value:

| Result | Meaning | Rows |
|---|---|---|
| `found` | The value appears in the source file (same number, at the recorded precision) | 169 |
| `recomputed_ok` | Value is a total or rate over a source table and the script recalculated it with the same result (hospital beds by canton, NOGA 64–66 employment, employment rate 15–64) | 12 |
| `derived_ok` | Value is a sum, difference, ratio or tax share of figures quoted in `comparability_note`, and those figures are in the file | 22 |
| `weak` | Found, but the number is short (one or two digits, e.g. 4 or 2.6) and could match elsewhere in the file: confirm the location | 58 |
| `found_scaled` | Found written in another unit (e.g. "86.0 billion" for 86,000 million): check the unit | 11 |
| `derived_partial` | Calculation checks out, but some inputs are not in the file (e.g. population from another source) | 9 |
| `derived` | Value not in the file, but figures in the note are: check the calculation by hand | 5 |
| `manual` | Yes/no or zero values (tax rules, restrictions): read the source | 33 |
| `not_found` | Value not found in the file | 0 |

**Every value was traced to its source file or to a calculation from it.** 203 rows (`found`, `recomputed_ok`, `derived_ok`) are ready for a quick second check; 116 need a closer look.

## Rows that need a closer look, by collector

| Collected by | Ready for quick check | Closer look |
|---|---|---|
| Elena | 130 | 60 |
| Luca | 45 | 28 |
| Nicole | 7 | 16 |
| Petra | 21 | 12 |

Filter `precheck.csv` by `collected_by` and by the results other than `found`, `recomputed_ok` and `derived_ok` to get each reviewer's list. Under the register rule, the second check is done by someone other than the collector.

## Points found during the check

- **Employment rate 15–64 from the BFS structural survey** (`ZG-007`, `ZH-026`, `TI-023`, `GE-019`, `GR-016`). The team's calculation, (active − unemployed) / population 15–64, is reproduced exactly. The same file also has a column called "Tasso di occupazione netto" (e.g. 72.0% for Ticino): it equals active / population, so it is a participation rate, not an employment rate, and should not be used instead. The structural-survey values remain well below the Eurostat 2025 values for the same cantons (Ticino 66.8% vs 71.5%), as the notes already say: the team should choose one source for scoring.
- **Values from reports rather than statistical tables** (Nicole's `Milano_Ginevra_Londra.docx`, Petra's workbook): the number is in the file, but the file is a summary written by the team, not the original source. The second check should open the original publication named in `source_title`.
- **Approximate values** (`LDN-006` ≈ 9.1 million, `LDN-008`, `LDN-009`, `MI-020` lower bound): traceable, but rounded in the source; keep the grade they have.
