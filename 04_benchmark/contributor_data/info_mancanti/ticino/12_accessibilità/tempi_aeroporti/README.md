# Travel time from Lugano to the intercontinental hubs

Collected by: Elena · Access date: 22.10.2026 · Status: `to_verify`

Recorded in the data register as `TI-036` (`travel_time_hub_airport`, Q5). See [`03_data/observations.csv`](../../../../../../03_data/observations.csv).

## Method

- **Origin:** Lugano railway station, used as the main centre. Lugano is the reference municipality.
- **Reference date:** Tuesday 3 November 2026, departures in the morning and early afternoon (06:30–14:06). This is the 2026 timetable, which changes on 13 December 2026.
- **Train:** official SBB/TILO timetable, read through the open API [transport.opendata.ch](https://transport.opendata.ch). Times run from station to the airport station, which is at the terminal. The value used is the fastest regular connection.
- **Car:** route estimate from [OSRM](https://project-osrm.org/) on OpenStreetMap data, from Lugano station to the terminal. It assumes free-flowing traffic: no congestion and no queues at the Chiasso border or at the Gotthard tunnel. Real times are often longer.
- **Car route to Malpensa:** the motorway route is used (A2 → Chiasso → A9 → A36, ~78 km, ~65 min), consistent with Google Maps (~80 km). OSRM's shortest route via Stabio–Gaggiolo–Varese is ~67 km and ~63 min, but runs largely on ordinary roads.

## Results

| Hub | Train (fastest) | Train: connections | Car (estimate, no traffic) | Distance by road |
|---|---|---|---|---|
| **Milan Malpensa (MXP), T1** | **1 h 35 min** | Direct TILO S10 every hour, no transfers | ~1 h 05 min | ~78 km (motorway via Chiasso) |
| Milan Malpensa (MXP), T2 | 1 h 41 min | Same train | – | – |
| **Zurich Airport (ZRH)** | **2 h 09 min** | 2 per hour, 1 transfer (IC 2 + IC 5 via Zurich HB) | ~2 h 46 min | ~220 km |

**Value used for Q5:** 95 min by train to Malpensa, because Malpensa is the nearest intercontinental hub (`TI-036`, grade A). The Zurich figures and the car estimates are context only. They are not in the register, so that the indicator keeps a single mode and a single hub.

## Implications for the benchmark

- Malpensa has a direct hourly train from Lugano with no transfers. That is good, but the airport is in Italy and serves 231 direct international destinations (`TI-028`).
- Zurich is a little over 2 hours away by train. It is the Swiss hub with direct long-haul flights operated by Swiss.
- Neither hub is within one hour by public transport. For UHNWIs who fly private, Lugano Airport partly makes up for this (`TI-035`, see [aeroporto_lugano](../aeroporto_lugano/README.md)).

## For the team

- [ ] Agree the **mode** for Q5 for every destination (proposal: public transport, which is easier to verify on official timetables; car as a note).
- [ ] Use the same method for the other destinations: same weekday, main centre as origin, nearest intercontinental hub.
- [ ] Second check (`verified_by`) on the SBB online timetable.

## Files

| File | Content |
|---|---|
| [lugano_hub_train_connections_2026-11-03.csv](lugano_hub_train_connections_2026-11-03.csv) | All connections retrieved (Lugano → MXP T1, MXP T2, ZRH) for 3.11.2026 |
