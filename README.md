# UBS Ticino HNWI Project

Research materials for studying **Ticino’s attractiveness** and comparing it with other Swiss and international destinations: wealth, banking presence, business presence, employment, stability and institutions, quality of life, taxation, property, population, healthcare and education.

## Research by destination

Research is organised by destination, with **Ticino as the baseline**. Each researcher uses the shared topics below to collect comparable information for their assigned destinations.

| Destination | Researcher | Research sheet |
|---|---|---|
| Zug | Luca | [Open sheet](04_benchmark/zug/README.md) |
| Dubai | Luca | [Open sheet](04_benchmark/dubai/README.md) |
| Lisbon | Luca | [Open sheet](04_benchmark/lisbon/README.md) |
| Zurich | Elena | [Open sheet](04_benchmark/zurich/README.md) |
| Singapore | Elena | [Open sheet](04_benchmark/reference_hubs/singapore/README.md) |
| Monaco | Elena | [Open sheet](04_benchmark/monaco/README.md) |
| Geneva | Nicole | [Open sheet](04_benchmark/geneva/README.md) |
| London | Nicole | [Open sheet](04_benchmark/reference_hubs/london/README.md) |
| Milan | Nicole | [Open sheet](04_benchmark/italy_milan/README.md) |
| Graubünden | Petra | [Open sheet](04_benchmark/graubuenden/README.md) |
| Luxembourg | Petra | [Open sheet](04_benchmark/reference_hubs/luxembourg/README.md) |
| Ticino (baseline) | Petra | [Open sheet](04_benchmark/ticino/README.md) |

The sheets are starting templates: complete each topic with findings, source links, reference periods and geographical coverage. Link to files already stored in `03_data/` instead of duplicating them. Mark missing information explicitly and explain limitations when figures are not directly comparable.

## Shared research topics

This is the proposed collection grid for every destination; the benchmark methodology remains to be completed.

| Topic | Information to collect |
|---|---|
| **Wealth** | International wealth, private wealth and wealth distribution |
| **Banking presence and density** | Number of banks operating in the territory; branch count and density per 100,000 residents and per km², distinguishing banks from branches |
| **Business presence** | Number of companies present in the territory; companies per 1,000 residents and breakdown by sector, distinguishing registered companies from local establishments |
| **Employment** | Employment level and rate, unemployment rate, and employment by sector |
| **Stability and institutions** | Political and institutional stability, rule of law, regulatory predictability and public administration quality |
| **Quality of life** | Safety and crime, cost of living, air pollution, noise, green spaces and access to everyday services |
| **Taxation and relocation** | Income and wealth taxes, lump-sum taxation, inheritance and immigration |
| **Real estate** | Residential and luxury property markets |
| **Population and migration** | Residents, nationality, arrivals and departures; specify the geographical scope |
| **Healthcare** | Hospitals, healthcare provision and historical series |
| **Education** | Education system, international schools and higher education |

## Sources already collected — Switzerland and Ticino

The existing archive mainly supports the Swiss and Ticino research, with some international context. It does not yet provide complete coverage of every destination or topic.

| Topic | Available materials |
|---|---|
| **Wealth** | [UBS, Swiss Banking and BAK reports](03_data/raw/reports/ricchezza/README.md) |
| **Taxation and relocation** | [ESTV, KPMG and Deloitte reports](03_data/raw/reports/fiscalita/README.md) |
| **Real estate** | [Original UBS reports](03_data/raw/reports/immobiliare/README.md) |
| **Population and migration** | [USTAT/BFS tables](03_data/raw/demografia/README.md) · [USTAT guides](03_data/raw/reports/demografia/README.md) |
| **Healthcare** | [BAG/BFS data](03_data/raw/sanita/README.md) · [Reports and definitions](03_data/raw/reports/sanita/README.md) |
| **Education** | [Education in figures](03_data/raw/reports/istruzione/README.md) |

| Looking for… | Open |
|---|---|
| Full reports downloaded from publishers | **[Original PDFs — catalogue of 22 documents](03_data/raw/reports/README.md)** |
| Tables for analysis | **[Excel and CSV data — annotated index](03_data/README.md)** |
| Guidance on formats and selections | [How to use the data](03_data/DATA_GUIDE.md) |
| Publishers and source links | [Original sources](03_data/SOURCES.md) |

**84 original files:** 22 PDFs, 13 Excel workbooks, 47 CSV files and 2 ZIP archives. Downloaded on 5 October 2026.

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
│   ├── dubai/
│   ├── geneva/
│   ├── graubuenden/
│   ├── italy_milan/
│   ├── lisbon/
│   ├── monaco/
│   ├── nordic_contrast/ (existing background folder)
│   ├── reference_hubs/
│   │   ├── london/
│   │   ├── luxembourg/
│   │   └── singapore/
│   ├── ticino/ (baseline)
│   ├── zug/
│   └── zurich/
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
