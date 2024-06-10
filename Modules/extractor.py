from PyPDF2 import PdfReader
import os
import re 
import json
folder = "Sample_PDFs"
filelist = os.listdir(folder)#alle Testdateien
reader = PdfReader("Sample_PDFs/" + filelist[0])#Ausgewählte Datei
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
meta = reader.metadata
a = 0
imagecounter = 0
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

def Metadata():

    # All of the following could be None!
    print("Author = " +meta.author)
    print("creator = " + meta.creator)
    print("producer =" + meta.producer)
    print("subject = "+meta.subject)
    print("title = " +meta.title)
    print("Seitenzahl = " + str(number_of_pages))
    print("Text: ")
#Metadata()
def extracting():
    global totalText
    global pages
    a1 = 0
    while a1 < (number_of_pages-1):
        page=reader.pages[a1]
        #print(page.extract_text())
        totalText += str(page.extract_text())
        a1+=1
        pages += str(page.extract_text())


def getLocation(pagecounter):  
        global text
        global location  
        global counter
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

        

def getData():
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

# def Immagecount(page):
#     print(page)
#     print("blubber")

# def Listofillustrations():
#     global pages
#     global listOfIllustrations
#     for page in pages:
#         if "Abbildungsverzeichnis" in page.remove(" ", ""):
#             if listOfIllustrations == True:
#                 Immagecount(page)
#                 break
#             listOfIllustrations = True



# Listofillustrations()

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
    print(company)



def printinfos():
    print("author: " + author)
    print("title: " + title)
    print("location: " + location)
    print("Matnr: " + matNr)
    print("")

counter = 0
# while counter < len(filelist):
#     pagecounter = 0
#     print(counter)
#     print(filelist[counter])
#     reader = PdfReader("Sample_PDFs/" + filelist[counter])
#     page=reader.pages[0]
#     getData()
#     getTitle()
#     getCompany()
#     try:
#         getMatNr()
#     except: 
#         pass
#     printinfos()
#     counter += 1

# read = PdfReader("Sample_PDFs/" + filelist[20])
# print(read.pages[0].extract_text())
#print(read.pages[30].extract_text())
#print(read.pages[2].extract_text())
#print(read.pages[3].extract_text())

#um zusätzlich erste Seite zu drucken


def getJson():
    jsonContent = {
        "title": title,
        "student": author,
        "totalPages": number_of_pages,
        "firma": company,
        "matNr": matNr,
        "text": totalText
    }
    bachelorTestJson = json.dumps(jsonContent)
    return bachelorTestJson

def runExtraction(arg):  
    extracting()
    getData()
    getTitle()
    getCompany()
    try:
        getMatNr()
    except:
        pass
    return getJson()
