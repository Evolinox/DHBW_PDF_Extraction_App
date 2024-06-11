import csv
import json

from pathlib import Path

def createCsvFromJson(jsonData):
    jsonText = str(jsonData['text'])#.replace(" ", "")
    fieldnames = ['Titel', 'Student', 'Seitenanzahl', 'Firma', 'Matrikelnummer', 'Text']
    csvData = [
        {'Titel': jsonData['title'], 'Student': jsonData['student'], 'Seitenanzahl': jsonData['totalPages'], 'Firma': jsonData['firma'], 'Matrikelnummer': jsonData['matNr'], 'Text': jsonText}
    ]

    with open(Path.home() /  "export.csv", 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(csvData)