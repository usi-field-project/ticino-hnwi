# UBS Ticino HNWI Project

Research materials for studying **Ticino’s attractiveness** and comparing it with other Swiss destinations: wealth, banking presence, business presence, employment, stability and institutions, quality of life, taxation, property, population, healthcare and education.

## Start here

| Looking for… | Open |
|---|---|
| Full reports downloaded from publishers | **[Original PDFs — catalogue of 22 documents](03_data/raw/reports/README.md)** |
| Tables for analysis | **[Excel and CSV data — annotated index](03_data/README.md)** |
| Guidance on formats and selections | [How to use the data](03_data/DATA_GUIDE.md) |
| Publishers and source links | [Original sources](03_data/SOURCES.md) |

**84 original files:** 22 PDFs, 13 Excel workbooks, 47 CSV files and 2 ZIP archives. Downloaded on 5 October 2026.

## Browse by topic

| Topic | Contents | Materials |
|---|---|---|
| **Wealth** | International wealth, private wealth and wealth distribution | [UBS, Swiss Banking and BAK reports](03_data/raw/reports/ricchezza/README.md) |
| **Banking presence and density** | Number of banks operating in the territory; branch count and density per 100,000 residents and per km², distinguishing banks from branches | — |
| **Business presence** | Number of companies present in the territory; companies per 1,000 residents and breakdown by sector, distinguishing registered companies from local establishments | — |
| **Employment** | Employment level and rate, unemployment rate, and employment by sector | — |
| **Stability and institutions** | Political and institutional stability, rule of law, regulatory predictability and public administration quality | — |
| **Quality of life** | Safety and crime, cost of living, air pollution, noise, green spaces and access to everyday services | — |
| **Taxation and relocation** | Income and wealth taxes, lump-sum taxation, inheritance and immigration | [ESTV, KPMG and Deloitte reports](03_data/raw/reports/fiscalita/README.md) |
| **Real estate** | Residential and luxury property markets | [Original UBS reports](03_data/raw/reports/immobiliare/README.md) |
| **Population and migration** | Residents, nationality, arrivals and departures, comparisons across cantons | [USTAT/BFS tables](03_data/raw/demografia/README.md) · [USTAT guides](03_data/raw/reports/demografia/README.md) |
| **Healthcare** | Hospitals, healthcare provision and historical series | [BAG/BFS data](03_data/raw/sanita/README.md) · [Reports and definitions](03_data/raw/reports/sanita/README.md) |
| **Education** | Ticino’s education system | [Education in figures](03_data/raw/reports/istruzione/README.md) |

The expanded topics define the planned research scope. A dash in Materials means that supporting materials have yet to be collected; no new datasets or reports have been added for these topics.

## Three starting points

1. For the **broader context**, read the [UBS Global Wealth Report 2026](03_data/raw/reports/ricchezza/ubs_global_wealth_report_2026_en.pdf).
2. For **taxation**, open [KPMG Clarity on Swiss Taxes 2026](03_data/raw/reports/fiscalita/kpmg_clarity_swiss_taxes_2026_en.pdf).
3. To explore **Ticino’s data**, start with [USTAT migration flows](03_data/raw/demografia/ustat_movimenti_migratori.xlsx).

## Structure

```text
├── README.md
├── LICENSE
├── .gitignore
│
├── 01_project_management/
│   ├── development_plan.md
│   ├── timeline.md
│   ├── roles_responsibilities.md
│   └── meeting_notes/
│
├── 02_methodology/
│   ├── research_questions.md
│   ├── segmentation_framework.md
│   ├── benchmark_methodology.md
│   ├── scoring_methodology.md
│   ├── interview_methodology.md
│   └── limitations.md
│
├── 03_data/
│   ├── raw/
│   ├── processed/
│   ├── data_dictionary.md
│   ├── sources.csv
│   └── indicators.csv
│
├── 04_benchmark/
│   ├── cantoni/
│   │   ├── zugo/
│   │   ├── zurigo/
│   │   ├── ginevra/
│   │   ├── grigioni/
│   │   └── ticino/ (base)
│   └── stati_citta/
│       ├── dubai/
│       ├── lisbona/
│       ├── singapore/
│       ├── monaco/
│       ├── londra/
│       ├── milano/
│       └── lussemburgo/
│
├── 05_interviews/
│   ├── interview_guide.md
│   ├── consent_template.md
│   ├── outreach_template.md
│   ├── transcripts/
│   ├── anonymized_transcripts/
│   ├── coding/
│   └── interview_summary.csv
│
├── 06_analysis/
│   ├── segmentation/
│   ├── scoring/
│   ├── sensitivity_analysis/
│   ├── business_case_ubs/
│   └── risks_constraints/
│
├── 07_visualizations/
│   ├── benchmark_heatmaps/
│   ├── segment_charts/
│   ├── interview_charts/
│   ├── business_case/
│   └── roadmap/
│
├── 08_report/
│   ├── drafts/
│   ├── figures/
│   ├── tables/
│   └── final/
│
└── 09_presentation/
    ├── drafts/
    ├── figures/
    └── final/
```

The catalogue describes each PDF’s edition, language and purpose. Original files and source metadata retain their original languages and contents. Sources cover different reference periods; check these before making comparisons. Third-party materials remain subject to their publishers’ terms, which are not replaced by this repository’s licence.

The new planning, methodology and interview documents are templates to complete. Empty working directories contain `.gitkeep` so the structure is retained in Git. Original publisher PDFs are in `03_data/raw/reports/`; `08_report/` is reserved for the project’s own report. The existing repository folder name is unchanged.
