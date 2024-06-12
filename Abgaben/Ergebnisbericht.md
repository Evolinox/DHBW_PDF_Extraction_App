# Ergebnisbericht

## Beschreibung

Unsere App ermöglicht es Dozenten, aus Bachelor-Arbeiten die wichtigsten Randinformationen wie Autor, Seitenzahl, Titel und Unternehmen auszulesen. Diese Informationen werden anschließend an ein Natural Language Processing-System weitergegeben, um tiefgehendere Inhalte zu extrahieren. In der App können entweder eine einzelne PDF-Datei oder verschiedene Suchkriterien ausgewählt und an unser Backend übermittelt werden. Die Auswertung von Ordnern funktioniert allerdings aktuell nicht.

Der Text wird im Backend basierend auf den Suchkriterien analysiert, und die Ergebnisse werden im Frontend angezeigt. Dabei kommt es vor, dass das Auslesen der PDF-Dateien teilweise Leerzeichen interpretiert, wo keine sind. Zudem werden je nach Schriftart manchmal Buchstaben nicht richtig erkannt oder ausgelassen, da der Extraktor diese nicht als bekannte Buchstaben identifizieren kann. Das Frontend bietet die Möglichkeit, die Auswertung als CSV-Datei zu exportieren.

## Natural Language Processing

Ein Ziel unserer Software war die Nutzung eines Large Language Models zur Analyse der genutzten Sprache in der Bachelorarbeit. Dafür nutzen wir anfangs `Ollama`, welches allerdings keine zufriedenstellenden Ergebnisse brachte. Deshalb sind wir später auf das `NLTK` (= Natural Language Toolkit) umgestiegen.

Die Nutzung ist einfach zu handhaben, der erste Schritt ist die Installation von `NLTK`. Dies passiert mit dem folgenden Command:

```bash
pip install nltk    # Windows
pip3 install nltk   # macOS
```

## CSV-Exporter

Die CSV-Export Funktion wurde mithilfe des internen Moduls `csv` implementiert. Die Implementierung ist dabei sehr einfach gehalten, so gibt es lediglich eine Methode, welche den kompletten Export regelt:

```python
import csv                          # Importiert das csv Modul

def createCsvFromJson(jsonData)     # Unsere Methode
```

Um eine CSV Tabelle zu erstellen sind erst ein mal die Namen für die Spalten zu definieren. Dies wird mithilfe eines Arrays realisiert:

```python
fieldnames = [
    'Titel',
    'Student',
    'Seitenanzahl',
    'Firma',
    'Matrikelnummer',
    'Adjektive',
    'Nomen',
    'Verben',
    'Adverben',
    'Text'
]
```

Dabei wurde darauf geachtet, dass die Namen einfach lesbar sind. So wurde zum Beispiel `matNr` aus dem JSON Objekt zu `Matrikelnummer` umbenannt.

Nachdem die Spalten definiert sind, müssen nun auch die Einträge für die einzelnen Spalten definiert werden. Auch diese wurden wieder in einem Array definiert:

```python
csvData = [
    {
        'Titel': jsonData['title'],
        'Student': jsonData['student'],
        'Seitenanzahl': jsonData['totalPages'],
        'Firma': jsonData['firma'],
        'Matrikelnummer': jsonData['matNr'],
        'Adjektive': jsonData['totalAdjectives'],
        'Nomen': jsonData['totalNouns'],
        'Adverben': jsonData['totalAdverbs'],
        'Verben': jsonData['totalVerbs'],
        'Text': jsonText
    }
]
```

Das war auch schon der Großteil der Arbeit, nun müssen nur noch die Daten in eine CSV-Datei geschrieben werden. Dafür erstellen wir mit der Methode `open()` eine neue Datei im Nutzerverzeichnis und öffnen diese in der Variable `file`.

```python
with open(Path.home() /  "export.csv", 'w', newline='') as file:
```

Jetzt können wir den `DictWriter` aus dem `csv` Modul laden und in der Variable `writer` speichern. Durch die Variable haben wir nun Zugriff auf die Methode `writeheader()`, welche die Spaltennamen aus dem vorher definierten Array schreibt und die Methode `writerows()`, welche die Einträge in die Datei schreibt.

```python
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(csvData)
```
