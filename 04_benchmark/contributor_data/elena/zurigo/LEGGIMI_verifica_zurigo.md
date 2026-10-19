# Zurigo – materiale per il benchmark

Ultimo aggiornamento: 17 ottobre 2026. Ticino è il riferimento del confronto.

## Struttura delle cartelle
Cartelle numerate secondo la griglia di benchmark del progetto:

| Cartella | Contenuto principale |
|---|---|
| 01_ricchezza | Henley, Knight Frank, Julius Baer; statistica patrimonio ESTV; statistiche fiscali e patrimonio per comune (zh.ch, città) |
| 02_banche e piazza finanziaria | Sportelli bancari per cantone (BNS); BFS banche (2020, superato); elenchi FINMA; studi Finanzplatz Zürich fino al 2025/26 |
| 03_imprese | Sedi, occupati ed ETP totali, per settore NOGA e per comune 2012-2024 (STATENT, aggiornamento ago 2026: 126.784 sedi e 1.149.866 occupati nel 2024); registro di commercio; trasferimenti di aziende; commercio estero |
| 03_imprese (confronto cantoni) | BFS STATENT sedi e occupati per cantone e settore 2011-2024, tutti i cantoni (CSV convertito + originale .px). 2024: Zurigo 126.784 sedi / 1.149.866 occupati; Ticino 40.590 / 250.618; Svizzera 728.380 / 5.681.021 |
| 04_occupazione | Disoccupazione (2010-2026), salari LSE 2024. Occupati per settore recenti: vedi 03_imprese (STATENT 2012-2024); i file per settore in questa cartella sono 1995-2008 |
| 05_stabilità e istituzioni | WGI World Bank (dato Svizzera), rating S&P/Fitch del cantone, finanze comunali |
| 06_qualità della vita | Aria, sicurezza e criminalità, sondaggio soddisfazione, Mercer, territorio, cultura |
| 07_tasse e residenza | Onere fiscale e aliquote ESTV, imposta su successioni e donazioni ZH, permessi di residenza, contribuenti per tipo d'imposta |
| 08_immobili | Prezzi e compravendite (zh.ch), affitti città, lusso (UBS), Lex Koller |
| 09_popolazione e migrazione | Crescita, struttura per età, stranieri e migrazione, previsioni, rapporto sociale |
| 10_sanità | Ospedali (UFSP), medici (FMH), premi cassa malati 2027, spesa comunale |
| 11_istruzione | Scuole internazionali e private, UZH, QS 2027, spesa comunale |
| 12_accessibilità | Aeroporto di Zurigo (statistiche 2010-2024, report 2026) |
| 99_non usati | Questionari Persuisse vuoti |

I file con codici zh.ch (KTZH_…, KANTON_ZUERICH_…) hanno un nome descrittivo; il codice originale è tra parentesi per risalire alla fonte. Le "spese comunali per abitante" sono indicatori indiretti (non misurano l'offerta di servizi).

## Aggiornamenti scaricati (17 ottobre 2026)

| File | Cartella | Note |
|---|---|---|
| ugz_ogd_air_h1_2023.csv | 06_qualità della vita/aria (città di Zurigo) | Serie completa gen-dic 2023; la serie copre ora 2013-2026 senza buchi |
| Finanzplatz Zürich 2025-2026 | 02_banche e piazza finanziaria/studi piazza finanziaria Zurigo | Sostituisce il 2023/24 come fonte principale |
| Sportelli bancari per cantone 1987-2025 (BNS bastdagsua) | 02_banche e piazza finanziaria | Zurigo: 344 sedi e succursali bancarie nel 2025 (359 nel 2023); Ticino: 155. Sostituisce il file BFS "Banken in der Schweiz" (2020) |
| Indici prezzi immobiliari Svizzera (BNS plimoincha) | 08_immobili/Svizzera (BNS) | Dato nazionale, non cantonale: usarlo solo come contesto |
| EIU Liveability Index 2026 – classifica (sito EIU) + comunicato + articolo IamExpat | 06_qualità della vita/classifiche e mappe | Fonte primaria EIU: Zurigo 5ª (96 punti, -3 posizioni rispetto al 2025), Ginevra 6ª. Punteggio più basso di Zurigo in "cultura e ambiente". Il file Wikipedia serve solo per verificare la serie storica, non per citarla |
| Livello salariale ZH vs resto CH, LSE 2024 | 04_occupazione/occupati e salari | Mediana regione Zurigo 7.502 CHF/mese vs Ticino 5.708 (BFS LSE 2024). Il testo del PDF non è ricercabile (lettere mancanti), ma si legge |
| Salari LSE 2024 – comunicato BFS 25.11.2025 | 04_occupazione/occupati e salari | Fonte primaria: mediana CH 7.024, regione Zurigo 7.502, Ticino 5.708 CHF/mese; anche decile superiore per regione |

## Stato
Cartella **completa**: tutti gli 11 temi della griglia sono coperti e tutti i download in sospeso sono stati fatti (17 ottobre 2026).

## Limiti da segnalare nel report
- **Dati vecchi**, da usare solo come contesto storico:
  - "ZH in cifre" 2003/2004/2006;
  - Reddito e patrimonio 2006;
  - analisi immobiliari 2017-2019;
  - patrimonio medio per comune fino al 2022;
  - statistica fiscale per classe fino al 2020.
- **Mercer Quality of Living**: l’ultima edizione è il 2024; affiancare EIU 2026.
- **WGI**: dato nazionale (Svizzera), non cantonale.
- **Aria città**: mancano 2004-2010 e 2012 (non necessari per il benchmark).
