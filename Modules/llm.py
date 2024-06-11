import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import ollama
import json

stop_words = set(stopwords.words("german"))

clusteredJson = {
    "data": [

    ]
}

def analyzeJson(jsonObject):
    global jsonData
    jsonData = json.loads(jsonObject)
    #print(getWordFrequency(jsonObject))
    clusterJson()
    #analyzeTextWithNltk(jsonData['text'])

def analyzeTextWithNltk(text):
    print("------ NLTK started")
    print(nltk.pos_tag(word_tokenize(text)))

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