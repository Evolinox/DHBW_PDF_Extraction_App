import ollama
import json

def getLlmSummary(jsonObject):
    jsonData = json.loads(jsonObject)

    response = ollama.chat(model='llama2', messages=[
    {
        'role': 'user',
        'content': 'Ich habe eine Bachelorarbeit mit dem folgenden Titel: "' + jsonData['title'] + '", um was könnte es sich in dieser Bachelorarbeit handeln?',
    },
    ])
    msgContent = response['message']['content']

    return msgContent

def getChapters(jsonObject):
    jsonData = json.loads(jsonObject)

    response = ollama.chat(model='llama2', messages=[
    {
        'role': 'user',
        'content': 'Ich habe eine Bachelorarbeit mit dem folgenden Text: "' + jsonData['text'] + '", kannst du das Inhaltverzeichnis aus dem Text herausarbeiten?',
    },
    ])
    msgContent = response['message']['content']
    
    return msgContent

def clusterJson():
    print("blop")