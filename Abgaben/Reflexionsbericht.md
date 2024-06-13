# Reflexionsbericht unseres Projekts

Unser gewähltes Projekt "Analyse von PDF-DHBW-Praxisarbeiten mit Python-Tools zur Extraktion von Features" hatte das Ziel, eine Python App zuentwickeln, mit welcher Praxisarbeiten analysiert werden können.

## Zeitplanung




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


## Fazit - Learning

- Teilweise schlechte Planung / missverständliche Kommunikation der Interfaces zwischen den Modules, wodurch spätere Anpassungen nötig waren.
- Trotz der teilweise fehlenden Planung konnte das Projekt dennoch erfolgreich beendet werden, ohne große Funktionseinbußen zu haben.
- Das Planen mit neuen Frameworks / Tools birgt die Gefahr, dass beim Umsetzten Fehler und Unklarheiten auftauchen, die man so nicht vorhergesehen hat
- Die Wahl des rochtigen Tools mit ausreichender Dokumentation und genügend Erprobung ist essentiel für den Erfolg des Projektes - Flet hat eine Dokumentation, ist jedoch nicht so viel genutzt wie HTML und Co und hat deshalb nicht soviele User, die das selbe Problem hatten und somit ist es schwieriger die Lösung eines spezifischen Problems zu finden.






### Reflexionsbericht über das Frontend

Das Ziel im Frontend war die Entwicklung eines benutzerfreundlichen Frontends für eine App, die bei der Analyse von Bachelor-Arbeiten unterstützt. Eine Upload-Option für einzelne PDF-Dateien und Ordner wurde implementiert. Während der Upload einer einzelnen PDF-Datei reibungslos funktioniert, ist die Funktion zum Hochladen und Analysieren von Ordnern derzeit nicht funktionsfähig. 

Die geplante Filterauswahl mit einem simplen Checkbox-System wurde erfolgreich umgesetzt und ermöglicht es, spezifische Kriterien für die Analyse auszuwählen. Der Analysieren-Button wurde ebenfalls erfolgreich integriert und stößt zuverlässig den Analyseprozess im Backend an. 

Die Navigation von der Hauptseite zur Result-Seite nach dem Start der Analyse funktioniert einwandfrei, wodurch ein logischer und intuitiver Arbeitsfluss gewährleistet ist. Die Result-Seite rendert die Ergebnisse aus dem Backend dynamisch. Während die Analyse einer einzelnen PDF korrekt angezeigt wird, ist die Anzeige von mehreren Ergebnissen aus einem Ordner noch nicht erfolgreich umgesetzt. 

Die Funktion zum Download der Analyseergebnisse als CSV-Datei ist voll funktionsfähig und bietet eine praktische Option zur weiteren Datenverarbeitung. Der Button zum Starten einer neuen Analyse ermöglicht es den Benutzern, nach Abschluss einer Analyse zur Hauptseite zurückzukehren und eine neue Analyse zu starten.

Zusammenfassend ist das Frontend der App funktional und benutzerfreundlich gestaltet. Die wesentlichen Ziele wurden erreicht, auch wenn die Implementierung der Ordneranalyse noch verbessert integriert werden muss.