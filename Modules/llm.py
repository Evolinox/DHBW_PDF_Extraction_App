import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import ollama
import json

stop_words = set(stopwords.words("german"))
test_str = "Bei Gebhardt werden alle Industrie 4.0 Produkte unter dem Namen Galileo IoT zusammengefasst. Darunter fallen Condition Monitoring, Predictive Maintenance, Digitale Zwillinge und generell alle Anwendungsgebiete, die sich mit Datenerhebung oder Auswertung befassen. Kunden bekommen ihre Daten und Auswertungen über eine Online-Plattform bereitgestellt. In diesem Kapitel geht es hauptsächlich um den Aufbau von Galileo Internet of Things (IoT)."

clusteredJson = {
    "data": [

    ]
}

def downloadNltkStuff():
    nltk.download()

def analyzeJson(jsonObject):
    global jsonData
    jsonData = json.loads(jsonObject)
    #print(getWordFrequency(jsonObject))
    clusterJson()
    analyzeTextWithNltk(jsonData['text'])

def analyzeTextWithNltk(text):
    print("------ NLTK started:")
    posTags = nltk.pos_tag(word_tokenize(text))
    print(posTags)
    print("------ Extracted Data:")
    # Get all Nouns
    countNouns = 0
    for item in posTags:
        if (item[1] == "NN"):
            countNouns += 1
    # Get all Verbs
    countVerbs = 0
    for item in posTags:
        if (item[1] == "VB"):
            countVerbs += 1
    
    print("Total no. of Nouns: " + str(countNouns))
    print("Total no. of Verbs: " + str(countVerbs))


def getWordFrequency(jsonObject):
    jsonData = json.loads(jsonObject)

    response = ollama.chat(model='llama2', messages=[
    {
        'role': 'user',
        'content': 'Ich habe eine Bachelorarbeit mit dem folgenden Text: "' + jsonData['text'] + '", kannst du die Worthäufigkeit analysieren?',
    },
    ])
    msgContent = response['message']['content']
    
    return msgContent

def clusterJson():
    clusteredJson['data'].append(jsonData)
    #print(clusteredJson)

def getClusteredJson():
    return clusteredJson

analyzeTextWithNltk(test_str)