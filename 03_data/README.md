# Benchmark data register

Status: **proposal for team review**. The rows in `observations.csv` marked `example` come from the contributor files in [04_benchmark/contributor_data](../04_benchmark/contributor_data/) and show how to fill the register; they still need verification.

The rules behind this register (benchmark unit, reference year, comparability grades) are in [benchmark_methodology.md](../02_methodology/benchmark_methodology.md#reference-periods-and-comparability).

## Files

| File | Content | Who edits it |
|---|---|---|
| [geographies.csv](geographies.csv) | Every territory that can appear in a source, with its level and whether it is the benchmark unit of its destination | Add a row when a source uses a new territory |
| [indicators.csv](indicators.csv) | Catalogue of indicators: definition, unit, scope (local, regime, national), direction | Add a row before recording a new indicator; agree changes as a team |
| [observations.csv](observations.csv) | One row per value: territory, period, unit, source, comparability | Each researcher adds their own values |
| [validate_register.py](validate_register.py) | Checks required fields and comparability rules | Run before every commit: `python 03_data/validate_register.py` |

Each researcher can keep working in their own folder or workbook; values that will be used in the benchmark are copied into `observations.csv`, one row per value.

## Fields of `observations.csv`

| Field | Required | What to write | Example |
|---|---|---|---|
| `obs_id` | yes | Unique id: destination code + number | `TI-001` |
| `topic` | yes | Topic of the shared grid | `Banking presence and density` |
| `indicator_id` | yes | Id from `indicators.csv` | `bank_offices` |
| `source_indicator_label` | no | Name of the indicator in the source, in the original language | `Sedi bancarie totali` |
| `geo_id` | yes | **Territory actually covered by the data** (from `geographies.csv`), not the destination | `AE` for a UAE value used for Dubai |
| `geo_match` | yes | Relation to the benchmark unit: `exact`, `larger`, `smaller`, `national_proxy` | `larger` |
| `value` | yes | Plain number, dot as decimal separator, no thousands separators; `yes`/`no` for yes/no indicators | `135018` |
| `unit` | yes | Unit as published | `count`, `%`, `persons`, `per 100k adults` |
| `currency` | if monetary | ISO code of the original currency; do not convert | `CHF`, `EUR`, `AED` |
| `period` | yes | `2024`, `2024-09` (month), `2024-Q3` (quarter) or `2023/2024` (fiscal or school year) | `2025` |
| `period_type` | no | `year_end`, `annual_average`, `month_end`, `fiscal_year`, `rules_in_force` | `year_end` |
| `source_publisher` | yes | Institution that produced the data (not the website that republished it) | `Swiss National Bank (SNB)` |
| `source_title` | yes | Title of the table, report or dataset, with the table or cube number | `Banken in der Schweiz 2025, Geschäftsstellen` |
| `source_url` | recommended | Direct link to the table or report | |
| `access_date` | recommended | Date the value was read, `YYYY-MM-DD` | `2026-10-17` |
| `local_file` | recommended | Path in the repository of the downloaded file | `04_benchmark/contributor_data/...` |
| `comparability` | yes | `A`, `B` or `C` (see methodology) | `B` |
| `comparability_note` | if B or C | Why the value is not fully comparable | `National value, adult denominator` |
| `collected_by` | yes | Who recorded the value | `Elena` |
| `verified_by` | no | Second team member who checked the value against the source | `Petra` |
| `status` | yes | `draft`, `to_verify`, `verified`, `rejected` (`example` only for the sample rows) | `to_verify` |

## Codes in `geographies.csv`

Swiss cantons use the official two-letter codes (`TI`, `ZH`, `ZG`, `GE`, `GR`); countries use ISO codes (`CH`, `AE`, `GB`, `IT`, `PT`); sub-units add a suffix (`TI-LUG`, `AE-DXB`, `PT-GL`). If a source covers a territory not listed, add a row rather than choosing the closest existing one.

## Practical rules

- **Record what the source says.** If the source covers the UAE, the row says `AE`, even if it is used for Dubai.
- **Do not calculate ratios in this file.** Densities per resident or per km² are computed in the analysis from `population` and `area_km2` rows of the same territory and year.
- **One definition per indicator.** If a source counts something different (e.g. credit institutions instead of bank offices), use or create a different `indicator_id`.
- **Keep the original currency.** Conversion to CHF is done in the analysis.
- **Second check.** A value becomes `verified` only after a second team member has opened the source and filled `verified_by`.

## Open points found in the example rows

- **SNB bank offices**: Ticino and Zurich (EX-001, EX-002) come from cube `bastdagsua` (parent company perspective), Zug (EX-003) from cube `BSTA@SNB.JAHR_U.STK.GST` (company level). The team should pick one table for all Swiss cantons.
- **Bank offices abroad**: see the warning below.

> [!WARNING]
> **Banking data: three different indicators, not one.**
> Lisbon (EX-009) counts **branches only**, the Swiss cantons count **registered offices plus branches**, Monaco (EX-007) counts **credit institutions**.
> These are three different indicators and **must not be put in the same column** or compared directly in the benchmark table.
