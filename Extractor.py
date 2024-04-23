from PyPDF2 import PdfReader
reader = PdfReader("160907_Bachelorarbeit_Sebastian Sperl.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
meta = reader.metadata

print(len(reader.pages))

# All of the following could be None!
print("Author = " +meta.author)
print("creator = " + meta.creator)
print("producer =" + meta.producer)
print("subject = "+meta.subject)
print("title = " +meta.title)
print("Seitenzahl = " + str(number_of_pages))
print("Text: ")
file = page
a = 1
while a < number_of_pages:
    page=reader.pages[a]
    print(page.extract_text())
    a+=1
    
#print(text)