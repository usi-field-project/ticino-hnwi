# How to use the collection

[Home](../README.md) · [Data](README.md) · [PDFs](raw/reports/README.md)

## Choose a format

- **PDF:** original reports, legislation and methodological notes. Open them from the PDF catalogue for context and citations.
- **Excel:** source tables organised into worksheets, with no additional analysis. Start here to explore the data.
- **CSV:** BFS table exports, one per year. Import with a comma delimiter and Windows-1252 encoding.
- **ZIP:** original USTAT archives containing a CSV and an information file. Extract both and read the information before analysing the data.

## CSV selections

| Series | Selection |
|---|---|
| Population by canton | All cantons, population types, citizenship categories and sexes; country of birth aggregated |
| Migration | Switzerland and cantons; districts and municipalities excluded; all available citizenship categories, sexes and migration types |
| Residence one year earlier | Switzerland and cantons; age aggregated; available residence, citizenship, population-type and sex categories |
| Hospital provision | All available geographical categories, observation units and facility types |

Exact selections and original metadata are in [data/metadata](metadata). BAG indicator definitions are provided in the [companion PDF](raw/reports/sanita/bag_ospedali_svizzeri_2024_definizioni_it.pdf).

## Before comparing values

1. Align reference years: a report’s edition and its underlying data year may differ.
2. Use consistent geographical coverage and units.
3. Do not add totals to their subcategories: both may appear in the CSV files.
4. Preserve source symbols for missing or confidential values; do not automatically treat them as zero.
5. Population and migration statistics do not directly identify HNWI/UHNWI individuals.

## Resources that are not yet consolidated datasets

Tax and property reports contain tables and analysis, but have not been converted into a single dataset. Tax calculators require a defined scenario: municipality, year, household circumstances, income and wealth. No tax simulations have been produced.

BFS table `1404050000_104` on physicians is not included: the attempted API export returned HTTP 400. Its consultation link is listed in the source directory.

## Provenance and integrity

Downloaded contents are unchanged. Some filenames and locations were simplified. [data/sources.json](sources.json) records URLs, download dates, file sizes and SHA-256 checksums. For previously renamed files it also retains the earlier filename or path. Source datasets, metadata and PDF contents retain their original languages; only the collection documentation and descriptive catalogue fields are translated into English.
