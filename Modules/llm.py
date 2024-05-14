import ollama

def analyzeJson(jsonObject):
    response = ollama.chat(model='llama2', messages=[
    {
        'role': 'user',
        'content': jsonObject,
    },
    ])
    msgContent = response['message']['content']

    # Debug
    print(msgContent)
    return msgContent

def clusterJson():
    print("blop")