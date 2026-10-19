# Data coverage by destination

Status: **working check, 19 October 2026**. It shows which indicators of the [indicator matrix](../02_methodology/indicator_matrix.md) are already covered by the material each team member collected in [contributor_data](contributor_data/). Nothing has been copied into [`observations.csv`](../03_data/observations.csv) yet and no value has been verified against its source.

The cell-by-cell detail (value found, file, owner) is in [`03_data/coverage.csv`](../03_data/coverage.csv): filter it by `owner` to get your own to-do list.

## Legend

| Symbol | Meaning | Next step |
|---|---|---|
| ✅ | Value already extracted in a team workbook or table, matching the matrix definition and territory | Copy into `observations.csv` with source and period |
| 🟡 | Value extracted, but proxy: different territory (e.g. national), different definition, range or very old year | Record with grade B/C, or look for a better source |
| 📁 | Source file already downloaded, value not yet extracted | Extract the value from the file |
| ❌ | Nothing found in the collected material | Collect, or drop the indicator if it is optional |

## Coverage grid

| Code | Indicator | Ticino | Zug | Zurich | Geneva | Graubünden | Monaco | Singapore | Luxembourg | Dubai | Lisbon | London | Milan |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| W1 | GDP per capita | ❌ | ❌ | ❌ | 🟡 | ❌ | 📁 | ❌ | ❌ | ❌ | 🟡 | ✅ | 🟡 |
| W2 | Millionaires per 1,000 residents | ❌ | 🟡 | 📁 | ✅ | 🟡 | 📁 | 📁 | ❌ | ✅ | 🟡 | ✅ | ✅ |
| W3 | Resident centi-millionaires | ❌ | ✅ | 📁 | ✅ | ❌ | 📁 | 📁 | ❌ | ✅ | 🟡 | ✅ | ✅ |
| B1 | Banks headquartered | ✅ | ✅ | 📁 | 🟡 | ❌ | 🟡 | 📁 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 |
| B2 | Bank offices per 100,000 residents | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | 🟡 | ❌ | 🟡 | 🟡 | ❌ | ❌ |
| B3 | Financial-sector employment share | 🟡 | ✅ | 📁 | 🟡 | ❌ | 📁 | 📁 | ✅ | 🟡 | ❌ | 🟡 | 🟡 |
| E1 | Local establishments per 1,000 residents | ✅ | ✅ | ✅ | ✅ | ✅ | 📁 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 |
| E2 | New companies per 1,000 residents | ❌ | ❌ | 📁 | 🟡 | 🟡 | ❌ | 📁 | ❌ | ✅ | ❌ | 🟡 | ✅ |
| L1 | Employment rate 15–64 | 🟡 | ✅ | 📁 | ❌ | 🟡 | ❌ | 🟡 | 🟡 | 🟡 | ✅ | ❌ | 🟡 |
| L2 | Unemployment rate (ILO) | ✅ | ✅ | 📁 | ❌ | 🟡 | 📁 | 📁 | ✅ | 🟡 | ✅ | ❌ | ❌ |
| L3 | Median gross monthly wage | ✅ | ❌ | ✅ | ✅ | ❌ | 📁 | ❌ | ❌ | ❌ | ❌ | 🟡 | 🟡 |
| S1 | WGI Rule of Law | ✅ | ✅ | ✅ | ✅ | ✅ | 📁 | 📁 | ✅ | ✅ | ✅ | 📁 | 📁 |
| S2 | WGI Political Stability | ✅ | ✅ | ✅ | ✅ | ✅ | 📁 | 📁 | 📁 | ✅ | ✅ | 📁 | 📁 |
| S3 | Sovereign credit rating | ❌ | ❌ | 🟡 | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |
| S4 | Basel AML Index | ❌ | ❌ | ❌ | ❌ | ❌ | 🟡 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Q1 | Recorded offences per 1,000 residents | ✅ | ✅ | 📁 | 🟡 | ✅ | 📁 | 📁 | ✅ | 🟡 | ✅ | 🟡 | 🟡 |
| Q2 | PM2.5 annual mean | ✅ | ❌ | 📁 | 🟡 | 🟡 | 📁 | 📁 | 🟡 | ❌ | ✅ | 🟡 | 🟡 |
| Q3 | Cost of living | ❌ | 🟡 | ❌ | ✅ | ❌ | ❌ | 🟡 | 🟡 | 🟡 | 🟡 | ✅ | ✅ |
| Q4 | Direct international destinations from main airport | ❌ | ❌ | 📁 | ❌ | ❌ | 🟡 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Q5 | Travel time to nearest intercontinental hub | 🟡 | ❌ | ❌ | ❌ | 🟡 | ❌ | ❌ | 🟡 | ❌ | ❌ | ❌ | ❌ |
| T1 | Effective income tax, reference case | 🟡 | ✅ | 📁 | 📁 | 🟡 | 📁 | 📁 | 🟡 | ✅ | ✅ | ❌ | ❌ |
| T2 | Effective wealth tax, reference case | 🟡 | ✅ | 📁 | 📁 | 🟡 | 📁 | 📁 | ❌ | ✅ | ✅ | ✅ | 🟡 |
| T3 | Inheritance tax, direct descendants | ✅ | ✅ | 📁 | ❌ | 🟡 | 📁 | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| T4 | Special regime for new residents | ✅ | ✅ | 📁 | 🟡 | 🟡 | 📁 | ❌ | 🟡 | ✅ | ✅ | ✅ | ✅ |
| T5 | Investor or financially independent residence route | ✅ | ✅ | 📁 | ❌ | ✅ | 📁 | 📁 | ❌ | ✅ | ✅ | ❌ | ❌ |
| R1 | Prime residential price per m² | 🟡 | 🟡 | 📁 | ✅ | ❌ | 📁 | 📁 | 🟡 | ✅ | 🟡 | ✅ | ✅ |
| R2 | Prime price change y/y | 🟡 | 🟡 | 📁 | 🟡 | 🟡 | 📁 | 📁 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 |
| R3 | Restrictions on foreign buyers | 🟡 | ✅ | 📁 | 🟡 | 🟡 | ❌ | 📁 | ❌ | ✅ | ✅ | ❌ | ❌ |
| P1 | Resident population | ✅ | ✅ | 📁 | ✅ | ✅ | 📁 | 📁 | ✅ | ✅ | ✅ | ✅ | 🟡 |
| P2 | Share of foreign residents | ✅ | ✅ | 📁 | ✅ | ✅ | 📁 | 📁 | ✅ | ✅ | 🟡 | 🟡 | 🟡 |
| P3 | Net international migration per 1,000 residents | ✅ | ✅ | 📁 | 🟡 | 🟡 | ❌ | 📁 | ✅ | ❌ | 🟡 | ✅ | 🟡 |
| H1 | Practising physicians per 100,000 residents | ❌ | ✅ | 📁 | ❌ | ❌ | 📁 | ❌ | ❌ | 🟡 | ✅ | ❌ | ❌ |
| H2 | Hospital beds per 1,000 residents | ❌ | ✅ | 📁 | ✅ | 🟡 | 🟡 | 📁 | ✅ | 🟡 | ✅ | ✅ | ✅ |
| H3 | Life expectancy at birth | ❌ | 🟡 | ❌ | 🟡 | ❌ | 📁 | 📁 | ✅ | ❌ | ✅ | 🟡 | ✅ |
| D1 | International schools | 🟡 | ✅ | 📁 | 🟡 | ❌ | 📁 | 📁 | 🟡 | 🟡 | ✅ | 🟡 | ✅ |
| D2 | Universities in global rankings | ❌ | 🟡 | 📁 | ✅ | ❌ | ❌ | 📁 | ❌ | ❌ | ❌ | ✅ | ✅ |
| D3 | Tertiary-educated population 25–64 | ❌ | 🟡 | ❌ | ❌ | 🟡 | ❌ | ❌ | 🟡 | ❌ | ✅ | ❌ | ❌ |
| | **✅ / 🟡 / 📁 / ❌** | 15/9/0/13 | 22/7/0/8 | 5/1/25/6 | 12/12/2/11 | 7/15/0/15 | 0/4/23/10 | 2/4/23/8 | 10/12/1/14 | 15/12/0/10 | 18/11/0/8 | 11/11/2/13 | 10/13/2/12 |

