# Reflexionsbericht unseres Projekts

Unser gewähltes Projekt "Analyse von PDF-DHBW-Praxisarbeiten mit Python-Tools zur Extraktion von Features" hatte das Ziel, eine Python App zuentwickeln, mit welcher Praxisarbeiten analysiert werden können.

## Geplant

Entwicklung einer Python-Anwendung zur Analyse von Bachelorarbeiten aus dem Bereich der Informatik, die folgende Funktionalitäten umfasst:

- Extraktion von Seitenzahlen unter Berücksichtigung spezifischer Abschnitte wie Inhaltsverzeichnis und Quellenangaben.
- Verwendung eines Large Language Models zur Ermittlung der Wortfrequenz, wobei alltägliche und unwichtige Wörter herausgefiltert werden.
- Extraktion relevanter Metadaten wie Autor und Firma vom Deckblatt der Bachelorarbeiten.
- Darstellung der extrahierten Daten in einem Benutzerinterface (UI) mit der Möglichkeit zum Export als CSV-Datei.
- Verwendung der Python-Bibliothek Flet oder Kompilierung mit Pygame für die Bereitstellung als ausführbare Anwendung (.exe).
- Implementierung der Möglichkeit zum Hochladen einzelner PDF-Dateien zur Analyse sowie eines Ordners mit mehreren PDFs, wobei die hochgeladenen Dateien nur temporär für die Verarbeitung gespeichert werden und nach dem Schließen der Anwendung gelöscht werden.

## Ist-Zustand

Teilweise schlechte Planung der Interfaces zwischen den Modules, wodurch spätere Anpassungen nötig waren.
