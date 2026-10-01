# Product Backlog: Project C Batterij test systeem

| Requirement | User Story | Acceptatiecriteria | Wie |   
| --- | --- | --- | --- |    
| 1. Onze model moet getraind worden op basis van weer data, zoals lucht vochtigheid, regen, licht, temperatuur en de stroom en spanning uit het bron. | Als gebruiker wil ik data voeden aan het model zodat het model de opbrengst van energie efficienter kan maken. | 1. Het systeem moet verschillende beslissingen maken als er verschillende data wordt gevoedt | Jelle/Adam | 
| 2. De data moet via de API van de database opgehaald worden voor het trainen van het model. | Als gebruiker wil ik dat data constant zonder mij invloed wordt opgehaald van de database | 1. De data die op de localhost database staat moet via Teamviewer opgehaald. | Adam | 
| 3. Het model moet op de basis van data zichzelf verder kunnen leren zonder enige user input | Als gebruiker wil ik dat ik niet handmatig het model hoef te trainen. |1. Het model doorloopt het proces van leren zelf 2. Het model haalt zelf de nieuwste training data op van de database | Jelle/Adam |  
| 4. Het systeem moet veilig gemaakt worden met gebruik van encryption | Als gebruiker wil ik dat het systeem veilig is en dat niemand zonder toestemming er in kan | | Abhaypartap |
| 5. Het systeem moet veilig getest kunnen worden in een virtual environment | Als gebruiker wil ik het model veilig kunnen testen zonder het risico op te lopen dat de echte batterij kapot gaat |1. De virtual environment moet een goeie weerspiegeling zijn van het echte systeem | Adam | 
| 6. Het systeem moet een sql injection protectie hebben | Als gebruiker wil ik dat de database goed beveiligd is en dat niemand door middel van de database toegang kan krijgen. | 1. SQL keywords moeten in plekken zoals het login pagina niet beschikbaar zijn. | Abhaypartap/Rio/Fatih
| 7. De login details moeten prive blijven | Als gebruiker wil ik dat de login details in een .env bestand niet publiek worden gemaakt en goed beschermd zijn | 1. .env bestand moet niet gepusht worden naar gitlab 2. De login details moeten uit de . env bestand uitgehaald worden en niet hardcoded zijn in de codee | Abhaypartap/Rio/Fatih
| 8. Er moet een bescherming zijn tegen uitwijkende data uit bijvoorbeeld een kapotte sensor | Als gebruiker wil ik dat de systeem beschermd is tegen uitwijkende data in het geval dat een onderdeel van het systeem faalt en verkeerde data afgeeft | 1. De systeem moet kunnen reageren op uitwijkende



