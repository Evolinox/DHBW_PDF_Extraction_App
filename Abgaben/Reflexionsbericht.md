# Reflexionsbericht unseres Projekts

Unser gewähltes Projekt "Analyse von PDF-DHBW-Praxisarbeiten mit Python-Tools zur Extraktion von Features" hatte das Ziel, eine Python App zuentwickeln, mit welcher Praxisarbeiten analysiert werden können.

## Zeitplanung und Arbeitspakete

Unser gesamtes Projekt haben wir in Arbeitspakete aufgeteilt, für welche wir wiederum Zeitschätzungen vorgenommen haben. Für manche Arbeitspakete war diese Schätzung sehr treffend, für andere wiederum haben wir uns, wie wir im Folgenden darstellen wollen, leider verschätzt.
So haben wir gerade bei den Themen Reflexion und Testing unsere geplanten Zeiten perfekt eingehalten. Andere Themen, beispielsweiße das Aufsetzen des Frontends, gingen fast doppelt so schnell wie geplant oder wurden, wie die Datenbank, komplett ausgelassen. 
Wieder andere Arbeitspakete wie beispielsweiße die Schnittstelle zwischen Front und Backend hingegen haben fast dreimal so lange gedauert wie geplant. 
Im Gesamten haben sich diese Fehlschätzungen allerdings größtenteils ausgeglichen und wir haben nahezu perfekt das Gesamtbudget getroffen.
Außerdem haben wir uns bei einigen Arbeitspaketen bereits in der Planung, vor ausreichender Recherche, für Arbeitsansätze festgelegt, ohne ausreichend recherchiert zu haben. So haben wir das Arbeitspaket LLM (Large Language Module) aufgestellt und uns dabei für Ollama entschieden. Stattdessen hat sich in der Umsetzung allerdings gezeigt, dass sich dieses Modell nicht eignet. Aus diesem Grund musste dann von der ursprünglichen Planung abgewichen werden und wir verwendeten ein Native Language Model. 
Darüber hinaus haben wir im Projektverlauf festgestellt, dass uns ein Arbeitspaket zum Austausch fehlte und wir für Gespräche und Kommunikation mehr Zeit hätten einplanen sollen. 


## Geplant - Zieldefinition

Entwicklung einer Python-Anwendung zur Analyse von Bachelorarbeiten aus dem Bereich der Informatik, die folgende Funktionalitäten umfasst:

- Extraktion von Seitenzahlen unter Berücksichtigung spezifischer Abschnitte wie Inhaltsverzeichnis und Quellenangaben.
- Verwendung eines Large Language Models zur Ermittlung der Wortfrequenz, wobei alltägliche und unwichtige Wörter herausgefiltert werden.
- Extraktion relevanter Metadaten wie Autor und Firma vom Deckblatt der Bachelorarbeiten.
- Darstellung der extrahierten Daten in einem Benutzerinterface (UI) mit der Möglichkeit zum Export als CSV-Datei.
- Verwendung der Python-Bibliothek Flet oder Kompilierung mit Pygame für die Bereitstellung als ausführbare Anwendung (.exe).
- Implementierung der Möglichkeit zum Hochladen einzelner PDF-Dateien zur Analyse sowie eines Ordners mit mehreren PDFs, wobei die hochgeladenen Dateien nur temporär für die Verarbeitung gespeichert werden und nach dem Schließen der Anwendung gelöscht werden.

## Ist-Zustand - Zieldefinition erfüllt / nicht erfüllt

- Extraktion von Seitenzahlen war erfolgreich
- Anstelle eines Large Language Models zur Ermittlung der Wortfrequenz wurde ein Native Language Model verwendet.
- Die Extraktion relevanter Metadaten wurde implementiert - Autor, Dualer Partner, Titel der Arbeit und Matrikelnummer des Studenten.
- Darstellung der extrahierten Daten mit Möglichkeit zum Export als CSV-Datei wurde umgestzt, allerdings nur für eine einzelne PDF.
- Die App ist nicht als ausführbare Anwendung (.exe) kompiliert. Sie wird von der IDE gestartet.
- Es gibt die Möglichkeit zum Hochladen einzelner PDF-Dateien oder eines Ordners, wobei die Dateien selbst nicht dauerhaft gespeichert werden, doch das Hochladen eines Ordners führt zu Problemen in der Darstellung auf der Result-Seite. 

## Zieldefinition

Das Ziel des Projekts war die Entwicklung einer Python-Anwendung zur Analyse von Bachelorarbeiten im Bereich der Informatik. Diese Anwendung sollte mehrere zentrale Funktionen bieten. Eine davon war die Extraktion der Seitenzahlen, wobei spezifische Abschnitte wie das Inhaltsverzeichnis und die Quellenangaben besonders berücksichtigt werden sollten. Zudem sollte ein Large Language Model zur Ermittlung der Wortfrequenz eingesetzt werden, das in der Lage ist, alltägliche und unwichtige Wörter herauszufiltern. Ein weiterer wichtiger Aspekt war die Extraktion relevanter Metadaten vom Deckblatt der Bachelorarbeiten, wie zum Beispiel Informationen über den Autor und die beteiligte Firma.

