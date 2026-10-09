# Machine Learning notities

## Algoritmes die we kunnen gebruiken

| Algoritme | Type| Hoe het werkt | Voordelen | 
| --- |--- | --- | --- | 
| PPO/SAC | Reinforcement Learning | Bepaalt de exacte laad of ontlaadstroom op basis van sensorwaarden | Past zich aan op aanbod van zonnepanelen |
| DQN | Reinforcement Learning | Schakelt tussen vaste standen, bijv. Laden, rust, ontladen etc. | Eenvoudiger te trainen |
| Data-Driven MPC | Model predictive control | Gebruikt het bestaande SOC (?) en corrigeert het sturen van de batterij met sensordata | Garanteert veilige spanning- en temperatuurgrenzen |
| Fuzzy Neural Network | Hybride AI | Combineert menselijke regels zoals bijv. "SOC > 80% en zon hoog, verlaag stroom" met lerende gewichten | Heel snel om uit te voeren op lichte hardware | 

## Welke type Machine learning gaan we gebruiken
Wij gaan voor **DQN** (Deep Q-Network) uit de vergelijkstabel hierboven. DQN schakelt tussen vaste standen (laden / rust / ontladen), is eenvoudiger te trainen dan PPO/SAC met continue stroomwaarden en past goed bij een systeem dat via een relais laadcutting doet.

Als baseline nemen we een **vaste ruleset** (`limits.py`): de laadgrenzen mét hysterese, zonder instelling.

De DQN wordt getraind in een Reinforcement Learning environment (twin) met de data over weer, temperatuur, stroom etc. En wordt daarna vergeleken met de vaste ruleset.

**Doel van het systeem (beloningsfunctie):** zonne-energie eigenverbruik maximaliseren — het aandeel zonne-energie dat echt benut wordt (opladen of direct gebruik) — en verspillen van zonne-energie bestraffen.

**Veiligheid** blijft een aparte, vaste laag die nooit geleerd wordt: alle acties (ruleset én DQN) gaan door dezelfde grenzen heen. De pompenbediening komt nog; voor nu regelt de vaste layer alleen de lithium-ion batterij.

### Plan
1. **Vaste ruleset** (`limits.py`) als baseline: vaste laadgrenzen + hysterese.
2. **Twin/environment** bouwen, DQN trainen en evalueren.
3. **Vergelijking** DQN vs. vaste ruleset op dezelfde data; evalueren op eigenverbruik.

## Changelog

| Versie | Datum | Wijziging |
|--------|-------|-----------|
| v0.1 | 2026-09-17 | Notitie aangemaakt (eerste versie met algoritmetabel en eerste conclusie "Reinforcement Learning"). |
| v0.2 | 2026-10-08 | Conclusie aangescherpt: vast voor DQN gekozen (de oude was alleen "Reinforcement Learning"), met vaste ruleset (`limits.py`) als baseline. Plan toegevoegd, doel van het systeem toegevoegd (eigenverbruik maximaliseren, zonne-energie verspilling bestraffen). De fixed ruleset is dus `limits.py` (dat wordt met dezelfde code geregeld). |