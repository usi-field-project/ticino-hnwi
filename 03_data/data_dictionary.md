# Data dictionary

## Collection

- `raw/`: original datasets and archives; publisher PDFs are in `raw/reports/`.
- `processed/`: future cleaned or derived datasets.
- `metadata/`: original BFS variable definitions and export queries.
- [Data guide](DATA_GUIDE.md): formats, encodings, selections and caveats.
- [Dataset index](README.md): descriptions and coverage of existing datasets.

## sources.csv

One record per downloaded original file, exported from `sources.json`. Paths are relative to the repository root. `sources.json` remains the detailed provenance inventory, including query paths and historical filenames. Refresh the CSV if the inventory changes.

| Field | Meaning |
|---|---|
| source_id | Unique catalogue identifier, retained when adding sources |
| path | Current repository-relative file path |
| title | Source document or dataset title |
| source | Original source page or API |
| url | Download URL |
| downloaded_on | Download date (YYYY-MM-DD) |
| kind | Material type recorded in the inventory |
| period | Reference period as provided by the source |
| encoding | Text encoding, where applicable |
| bytes | Original file size in bytes |
| sha256 | Original file checksum |
| description | Source description |

Empty fields mean information is not specified in the inventory.

## indicators.csv

Header-only template: `indicator_id` is the unique identifier; `name`, `dimension` and `definition` describe the indicator; `unit` specifies its measurement unit; `direction` specifies the preferred direction for scoring; `source_id` references the source catalogue; `geography` and `reference_period` delimit coverage; `notes` records qualifications. Indicators and weights are still to be defined.

## interview_summary.csv

The header-only register in `05_interviews/` contains interview ID, date, participant segment, location, consent status, repository-relative anonymized transcript path, key themes and notes. No interviews are currently recorded.
