from PyPDF2 import PdfReader
#Imports Imaga-analysation
import os
import fitz
import re
from PIL import Image 
import json
folder = "Sample_PDFs"
filelist = os.listdir(folder)#alle Testdateien
reader = PdfReader("Sample_PDFs/" + filelist[0])#Fehler: 3;4;5;6;7;8;9;10;13;14;15;19;20;21;22;23;24;26;27;28;29;30;...
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
meta = reader.metadata
a = 0
imagecounter = 0
location = ""
totalText = ""
#Probedaten:

author = ""


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
    a1 = 0
    while a1 < (number_of_pages-1):
        page=reader.pages[a1]
        print(page.extract_text())
        totalText += str(page.extract_text())
        a1+=1
        #print(len(page.images))
        #imagecounter += page.images
    print(totalText)
#extracting()

def getLocation():  
        global text
        global location  
        global counter
        global pagecounter
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

        site = page.extract_text()
        pagetext = str(site)
        lines = pagetext.splitlines()
        text = ""
        for line in lines:
            if not line.isspace():
                text = text + line + "\n"
        blanktext = text.replace(" ", "")
        getLocation()
        title = text.split("Bachelorarbeit")[0].replace("\n", "").strip()
        
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




def printinfos():
    print(author)
    print(title)
    print(location)

counter = 0
while counter < len(filelist):
    pagecounter = 0
    print(counter)
    print(filelist[counter])
    reader = PdfReader("Sample_PDFs/" + filelist[counter])
    page=reader.pages[0]

    getData()
    printinfos()
    print("")
    counter += 1

# reader = PdfReader("Sample_PDFs/" + filelist[38])
# print(reader.pages[0].extract_text())

#um zusätzlich erste Seite zu drucken


def images():
    
    count = 0
    a=0
    while a < number_of_pages:
        page=reader.pages[a]
        for image_file_object in page.images:
            with open(str(count) + image_file_object.name, "wb") as fp:
                fp.write(image_file_object.data)
                count += 1
        print("At page " + str(a+1) + " we reached " + str(count)+ " Images")
        a+=1

        #Transparentes Bild -> Fehler!!!
    
def imagebyMupdf():
    file = "160907_Bachelorarbeit_Sebastian Sperl.pdf"
    
    # open the file 
    pdf_file = fitz.open(file) 
    total_images = 0
    
    # STEP 3 
    # iterate over PDF pages 
    for page_index in range(len(pdf_file)): 
    
        # get the page itself 
        page2 = pdf_file[page_index] 
        image_list = page2.get_images() 
       
    
        # printing number of images found in this page 
        if image_list: 
            print( 
                f"[+] Found a total of {len(image_list)} images in page {page_index+1}") 
            total_images = total_images + len(image_list)
        else: 
            print("[!] No images found on page", page_index+1) 
        for image_index, img in enumerate(page2.get_images(), start=1): 
    
            # get the XREF of the image 
            xref = img[0] 
    
            # extract the image bytes 
            base_image = pdf_file.extract_image(xref) 
            image_bytes = base_image["image"] 
    
            # get the image extension 
            image_ext = base_image["ext"] 
    print("We have found a total of " + str(total_images) + " images in the file.")


def getJson():
    jsonContent = {
        "title": "SAP ist cool!",
        "student": author,
        "totalPages": number_of_pages,
        "firma": "SIT",
        "gliederung": ["Einleitung", "Was ist SAP?", "Geschichte", "HANA", "UI5", "Meins Meinung"],
        "text": totalText
    }
    bachelorTestJson = json.dumps(jsonContent)