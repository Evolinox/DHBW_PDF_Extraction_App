from PyPDF2 import PdfReader
#Imports Imaga-analysation
import os
import fitz 
import io 
from PIL import Image 
from names_dataset import NameDataset #Prüfen, ob Namen
folder = "Sample_PDFs"
filelist = os.listdir(folder)#alle Testdateien
reader = PdfReader("Sample_PDFs/" + filelist[30])#Fehler: 3;4;5;6;7;8;9;10;13;14;15;19;20;21;22;23;24;26;27;28;29;30;...
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
meta = reader.metadata
a = 0
imagecounter = 0
#Probedaten:




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
    totalText = ""
    a1 = 0
    while a1 < (number_of_pages-1):
        page=reader.pages[a1]
        #print(page.extract_text())
        totalText += str(page.extract_text())
        a1+=1
        #print(len(page.images))
        #imagecounter += page.images
    print(totalText)
#extracting()


def getData():
    #for files in filelist:
        reader = PdfReader("Sample_PDFs/" + filelist[0])

        page=reader.pages[0]
        site = page.extract_text()
        pagetext = str(site)
        lines = pagetext.splitlines()
        pagetext = ""
        for line in lines:
            flagletter = False
            for letter in line:
                if letter.isalpha():#prüft, ob Buchstabe in Zeile
                    flagletter = True
            if not flagletter:
                lines.remove(line) #löscht leere zeilen
            else:
                pagetext += line + "\n"
        #print(pagetext)
        title = site.split("Bachelorarbeit")
        #print(pagetext)
        print(title[0])
        for line in lines:
            if "von" in line and len(line)<5: #get Author; funktioniert nur, wenn es eine gewisse Formatierung gibt
                nextline = lines[lines.index(line)+1]
                index = 0
                # while index < len(nextline):
                #     if letter.isalpha:
                #         author = nextline
                #     index += 1
                #     if author != "":
                #         print(author)
                #         index = len(nextline)
                #     if index == len(nextline):
                #         if author == "":
                #             nextline = lines[lines.index(line)+1]
                #             index = 0
                    

#                print(lines[lines.index(line)+1]) #funktioniert nur bei bestimmten Layout
#                author = lines[lines.index(line)+1]
#                print(author)
        #title = pagetext.split("Bachelorarbeit")
        #author = title[0].split("von")
        #author = author[0].split("eingereicht am")
        #print("Titel: " + title[0])
        #print("Von : " + author[0])
        #date = author[0].split("Matrikelnummer")
        #print("Einreichedatum: " + date[0])
        #print(len(page.images))
        #imagecounter += page.images
getData()
def isname(name): #prüde, ob eingegebener String ein Name ist
    namebool = False
    name = str(name)
    strings = name.split(" ")
    for names in strings:
        namecheck = NameDataset.search('Walter')
        print(namecheck)
    return namebool
#isname('Florian')
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
#imagebyMupdf()
        
    
#images()
#extracting()
#print("We have " + str(imagecounter) + " Images." )

#print(text)