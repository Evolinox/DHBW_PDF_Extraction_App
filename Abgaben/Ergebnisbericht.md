# Ergebnisbericht

Ergebnissbeschreibung:
Unsere App ermöglicht es Dozenten, aus Bachelor-Arbeiten die wichtigsten Randinformationen wie Autor, Seitenzahl, Titel und Unternehmen auszulesen. Diese Informationen werden anschließend an ein Natural Language Processing-System weitergegeben, um tiefgehendere Inhalte zu extrahieren. In der App können entweder eine einzelne PDF-Datei oder verschiedene Suchkriterien ausgewählt und an unser Backend übermittelt werden. Die Auswertung von Ordnern funktioniert allerdings aktuell nicht.

Der Text wird im Backend basierend auf den Suchkriterien analysiert, und die Ergebnisse werden im Frontend angezeigt. Dabei kommt es vor, dass das Auslesen der PDF-Dateien teilweise Leerzeichen interpretiert, wo keine sind. Zudem werden je nach Schriftart manchmal Buchstaben nicht richtig erkannt oder ausgelassen, da der Extraktor diese nicht als bekannte Buchstaben identifizieren kann. Das Frontend bietet die Möglichkeit, die Auswertung als CSV-Datei zu exportieren.

### Ergebnisbericht über das Frontend

Das Frontend unserer App sollte es ermöglichen, zwischen der Analyse eines Ordners oder einer einzelnen PDF zu wählen. Diese Auswahloption wurde erfolgreich implementiert. Beim Upload macht es jedoch derzeit nur Sinn, eine einzelne PDF-Datei hochzuladen, da die Übergabe von mehreren Werten, wie zum Beispiel des Titels, an das Frontend noch nicht korrekt implementiert ist.

Die geplante Filterauswahl mit einem simplen Checkbox-System wurde erfolgreich umgesetzt und an das Backend übergeben. Der Analysieren-Button ist ebenfalls funktionsfähig und löst die Analyse im Backend aus.

Die geplante Result Page kann aktuell nur die Analyse einer einzelnen PDF anzeigen und nicht, wie ursprünglich geplant, die Analyse beliebig vieler PDFs in einem Ordner. Die auf dieser Seite platzierten Buttons zum Download einer CSV-Datei und zum Starten einer neuen Analyse sind funktionsfähig.

Im Allgemeinen ist das Frontend auf das Wesentliche reduziert und intuitiv gestaltet.