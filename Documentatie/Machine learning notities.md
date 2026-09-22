# Machine Learning notities

## Algoritmes die we kunnen gebruiken

| Algoritme | Type| Hoe het werkt | Voordelen | 
| --- |--- | --- | --- | 
| PPO/SAC | Reinforcement Learning | Bepaalt de exacte laad of ontlaadstroom op basis van sensorwaarden | Past zich aan op aanbod van zonnepanelen |
| DQN | Reinforcement Learning | Schakelt tussen vaste standen, bijv. Laden, rust, ontladen etc. | Eenvoudiger te trainen |
| Data-Driven MPC | Model predictive control | Gebruikt het bestaande SOC (?) en corrigeert het sturen van de batterij met sensordata | Garanteert veilige spanning- en temperatuurgrenzen |
| Fuzzy Neural Network | Hybride AI | Combineert menselijke regels zoals bijv. "SOC > 80% en zon hoog, verlaag stroom" met lerende gewichten | Heel snel om uit te voeren op lichte hardware | 

## Welke type Machine learning gaan we gebruiken
Wij gaan bij deze project werken met Reinforcement Learning, waarbij de programma een prijs krijgt voor een goede keuze en gestraft wordt voor en foute keuze.

Deze model gaat getraind worden in een Reinforcement Learning environment met de data over weer, temperatuur, stroom etc. 