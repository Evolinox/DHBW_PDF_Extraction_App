# PDF Extraction App
Eine App, um Praxisarbeiten der DHBW mithilfe der PyPDF2 und Ollama Libraries zu analysieren und diese Daten in einer CSV Datei zu exportieren

Erstellt im Rahmen der Projektmanagement Vorlesung der DHBW Mosbach mit dem Thema "Analyse von PDF-DHBW-Praxisarbeiten mit Python-Tools zur Extraktion von Features."

## Features
Benutzerinterface für eine einfache Benutzung   
PDF Import  
CSV Export    

## Setup
> [!IMPORTANT]
> Die App benötigt ein paar Bibliotheken, diese müssen vorher mit pip installiert werden.

```bash
pip install flet
pip install PyPDF2
pip install PyPDF2[image]
pip install ollama
pip install nltk
```

Um das Programm zu starten, bitte diesen Command ausführen:
```bash
flet run App.py
```