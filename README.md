# Progetto UBS

Raccolta di dati e documenti per lo studio dell’attrattività del Ticino e il confronto con altre destinazioni svizzere.

## Contenuto

| Cartella | Contenuto |
|---|---|
| `data/raw/demografia/` | Tabelle Excel e archivi CSV USTAT; esportazioni BFS di popolazione e migrazioni |
| `data/raw/wealth/` | UBS Global Wealth Report e Swiss Banking Barometer |
| `data/raw/fiscalita/` | Pubblicazioni ESTV, KPMG e Deloitte |
| `data/raw/immobiliare/` | UBS Luxury Property Focus e Real Estate Focus |
| `data/raw/sanita/` | Dati ospedalieri BAG e BFS, serie storiche e documentazione |
| `data/raw/istruzione/` | Scuola ticinese in cifre 2025 |
| `data/metadata/` | Metadati e richieste delle esportazioni BFS |

Data di acquisizione: **5 ottobre 2026**. Inventario e collegamenti: [SOURCES.md](SOURCES.md). URL di download e controlli di integrità: [data/sources.json](data/sources.json).

## Utilizzo dei dati

I file originali sono conservati senza modifiche. Gli archivi ZIP USTAT contengono CSV e note metodologiche: estrarli localmente prima dell’analisi. I PDF sono documenti di riferimento, non dataset tabellari già elaborati.

I CSV BFS conservano la codifica Windows-1252 e il separatore virgola del servizio originale. Le esportazioni BFS sono divise per anno; le query JSON documentano tutte le selezioni. Per la popolazione (`0103010000_499`) sono inclusi tutti i cantoni, i tipi di popolazione, le cittadinanze e i sessi, con paese di nascita aggregato. Per la migrazione (`0103010200_121`) sono selezionati Svizzera e cantoni, escludendo distretti e comuni. La tabella sul domicilio un anno prima (`0103030000_225`) include Svizzera e cantoni, con età aggregata. L’offerta ospedaliera (`1404010100_102`) conserva tutte le categorie territoriali, le unità di osservazione e i tipi di struttura disponibili.

Le categorie totali e le relative sottocategorie possono coesistere: non sommarle indiscriminatamente. Conservare le definizioni e i simboli per valori mancanti o riservati della fonte. Gli anni disponibili differiscono tra dataset; verificare l’allineamento temporale prima di effettuare confronti.

## Attribuzione

I materiali di terzi restano soggetti alle condizioni dei rispettivi editori. La licenza del repository non sostituisce quelle delle fonti originali. Citare sempre ente, titolo, periodo di riferimento e URL riportati nell’inventario.