Totals over 444 cells: 127 ✅, 111 🟡, 78 📁, 128 ❌.

## What this shows

**Well covered** (usable for almost all destinations): WGI (S1, S2), population and foreign residents (P1, P2), establishments (E1), recorded crime (Q1), inheritance tax and special regimes (T3, T4), hospital beds (H2).

**Weak core indicators**, to collect centrally or reconsider:

| Code | Indicator | Issue | Suggestion |
|---|---|---|---|
| W1 | GDP per capita | 1 ✅, 7 ❌ | One person collects it for all destinations from the same type of source (regional accounts) |
| B2 | Bank offices per 100,000 residents | Definitions differ abroad (branches, credit institutions, per 100k adults) | Keep for the Swiss cantons (SNB); abroad only as grade B |
| Q4, Q5 | Accessibility | Almost nothing collected, except Singapore | One person collects both for all 12 destinations with the same method |
| H1 | Physicians | 2 ✅ | Collect centrally or replace with hospital beds (H2) |
| D2 | Universities in rankings | 3 ✅ | One person counts all destinations from the full QS 2027 ranking (the file in `elena/zurigo/11_istruzione` is a one-page capture) |
| R1, R2 | Prime prices | Swiss cantons have no "prime" figures; most values are averages | Ask UBS for luxury transaction prices (already noted by Luca), otherwise keep R1 as context |

**Optional indicators that could be dropped**: S3 sovereign rating (1 ✅), S4 Basel AML Index (0 ✅), D3 tertiary education (1 ✅), R2 prime price change (0 ✅).

## Shared sources that fill many cells at once

These files are already in the repository and cover several destinations, so extracting them once is faster than searching destination by destination:

| File | Fills |
|---|---|
| `elena/zurigo/03_imprese/BFS STATENT - sedi e occupati per cantone e settore 2011-2024` | E1 and B3 (NOGA K employment) for all five Swiss cantons |
| `elena/zurigo/07_tasse e residenza/onere fiscale e aliquote (ESTV)` (all cantonal capitals) | T1 and T2 for all five Swiss cantons with the same reference case |
| `elena/zurigo/02_banche e piazza finanziaria/Sportelli bancari per cantone 1987-2025 (BNS bastdagsua).xlsx` | B2 for all five Swiss cantons from one SNB table (solves the open point in the data README) |
| `elena/singapore/05_stabilità e istituzioni/World Bank WGI` (all countries) | S1 and S2 for Monaco, Singapore, Luxembourg, London and Milan |
| `elena/zurigo/04_occupazione/occupati e salari` (LSE 2024 by region) | L3 for the Swiss destinations (by large region, not canton) |

## Notes on the check

- Nicole's material is a Word report: only the values in its summary tables were counted; the text sections mostly list what remains to be collected.
- For Elena's destinations the files are raw sources: 📁 means the source is there, not that the value has been checked.
- Graubünden's workbook has most values under "General / source context"; they were counted under the matching topic.
- The status reflects the files on `main` on 19 October 2026.
