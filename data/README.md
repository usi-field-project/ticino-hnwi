# Dati per l’analisi

**62 file originali**: 13 Excel, 47 CSV annuali e 2 archivi ZIP. Le 47 annualità sono raggruppate in quattro serie.

[Pagina iniziale](../README.md) · [PDF originali](../reports/README.md) · [Guida di lettura](../docs/GUIDA_DATI.md)

## Da quali file partire

- **Migrazioni in Ticino:** [Excel USTAT](raw/demografia/ustat_movimenti_migratori.xlsx).
- **Confronto migratorio tra cantoni:** [CSV BFS 2025](raw/demografia/bfs_migrazioni_per_cantone/2025.csv).
- **Popolazione per cantone e cittadinanza:** [CSV BFS 2025](raw/demografia/bfs_popolazione_per_cantone/2025.csv).
- **Offerta sanitaria:** [Excel BAG 2024](raw/sanita/bag_ospedali_indicatori_2024.xlsx), da leggere con le [definizioni degli indicatori](../reports/sanita/bag_ospedali_svizzeri_2024_definizioni_it.pdf).

## Popolazione e migrazioni

| Dati da aprire | Periodo | Formato | Contenuto |
|---|---|---|---|
| [BFS — Domicilio un anno prima](raw/demografia/bfs_domicilio_anno_precedente) | 2025 | CSV annuali | Mobilità residenziale: confronto del domicilio attuale con quello precedente. Età aggregata. |
| [BFS — Migrazioni per cantone](raw/demografia/bfs_migrazioni_per_cantone) | 2011–2025 | CSV annuali | Flussi migratori per cantone, cittadinanza, sesso e tipo di migrazione. |
| [BFS — Popolazione per cantone e cittadinanza](raw/demografia/bfs_popolazione_per_cantone) | 2010–2025 | CSV annuali | Confronto tra tutti i cantoni; popolazione permanente e non permanente, cittadinanza e sesso. Paese di nascita aggregato. |
| [USTAT — Bilancio demografico per comune e distretto](raw/demografia/cubi_STATPOP_01_csv.zip) | Dal 1981; versione 20.08.2026 | ZIP di CSV | Bilancio demografico per sesso e nazionalità, con dettaglio comunale e distrettuale. |
| [USTAT — Bilancio demografico per età](raw/demografia/cubi_STATPOP_02_csv.zip) | Dal 1981; versione 20.08.2026 | ZIP di CSV | Bilancio demografico cantonale per sesso, età e nazionalità. |
| [USTAT — Acquisizioni della nazionalità svizzera](raw/demografia/ustat_acquisizioni_cittadinanza.xlsx) | 1991–2025 | Excel | Serie delle acquisizioni di cittadinanza. |
| [USTAT — Bilancio demografico](raw/demografia/ustat_bilancio_demografico.xlsx) | 1991–2025 | Excel | Componenti della variazione della popolazione. |
| [USTAT — Economie domestiche per dimensione](raw/demografia/ustat_economie_domestiche_dimensione.xlsx) | 2010–2025 | Excel | Numero e dimensione delle economie domestiche. |
| [USTAT — Movimenti migratori](raw/demografia/ustat_movimenti_migratori.xlsx) | 1991–2025 | Excel | Arrivi, partenze e dinamica migratoria. |
| [USTAT — Movimento naturale e stato civile](raw/demografia/ustat_nascite_decessi_matrimoni_divorzi.xlsx) | 2008–2025 | Excel | Nascite, decessi, saldo naturale, matrimoni e divorzi. |
| [USTAT — Nazionalità e statuto di residenza](raw/demografia/ustat_nazionalita_statuto_residenza.xlsx) | 2002–2025 | Excel | Composizione della popolazione per nazionalità e statuto. |
| [USTAT — Popolazione a fine e metà anno](raw/demografia/ustat_popolazione_fine_meta_anno.xlsx) | 2003–2025 | Excel | Base demografica per confronti temporali e indicatori pro capite. |
| [USTAT — Popolazione per nazionalità e sesso](raw/demografia/ustat_popolazione_nazionalita_sesso.xlsx) | 2003–2025 | Excel | Residenti svizzeri e stranieri, distinti per sesso. |
| [USTAT — Popolazione per classe di età](raw/demografia/ustat_popolazione_per_eta.xlsx) | 2003–2025 | Excel | Dimensione e struttura per età della popolazione. |
| [USTAT — Residenti nelle economie domestiche](raw/demografia/ustat_residenti_economie_domestiche.xlsx) | Dal 2010; dettaglio nel file | Excel | Numero di residenti per dimensione dell’economia domestica. |

## Sanità

| Dati da aprire | Periodo | Formato | Contenuto |
|---|---|---|---|
| [BAG — Indicatori degli ospedali svizzeri](raw/sanita/bag_ospedali_indicatori_2024.xlsx) | 2024 | Excel | Dati su struttura, attività, personale e situazione finanziaria degli ospedali. |
| [BAG — Liste ospedaliere cantonali](raw/sanita/bag_ospedali_liste_cantonali_dal_2008.xlsx) | Dal 2008; dettaglio nel file | Excel | Appartenenza degli ospedali alle liste cantonali. |
| [BAG — Serie storica degli ospedali](raw/sanita/bag_ospedali_serie_storica_dal_2008.xlsx) | Dal 2008; dettaglio nel file | Excel | Evoluzione temporale delle cifre chiave ospedaliere. |
| [BFS — Offerta ospedaliera](raw/sanita/bfs_offerta_ospedaliera) | 2010–2024 | CSV annuali | Ospedali, siti, letti e altre misure per cantone/grande regione e tipo di struttura. |
