from PyPDF2 import PdfReader
import os
import re 
import json
import Modules.llm as llm
#n = 0
#folder = "Sample_PDFs"

#changepath
#path = "C:\Users\nairo\Desktop\PDF working\Sample_PDFs"
#os.chdir(path)
reader = ""
filename = ""

#filelist = os.listdir(folder)#alle Testdateien
#folder = "C:/Users/nairo/Desktop/rezepte/fezu"
#filelist=os.listdir("C:/Users/nairo/Desktop/rezepte/fezu")
#reader = PdfReader(folder +"/"+ filelist[n])#Ausgewählte Datei
number_of_pages = 0
#text = page.extract_text()
#meta = reader.metadata
a = 0
location = ""
totalText = ""
title = ""
author = ""
company = ""
matNr = ""
blanktext = ""
illustrations = 0
listOfIllustrations = False
pages = []
result = []

def extracting():
    global totalText
    global pages
    a1 = 0
    while a1 < (number_of_pages-1):
        page=reader.pages[a1]
        totalText += str(page.extract_text())
        a1+=1
        pages += str(page.extract_text())


def getLocation(pagecounter):  
        global text
        global location 
        global page    
        blanktext = text.replace(" ", "")
        if "Lörrach" in blanktext:
            location = "Lörrach"
        elif "Mosbach" in blanktext:
            if "Bad Mergentheim" in blanktext or "MGH" in blanktext:
                location = "Bad Mergentheim"
            else: location = "Mosbach"
        else: 
            location = "unknown"
            page = reader.pages[pagecounter]
            if pagecounter < number_of_pages:
                pagecounter += 1
                getData()

        

def getData(getAuthor):
        global location
        global text
    #for files in filelist:
        global page
        global author
        global title
        global blanktext

        site = page.extract_text()
        pagetext = str(site)
        #print(site)
        lines = pagetext.splitlines()
        text = ""
        for line in lines:
            if not line.isspace():
                text = text + line + "\n"
        blanktext = text.replace(" ", "")
        getLocation(0)
        
        lines = text.splitlines()
        author = ""
        if getAuthor:
            if location == "Mosbach" or location == "Bad Mergentheim":
                for line in lines:
                    if "von" in line.replace(" ", "") and len(line.replace(" ",""))<5: #get Author; funktioniert nur, wenn es eine gewisse Formatierung gibt
                        author = lines[lines.index(line)+1].strip()

                            
                    
            elif location == "Lörrach":
                for line in lines:
                    if "Lörrach" in line.replace(" ", ""):
                        if lines.index(line) + 1 < len(lines):
                            author = lines[lines.index(line)+1].strip()
                        else:
                            specifyed = line.split("Lörrach")[1]
                            match = re.search(r'\d', specifyed)  # Search for the first digit
                            if match:
                                author = specifyed[:match.start()].strip()
            if author == "":
                if "Autor" in text or "Verfasser" in text:
                    for line in lines:
                        if "Autor" in line or "Verfasser" in line:
                            author = line.split(":")[1].strip()                        
                else: author = "unknown"

def getTitle():
    global title
    title = text.split("helor")[0].replace("\n", "").strip()
    title = title.split("HELOR")[0].strip()
    title= title[:-3]
    if "Duale Hochschule Baden" in title: #check, if in Layout, there is the location and the title switched
        title=text.split("helor")[1].replace("\n", "").strip()
        title = title.split("Studienrichtung")[0].strip()
    if len(title) > 300: #annahme: über 300 Zeichen entsprechen einem Fehler
        title = "invalid"

def getMatNr():
    global matNr
    matNr = ""
    if "Matrikelnummer" in blanktext or "Matnr" in blanktext:
        lines = blanktext.splitlines()
        for line in lines:
            if "Matrikelnummer" in line or "Matnr" in line:
                    matNr = re.findall(r"\d{7}", line)[0]#search for 7 following digits

def getCompany():
    global company
    if "firma" in text or "Firma" in text or "Dualer Partner" in text:
        lines = text.splitlines()
        for line in lines:
            if "firma" in line or "Firma" in line or "Dualer Partner" in line:
                if not "Betreuer" in line:
                    if ":" in line:
                        company = line.split(":")[1]
                    elif "irma" in line:
                        company = line.split("irma")[1]
                    elif "Partner" in line:
                        company = line.split("Partner")[1]
    company = company.strip()
    if company == "":
        company = "unknown"




def getJson():
    global bachelorTestJson
    global result
    global extractedJSONData
    jsonContent = {
        "title": title,
        "student": author,
        "totalPages": number_of_pages,
        "firma": company,
        "matNr": matNr,
        "text": totalText
    }
    bachelorTestJson = json.dumps(jsonContent)

def runExtraction(getTitleBool, getAuthorBool, getCompanyBool, getMatnrBool): 
    try: 
        extracting()
    except:
        pass
    try:
        getData(getAuthorBool)
    except:
        pass
    if getTitleBool:
        try:
            getTitle()
        except:
            pass
    if getCompanyBool:
        try:
            getCompany()
        except:
            pass
    if getMatnrBool:
        try:
            getMatNr()
        except:
            pass
    try:
        getJson()
        llm.analyzeJson(bachelorTestJson)
    except:
        pass

    
    #print(author)
    #print(filename)
    #print(bachelorTestJson)


def recieve(isFolder, file, getTitle, getAuthor, getNumberOfPages, getCompany, getMatNr):
    global reader
    global filename
    global page
    global text
    global number_of_pages
    if isFolder != True:
        reader = PdfReader(file)
        filename = file   
        page = reader.pages[0]   
        text = page.extract_text() 
        if getNumberOfPages: 
            number_of_pages = len(reader.pages)
        runExtraction(getTitle, getAuthor, getCompany, getMatNr)
    else:
       filelist=os.listdir(file)
       for document in filelist:
            filename =  file + "/" + document
            reader = PdfReader(filename) 
            page = reader.pages[0]  
            text = page.extract_text() 
            if getNumberOfPages: 
                number_of_pages = len(reader.pages)  
            runExtraction(getTitle, getAuthor, getCompany, getMatNr)
    totalJson = llm.clusterJson
    return totalJson


#recieve(True, "C:/Users/nairo/Desktop/PDF working/Sample_PDFs", True, True, True, True, True)
#recieve(False, "C:/Users/nairo/Desktop/PDF working/Sample_PDFs/Bachelorarbeit Kitzelmann.pdf", True, True, True, True, True)
