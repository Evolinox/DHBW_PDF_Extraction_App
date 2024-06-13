import nltk
from nltk.tokenize import word_tokenize

import json

exampleString = "Wer während der Autofahrt über Handy oder Freisprechanlage telefoniert, fährt wie ein angetrunkener Wagenlenker."
clusteredJson = {
    "data": [

    ]
}

def downloadNltkStuff():
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')

def analyzeJson(jsonObject):
    global jsonData
    jsonData = json.loads(jsonObject)
    text = str(jsonData['text']).replace('- ', '')
    analyzeTextWithNltk(text)
    clusterJson()

def analyzeTextWithNltk(text):
    downloadNltkStuff()
    print("------ NLTK started:")
    tokenize = word_tokenize(text)
    posTags = nltk.pos_tag(tokenize)
    print(tokenize)
    print(posTags)
    print("Text successfully tokenized...")
    print("------ Extracted Data:")
    # Get all Adjectives
    countAdjectives = 0
    for item in posTags:
        if (item[1] == "JJ"):
            countAdjectives += 1
    # Get all Nouns
    countNouns = 0
    for item in posTags:
        if (item[1] == "NN" or item[1] == "NNP" or item[1] == "NNS"):
            countNouns += 1
    # Get all Adverbs
    countAdverbs = 0
    for item in posTags:
        if (item[1] == "RB"):
            countAdverbs += 1
    # Get all Verbs
    countVerbs = 0
    for item in posTags:
        if (item[1] == "VB" or item[1] == "VBD"):
            countVerbs += 1
    
    print("Total no. of Adjectives: " + str(countAdjectives))
    print("Total no. of Nouns: " + str(countNouns))
    print("Total no. of Aderbs: " + str(countAdverbs))
    print("Total no. of Verbs: " + str(countVerbs))

    # Dump into json
    global jsonData
    jsonData['totalAdjectives'] = countAdjectives
    jsonData['totalNouns'] = countNouns
    jsonData['totalAdverbs'] = countAdverbs
    jsonData['totalVerbs'] = countVerbs
    jsonData['tokenizedText'] = tokenize

def clusterJson():
    clusteredJson['data'].append(jsonData)

def getClusteredJson():
    return clusteredJson