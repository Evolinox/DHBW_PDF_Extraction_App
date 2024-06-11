import ollama
import json

clusteredJson = {
    "data": [

    ]
}

def analyzeJson(jsonObject):
    global jsonData
    jsonData = json.loads(jsonObject)
    clusterJson()


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
    print(clusteredJson)

def getClusteredJson():
    return clusteredJson