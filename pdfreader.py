
@author: Karthik
"""

import pyttsx3
import PyPDF2  # Correct module name

def speak(text):
    speaker = pyttsx3.init()
    speaker.setProperty('rate', 200)  # Adjust speed if needed
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[1].id)  # Female voice
    speaker.say(text)
    speaker.runAndWait()

def read_pdf(file_path):
    try:
        with open(file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                if text:
                    print(f"Reading page {page_num + 1}...")
                    speak(text)
                else:
                    print(f"Page {page_num + 1} has no readable text.")
                    
    except Exception as e:
        print(f"An error occurred: {e}")
        speak("Sorry, I couldn't read the PDF file.")

if __name__ == "__main__":
    pdf_file_path = r"[your pdf with .pdf extension that must be on desktop]"  
    read_pdf(pdf_file_path)
