# Ergebnisbericht

## Beschreibung

Unsere App ermöglicht es Dozenten, aus Bachelor-Arbeiten die wichtigsten Randinformationen wie Autor, Seitenzahl, Titel und Unternehmen auszulesen. Diese Informationen werden anschließend an ein Natural Language Processing-System weitergegeben, um tiefgehendere Inhalte zu extrahieren. In der App können entweder eine einzelne PDF-Datei oder verschiedene Suchkriterien ausgewählt und an unser Backend übermittelt werden. Die Auswertung von Ordnern funktioniert allerdings aktuell nicht.

Der Text wird im Backend basierend auf den Suchkriterien analysiert, und die Ergebnisse werden im Frontend angezeigt. Dabei kommt es vor, dass das Auslesen der PDF-Dateien teilweise Leerzeichen interpretiert, wo keine sind. Zudem werden je nach Schriftart manchmal Buchstaben nicht richtig erkannt oder ausgelassen, da der Extraktor diese nicht als bekannte Buchstaben identifizieren kann. Das Frontend bietet die Möglichkeit, die Auswertung als CSV-Datei zu exportieren.

## Natural Language Processing

Ein weiterer Kernpunkt unserer App ist dass die extrahierten Daten aus der PDF mithilfe moderner Technologien analysiert und kategorisiert werden können. Dafür haben wir das Modul `NTLK` (= Natural Language Toolkit) genutzt.

```python
import nltk
from nltk.tokenize import word_tokenize
```

NLTK ist ein leistungsfähiges und flexibles Werkzeug zur Verarbeitung natürlicher Sprache, das uns ermöglicht, den Text einer Bachelorarbeit auf verschiedene Merkmale hin zu untersuchen, einschließlich der Tokenisierung und der Erkennung von Wortarten (POS-Tagging)

### Tokenisierung

```python
text = "Wer während der Autofahrt über Handy oder Freisprechanlage telefoniert, fährt wie ein angetrunkener Wagenlenker."
# Beispieltext von: 
# https://www.schreiben.zentrumlesen.ch/myUploadData/files/schreibberat_idee1104_wiss_formulieren_1_bsp.pdf

tokenize = word_tokenize(text)
```

Ein zentrales Element unserer Analyse war die Tokenisierung, bei der der Text in kleinere Einheiten, sogenannte Tokens, zerlegt wurde. Diese Tokens können Wörter, Satzzeichen oder andere bedeutungstragende Elemente des Textes sein. Durch die Tokenisierung konnten wir die Struktur des Textes besser verstehen und weiterführende Analysen, wie die Häufigkeitsverteilung von Wörtern und die Erkennung von Mustern, durchführen.

Für eine kleine Demonstration haben wir hier einmal den `text` (Quelle: [www.schreiben.zentrumlesen.ch](https://www.schreiben.zentrumlesen.ch/myUploadData/files/schreibberat_idee1104_wiss_formulieren_1_bsp.pdf)) mithilfe der Methode `word_tokenize()` tokenisieren lassen. Der Output in der Konsole sieht wie folgt aus:

```bash
>>> print(tokenize)
['Wer', 'während', 'der', 'Autofahrt', 'über', 'Handy', 'oder', 'Freisprechanlage', 'telefoniert', ',', 'fährt', 'wie', 'ein', 'angetrunkener', 'Wagenlenker', '.']
```

### POS Tagging

```python
posTags = nltk.pos_tag(tokenize)
```

Ein weiterer wichtiger Bestandteil unserer Textanalyse war das Part-of-Speech (POS) Tagging. Nachdem wir unseren Text einmal mit `nltk` tokenisiert haben, können wir mit der Methode `pos_tag()` den einzelnen Tokens eine entsprechende Wortart wie zum Beispiel *Nomen* oder *Verb* zuweisen. Der Output mit unserem Beispieltext in der Konsole sieht wie folgt aus:

```bash
>>> print(posTags)
[('Wer', 'NNP'), ('während', 'NN'), ('der', 'NN'), ('Autofahrt', 'NNP'), ('über', 'NNP'), ('Handy', 'NNP'), ('oder', 'NN'), ('Freisprechanlage', 'NNP'), ('telefoniert', 'NN'), (',', ','), ('fährt', 'JJ'), ('wie', 'NN'), ('ein', 'NN'), ('angetrunkener', 'NN'), ('Wagenlenker', 'NNP'), ('.', '.')]
```

Hier kann man zum Beispiel sehen, das `nltk` dem Wort ***Handy*** die Wortart ***NNP*** zugewiesen hat. NNP steht in dem Fall für *Nomen Plural*. Leider ist aber auch `nltk` nicht fehlerfrei, so weist das Modul zum Beispiel auch dem Wort während die Art NN (=Nomen) zu, was nicht richtig ist.

### Rückgabe an den Extractor

Nachdem das POS Tagging abgeschlossen ist, werden die einzelnen Wortarten gezählt und deren Anzahl dem JSON Objekt hinzugefügt und dann an den `extractor` zurückgegeben.

```python
jsonData['totalAdjectives'] = countAdjectives
jsonData['totalNouns'] = countNouns
jsonData['totalAdverbs'] = countAdverbs
jsonData['totalVerbs'] = countVerbs
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
