# Benchmark methodology

Status: the sections "Destinations and rationale" and "Reference periods and comparability" are a **proposal for team review**; nothing has been approved yet. The data register that applies these rules is in [03_data](../03_data/README.md).

## Destinations and rationale

### Comparison groups

| Group | Destinations | Role in the analysis |
|---|---|---|
| Baseline | Ticino | Reference territory: every other destination is read relative to Ticino |
| Swiss benchmarks | Zurich, Zug, Geneva, Graubünden | Same federal framework (law, currency, national institutions); differences come from cantonal taxation, economy and location |
| International benchmarks | Monaco, Dubai, Singapore, London, Luxembourg, Milan, Lisbon | Competing wealth destinations and financial hubs with different national regimes |

### Benchmark unit for each destination

The destinations are not the same kind of territory: Ticino and Zug are sub-national cantons, Monaco, Singapore and Luxembourg are whole states, Dubai is an emirate within a federation, Milan, London and Lisbon are cities inside larger countries. To keep the comparison consistent, each destination has **one benchmark unit**, chosen as the smallest territory that (a) produces its own official statistics and (b) corresponds to where an HNWI would actually choose to live.

| Destination | Benchmark unit | Unit type | Other units that may appear in sources |
|---|---|---|---|
| Ticino | Canton of Ticino | Canton | Lugano (municipality), Switzerland |
| Zurich | Canton of Zurich | Canton | City of Zurich, Switzerland |
| Zug | Canton of Zug | Canton | City of Zug, Switzerland |
| Geneva | Canton of Geneva | Canton | City of Geneva, Switzerland |
| Graubünden | Canton of Graubünden | Canton | Individual municipalities (e.g. Chur, St. Moritz), Switzerland |
| Monaco | Principality of Monaco | City-state | — |
| Singapore | Republic of Singapore | City-state | — |
| Luxembourg | Grand Duchy of Luxembourg | Country | Luxembourg City |
| Dubai | Emirate of Dubai | Emirate | United Arab Emirates |
| London | Greater London | Metropolitan region | City of London, United Kingdom |
| Milan | Metropolitan City of Milan (NUTS 3) | Metropolitan area | Comune di Milano, Lombardy, Italy |
| Lisbon | Grande Lisboa (NUTS 3) | Metropolitan area | Lisbon municipality, Portugal |

For the Swiss destinations the canton is the unit even for Zurich and Geneva, so that they stay comparable with Ticino; city-level data is used only as context.

### Three kinds of indicators

Not every indicator should be measured at the benchmark unit. Each indicator in the [indicator catalogue](../03_data/indicators.csv) has a `scope`:

1. **Local**: describes what happens in the territory (population, banks and branches, companies, employment, property prices, crime, air quality, hospitals, schools). It must be measured at the benchmark unit. A value for a larger or smaller area is a proxy and is graded lower (see below).
2. **Regime**: describes the rules that apply to a resident (income, wealth and inheritance tax, lump-sum taxation, residence permits). It is recorded for the level that sets the rule. In Switzerland the tax burden also depends on the municipality, so each canton uses a **reference municipality** (proposal: Lugano, Zurich, Zug, Geneva, Chur; St. Moritz as a sensitivity case for Graubünden), and the same taxpayer profiles are used everywhere.
3. **National**: only exists at country level (World Bank WGI, rule of law, credit rating of the state, FATF status). Using the national value is correct, but it is the same for all Swiss cantons, so it does not discriminate within the Swiss group.

## Comparison dimensions

This is the proposed collection grid for every destination; the benchmark methodology remains to be completed. The indicators selected for the benchmark table and the scoring are proposed in the [indicator matrix](indicator_matrix.md).

| Topic | Information to collect |
|---|---|
| **Wealth** | International wealth, private wealth and wealth distribution |
| **Banking presence and density** | Number of banks operating in the territory; branch count and density per 100,000 residents and per km², distinguishing banks from branches |
| **Business presence** | Number of companies present in the territory; companies per 1,000 residents and breakdown by sector, distinguishing registered companies from local establishments |
| **Employment** | Employment level and rate, unemployment rate, and employment by sector |
| **Stability and institutions** | Political and institutional stability, rule of law, regulatory predictability and public administration quality |
| **Quality of life** | Safety and crime, cost of living, air pollution, noise, green spaces and access to everyday services |
| **Taxation and relocation** | Income and wealth taxes, lump-sum taxation, inheritance taxes, and residency requirements |
| **Real estate** | Residential and luxury property markets |
| **Population and migration** | Residents, nationality, arrivals and departures; specify the geographical scope |
| **Healthcare** | Hospitals, healthcare provision and historical series |
| **Education** | Education system, international schools and higher education |

## Reference periods and comparability

### What to record for every data point

Every value goes into [03_data/observations.csv](../03_data/observations.csv) with, at minimum:

| Required information | Field(s) |
|---|---|
| Territory covered | `geo_id` (from [geographies.csv](../03_data/geographies.csv)) and `geo_match` |
| Year or period | `period`, `period_type` |
| Unit of measure | `unit`, `currency` |
| Source | `source_publisher`, `source_title`, `source_url`, `access_date`, `local_file` |
| Comparability limits | `comparability`, `comparability_note` |

The full definition of each field is in the [data README](../03_data/README.md).

### Reference period

- **Target year: 2024**, the latest year for which most official annual series are available for all destinations (e.g. BFS STATENT and LSE 2024). Values for 2023 to 2025 count as aligned.
- **Regime indicators** (tax and residence rules) use the rules in force for **tax year 2026**.
- If a destination only has an older value, it is recorded with its real year and graded B or C; it is never relabelled as 2024.
- Keep historical series when available, but the benchmark table uses one value per destination and indicator.

### Comparability grade

| Grade | Meaning | Use in the analysis |
|---|---|---|
| **A** | Benchmark unit (or the correct level for regime and national indicators), same definition as the Ticino value, period aligned | Directly comparable; can be used in scoring |
| **B** | Usable with a caveat: proxy territory (e.g. city instead of canton, country instead of emirate), slightly different definition, or period outside 2023–2025 but not before 2020 | Shown in the benchmark with a note; scoring only if the team agrees |
| **C** | Context only: very different coverage or definition, or before 2020 | Not used in scoring or rankings |

`geo_match` records how the territory of the data relates to the benchmark unit: `exact`, `larger` (e.g. UAE for Dubai), `smaller` (e.g. City of Zurich for the canton) or `national_proxy`. A value with `geo_match` other than `exact` for a local indicator cannot be grade A.

### Ratios, densities and currencies

- Densities (per 100,000 residents, per 1,000 residents, per km²) are **calculated in the analysis**, not copied from different sources, using the population and area of the same territory and year, recorded as observations with the indicators `population` and `area_km2`. State whether the area includes lakes or reclaimed land, because it changes per-km² densities (e.g. Zug, Ticino, Geneva). When a source already publishes a ratio with a different denominator (e.g. branches per 100,000 *adults*), record it as published with its own unit.
- Values are recorded in their **original currency**. Conversion to CHF happens only in the analysis, with one source for exchange rates (proposal: SNB annual averages for the reference year), stated in the report.
- Keep definitions separate: banks vs branches vs credit institutions; enterprises vs local establishments; residents vs adults vs workforce. A different definition is a different indicator, not the same indicator with a note.
