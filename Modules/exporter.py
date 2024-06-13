import csv
import json

from pathlib import Path

def createCsvFromJson(jsonData):
    fieldnames = ['Titel', 'Student', 'Seitenanzahl', 'Firma', 'Matrikelnummer', 'Adjektive', 'Nomen', 'Verben', 'Adverben', 'Text']

    with open(Path.home() /  "export.csv", 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for pdf in jsonData:
            jsonText = str(pdf['text'])#.replace(" ", "")
            csvData = [
                {
                    'Titel': pdf['title'],
                    'Student': pdf['student'],
                    'Seitenanzahl': pdf['totalPages'],
                    'Firma': pdf['firma'],
                    'Matrikelnummer': pdf['matNr'],
                    'Adjektive': pdf['totalAdjectives'],
                    'Nomen': pdf['totalNouns'],
                    'Adverben': pdf['totalAdverbs'],
                    'Verben': pdf['totalVerbs'],
                    'Text': jsonText
                }
            ]
            writer.writerows(csvData)