Die extrahierten Daten sollten in einem Benutzerinterface (UI) dargestellt und die Möglichkeit geboten werden, diese als CSV-Datei zu exportieren. Geplant war auch, die Anwendung entweder mit der Python-Bibliothek Flet oder durch Kompilierung mit Pygame als ausführbare Datei (.exe) bereitzustellen. Darüber hinaus sollte die Anwendung die Möglichkeit bieten, sowohl einzelne PDF-Dateien als auch ganze Ordner mit mehreren PDFs hochzuladen, wobei die hochgeladenen Dateien nur temporär für die Verarbeitung gespeichert und nach dem Schließen der Anwendung gelöscht werden sollten.

Der Ist-Zustand des Projekts zeigt, dass die Extraktion der Seitenzahlen erfolgreich umgesetzt wurde. Anstelle des ursprünglich vorgesehenen Large Language Models kam jedoch ein Native Language Model zur Ermittlung der Wortfrequenz zum Einsatz. Die Extraktion der relevanten Metadaten konnte erfolgreich implementiert werden, wobei neben dem Autor auch der Duale Partner, der Titel der Arbeit und die Matrikelnummer des Studenten erfasst wurden. Die Umsetzung des Erkennens von Sperrvermerk und Verzeichnissen war, zeitbedingt, leider nicht mehr möglich.

Die Darstellung der extrahierten Daten und deren Export als CSV-Datei wurden ebenfalls realisiert, jedoch nur für einzelne PDF-Dokumente. Leider wurde die Anwendung nicht als ausführbare Datei (.exe) kompiliert, sondern muss über die IDE gestartet werden. Die Möglichkeit, sowohl einzelne PDF-Dateien als auch Ordner hochzuladen, wurde implementiert. Dabei stellte sich jedoch heraus, dass das Hochladen eines ganzen Ordners zu Problemen in der Darstellung auf der Ergebnisseite führt.

## Fazit - Learning

Unser kürzlich abgeschlossenes Projekt war in vielerlei Hinsicht eine lehrreiche Erfahrung. Einer der Hauptpunkte war die teilweise unzureichende Planung und die missverständliche Kommunikation zwischen den Modulen. Dies führte dazu, dass im späteren Verlauf Anpassungen notwendig wurden, die bei einer klareren Anfangsphase vermeidbar gewesen wären.

Ein weiterer wichtiger Aspekt war die Arbeit mit neuen Frameworks und Tools. Es hat sich gezeigt, dass das Planen mit solchen neuen Technologien das Risiko birgt, dass unerwartete Fehler und Unklarheiten auftreten. Diese waren im Vorfeld oft nicht absehbar, was den Projektverlauf zusätzlich erschwert hat.

Die Wahl der richtigen Tools spielt eine entscheidende Rolle für den Projekterfolg. Unsere Erfahrung mit dem Tool Flet, das zwar eine Dokumentation bietet, aber nicht so weit verbreitet ist wie HTML und ähnliche Technologien, hat gezeigt, dass die begrenzte Anzahl von Nutzern und der daraus resultierende Mangel an verfügbaren Lösungen für spezifische Probleme eine große Herausforderung darstellen kann.

Auch die Definition der einzelnen Arbeitspakete hätte präziser sein können. Eine klarere Ausformulierung der Aufgaben und der erwarteten Ergebnisse hätte das Erreichen der Projektziele erleichtert und die Zusammenarbeit effizienter gestaltet.

Trotz dieser Herausforderungen konnten wir das Projekt dennoch erfolgreich abschließen, ohne wesentliche Funktionseinbußen hinnehmen zu müssen. 

Zusammenfassend lässt sich sagen, dass klare Kommunikation, präzise Planung und die sorgfältige Auswahl der Tools und Technologien essentiell sind, um den Erfolg eines Projektes sicherzustellen. Diese Erkenntnisse werden uns in zukünftigen Projekten helfen, effizienter und zielgerichteter zu arbeiten.





### Reflexionsbericht über das Frontend

Das Ziel im Frontend war die Entwicklung eines benutzerfreundlichen Frontends für eine App, die bei der Analyse von Bachelor-Arbeiten unterstützt. Eine Upload-Option für einzelne PDF-Dateien und Ordner wurde implementiert. Während der Upload einer einzelnen PDF-Datei reibungslos funktioniert, ist die Funktion zum Hochladen und Analysieren von Ordnern derzeit nicht funktionsfähig. 

Die geplante Filterauswahl mit einem simplen Checkbox-System wurde erfolgreich umgesetzt und ermöglicht es, spezifische Kriterien für die Analyse auszuwählen. Der Analysieren-Button wurde ebenfalls erfolgreich integriert und stößt zuverlässig den Analyseprozess im Backend an. 

Die Navigation von der Hauptseite zur Result-Seite nach dem Start der Analyse funktioniert einwandfrei, wodurch ein logischer und intuitiver Arbeitsfluss gewährleistet ist. Die Result-Seite rendert die Ergebnisse aus dem Backend dynamisch. Während die Analyse einer einzelnen PDF korrekt angezeigt wird, ist die Anzeige von mehreren Ergebnissen aus einem Ordner noch nicht erfolgreich umgesetzt. 

Die Funktion zum Download der Analyseergebnisse als CSV-Datei ist voll funktionsfähig und bietet eine praktische Option zur weiteren Datenverarbeitung. Der Button zum Starten einer neuen Analyse ermöglicht es den Benutzern, nach Abschluss einer Analyse zur Hauptseite zurückzukehren und eine neue Analyse zu starten.

Zusammenfassend ist das Frontend der App funktional und benutzerfreundlich gestaltet. Die wesentlichen Ziele wurden erreicht, auch wenn die Implementierung der Ordneranalyse noch verbessert integriert werden muss.
