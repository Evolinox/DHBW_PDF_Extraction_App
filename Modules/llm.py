import ollama
import json

def analyzeJson(jsonObject):
    jsonData = json.loads(jsonObject)
    response = ollama.chat(model='llama2', messages=[
    {
        'role': 'user',
        'content': 'I have a Text with the following Title: "' + jsonData['title'] + '", What do you think could be the topic of this Text?',
    },
    ])
    msgContent = response['message']['content']

    # Debug
    print(msgContent)
    return msgContent

def clusterJson():
    print("blop")