# Come leggere la raccolta

[Pagina iniziale](../README.md) · [Dati](../data/README.md) · [PDF](../reports/README.md)

## Scegli il formato

- **PDF:** report, normativa e note metodologiche originali. Aprili dal catalogo PDF; servono per leggere il contesto e citare le fonti.
- **Excel:** tabelle già navigabili in fogli, senza elaborazioni aggiunte. Parti da questi per esplorare i dati.
- **CSV:** esportazioni delle tabelle BFS, una per anno. Importale con separatore virgola e codifica Windows-1252.
- **ZIP:** archivi originali USTAT con CSV e un file di informazioni. Estrai entrambi e leggi le informazioni prima dell’analisi.

## Cosa è stato selezionato nei CSV

| Serie | Selezione |
|---|---|
| Popolazione per cantone | Tutti i cantoni, tipi di popolazione, cittadinanze e sessi; paese di nascita aggregato |
| Migrazioni | Svizzera e cantoni; distretti e comuni esclusi; tutte le cittadinanze, i sessi e i tipi di migrazione disponibili |
| Domicilio un anno prima | Svizzera e cantoni; età aggregata; categorie di domicilio, cittadinanza, popolazione e sesso disponibili |
| Offerta ospedaliera | Tutte le categorie territoriali, unità di osservazione e tipologie di struttura disponibili |

Le selezioni precise e i metadati originali sono in [data/metadata](../data/metadata). Le definizioni degli indicatori BAG sono nel [PDF dedicato](../reports/sanita/bag_ospedali_svizzeri_2024_definizioni_it.pdf).

## Prima di confrontare i valori

1. Allinea l’anno di riferimento: l’edizione di un report e l’anno dei dati possono essere diversi.
2. Usa lo stesso territorio e la stessa unità di misura.
3. Non sommare totali e sottocategorie: nei CSV possono comparire entrambi.
4. Conserva i simboli originali per valori mancanti o riservati; non convertirli automaticamente in zero.
5. I dati di popolazione e migrazione non identificano direttamente persone HNWI/UHNWI.

## Cosa non è ancora un dataset

I report fiscali e immobiliari contengono tabelle e analisi, ma non sono stati convertiti in un dataset unico. I calcolatori d’imposta richiedono uno scenario (comune, anno, situazione familiare, reddito e patrimonio). Non sono state prodotte simulazioni.

La tabella BFS sui medici `1404050000_104` non è inclusa: il tentativo di esportazione API ha restituito HTTP 400. Il collegamento di consultazione è riportato nell’indice delle fonti.

## Provenienza e integrità

I nomi e la collocazione dei file sono stati semplificati; i contenuti scaricati non sono stati modificati. [data/sources.json](../data/sources.json) registra URL, data di download, dimensione e SHA-256. Per i file rinominati conserva anche il nome o percorso precedente. Gli anni non riportati nel catalogo non sono stati dedotti dalla data di download.
