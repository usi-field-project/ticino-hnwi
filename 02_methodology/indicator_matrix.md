# Indicator matrix

Status: **proposal for team review**. The selection, directions and priorities below are not approved yet.

Purpose: for each of the 11 [comparison dimensions](benchmark_methodology.md#comparison-dimensions), select a **small set of genuinely comparable indicators** for the benchmark table and the scoring, instead of using everything that has been collected.

How it fits the data register:

- Raw values are recorded in [`03_data/observations.csv`](../03_data/observations.csv), one row per value, following the [register rules](../03_data/README.md).
- Every `indicator_id` used below is defined in [`03_data/indicators.csv`](../03_data/indicators.csv). Indicators marked **(new)** were added to the catalogue with this matrix.
- Ratios and densities are **calculated in the analysis** from counts and the `population` / `area_km2` of the same territory and year, as required by the [methodology](benchmark_methodology.md#ratios-densities-and-currencies). The column *Calculation* shows how.
- Territories and benchmark units are those in [`03_data/geographies.csv`](../03_data/geographies.csv). Tax cases use the reference municipality listed there.

## How to read the matrix

- **Code**: short label used in tables and charts (W1, B2 …).
- **Direction**: `+` higher is more attractive for HNWIs/UHNWIs; `−` lower is more attractive; `ctx` context only, not scored unless the team agrees a direction (e.g. property prices signal both prestige and cost).
- **Priority**: `core` = needed for every destination; `opt` = used only if coverage is good enough.

## Matrix

| Dimension | Code | Benchmark indicator | Calculation from the register (`indicator_id`) | Dir. | Priority | Comparability notes |
|---|---|---|---|---|---|---|
| **Wealth** | W1 | GDP per capita | `gdp_nominal` (new) ÷ `population` | + | core | Original currency in the register, converted in the analysis; regional GDP is published with a lag |
| | W2 | Millionaires per 1,000 residents | `millionaires` ÷ `population` × 1,000 | + | core | Henley geography often city, not canton; Swiss cantons may need a tax-data proxy (`taxable_wealth_total`, context) |
| | W3 | Resident centi-millionaires | `centimillionaires` | + | opt | Often not published for small territories |
| **Banking presence and density** | B1 | Banks headquartered | `banks_headquartered` | + | core | Do not mix with `credit_institutions` (Monaco) or branches only (Lisbon) |
| | B2 | Bank offices per 100,000 residents | `bank_offices` ÷ `population` × 100,000 | + | core | Align all Swiss cantons on one SNB table first (see open point in the data README); abroad, `bank_branches_per_100k_adults` (national, published) only as grade B/C fallback |
| | B3 | Financial-sector employment share | `financial_sector_employment` (new) ÷ `employment` | + | core | AUM rarely published below country level, so employment is the proxy for the size of the financial centre |
| **Business presence** | E1 | Local establishments per 1,000 residents | `establishments` ÷ `population` × 1,000 | + | core | Establishments ≠ registered companies; letterbox companies inflate `registered_companies` (Zug, Luxembourg) |
| | E2 | New companies per 1,000 residents | `new_companies` (new) ÷ `population` × 1,000 | + | opt | Registration rules differ by country |
| **Employment** | L1 | Employment rate 15–64 | `employment_rate_15_64` (new) | + | core | Use ILO/LFS definition |
| | L2 | Unemployment rate | `unemployment_rate` | − | core | Record ILO rate; SECO registered rate is not comparable abroad |
| | L3 | Median gross monthly wage | `median_wage` | ctx | opt | Signals both prosperity and staff cost |
| **Stability and institutions** | S1 | WGI Rule of Law | `wgi_rule_of_law` | + | core | National: identical for all Swiss destinations |
| | S2 | WGI Political Stability | `wgi_political_stability` | + | core | National, as S1 |
| | S3 | Sovereign credit rating | `sovereign_rating` (new) | + | opt | National; stored as a notch number (AAA = 1, lower is better) |
| | S4 | Basel AML Index | `basel_aml_index` (new) | − | opt | National; not every jurisdiction covered every year |
| **Quality of life** | Q1 | Recorded offences per 1,000 residents | `crime_rate` | − | core | Legal definitions differ: grade B across countries |
| | Q2 | PM2.5 annual mean | `pm25_annual` | − | core | Same station type for all (urban background) |
| | Q3 | Cost of living | `cost_of_living_index` (new) | ctx | opt | Commercial indices: one index and one edition for all |
| | Q4 | Direct international destinations from main airport | `air_destinations_direct` (new) | + | core | Accessibility (see open point 1) |
| | Q5 | Travel time to nearest intercontinental hub | `travel_time_hub_airport` (new) | − | core | Accessibility; fixed origin (main centre) and mode for all |
| **Taxation and relocation** | T1 | Effective income tax, reference case | `income_tax_effective_ref` (new) | − | core | Same synthetic taxpayer in the reference municipality (see open point 2); `top_income_tax_rate` kept as context |
| | T2 | Effective wealth tax, reference case | `wealth_tax_effective_ref` (new) | − | core | 0 where there is no wealth tax |
| | T3 | Inheritance tax for direct descendants | `inheritance_tax_direct` | − | core | Record exemptions in the note |
| | T4 | Special regime for new residents | `lump_sum_taxation` + `lump_sum_min_base` (new) | + | core | Rules in force for tax year 2026; regimes change often |
| | T5 | Investor or financially independent residence route | `investor_residence_route` (new) | + | opt | Yes/no; summarise conditions in the note |
| **Real estate** | R1 | Prime residential price per m² | `prime_price_m2` | ctx | core | Source definition of "prime" differs; `residential_price_m2` as fallback, never mixed in one column |
| | R2 | Prime price change y/y | `prime_price_change_yoy` (new) | ctx | opt | Only main cities covered by international indices |
| | R3 | Restrictions on foreign buyers | `foreign_buyer_restrictions` (new) | − | core | Yes/no (e.g. Lex Koller in Switzerland); detail in the note |
| **Population and migration** | P1 | Resident population | `population` | ctx | core | Denominator for all ratios |
| | P2 | Share of foreign residents | `foreign_residents_share` | ctx | core | Nationality vs foreign-born: state which |
| | P3 | Net international migration per 1,000 residents | `net_international_migration` (new) ÷ `population` × 1,000 | + | opt | Multi-year average recommended; `net_migration` includes domestic moves |
| **Healthcare** | H1 | Practising physicians per 100,000 residents | `physicians` (new) ÷ `population` × 100,000 | + | core | Practising vs licensed |
| | H2 | Hospital beds per 1,000 residents | `hospital_beds` ÷ `population` × 1,000 | + | opt | Private clinics sometimes excluded |
| | H3 | Life expectancy at birth | `life_expectancy` (new) | + | core | Good comparability |
| **Education** | D1 | International schools | `international_schools` | + | core | One list and one radius for all |
| | D2 | Universities in global rankings | `universities_ranked` (new) | + | core | One ranking, one edition, fixed distance |
| | D3 | Tertiary-educated population 25–64 | `tertiary_education_share` (new) | + | opt | Good comparability |

**Total:** 37 benchmark indicators (26 core, 11 optional). They reuse the existing catalogue and add 20 new register indicators.

## Open points for the team

1. **Accessibility**: here it sits under *Quality of life* (Q4–Q5) to keep the 11-topic grid, but some contributor folders already use a separate `12_accessibilità`. Decide whether to make it a 12th dimension (would need updating the destination sheets and the `topic` values).
2. **Reference tax case** for T1–T2: agree income, wealth and family status (proposal: single person, CHF 1m taxable income, CHF 10m net wealth) in the reference municipalities of `geographies.csv`.
3. **`ctx` indicators** (cost of living, wages, property prices, population): leave unscored or score by client segment.
4. **National indicators** (S1–S4) do not differentiate the Swiss destinations: decide whether to give them lower weight in the Swiss-only comparison.
5. **Coverage check**: once values are in `observations.csv`, drop any `opt` indicator missing for more than a few destinations, and any indicator that only reaches grade C.
