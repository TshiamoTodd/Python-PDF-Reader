import pyttsx3
import PyPDF2

path = "C:\\Users\\Tshiamo\\Desktop\\Desktop2.0\\NewDesk\\Python File Reader\\oop.pdf"
#PDF to read from
book = open(path, "rb")
pdfReader = PyPDF2.PdfFileReader(book)

#Get page to read from
page = pdfReader.getPage(0)
#pages = pdfReader.numPages
#print(pages)
#Extract text from book
text = page.extractText()
#Initialize pyttsx3
speaker = pyttsx3.init()

#Change speaking rate
rate = speaker.getProperty('rate')
print(rate)
#Set rate
speaker.setProperty('rate', 125)
#Set volume
speaker.setProperty('volume', 1.0)
#female voice
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[0].id)
#Read aloud the text
speaker.say(text)
speaker.runAndWait()