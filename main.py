from gtts import gTTS
from pypdf import PdfReader 
import os 
import tkinter as tk
from PIL import ImageTk as itk
from tkinter.filedialog import askopenfilename
import docx
import requests
def search():
    op_path = askopenfilename(parent=root,initialdir=r"/",
            title="Select Photo", filetypes=(("Photo files","*.pdf*; *.docx*"),("All Files","*.*")))
    split_tup = os.path.splitext(op_path)
    if split_tup[-1] == '.pdf':
        print("yesss")
        reader = PdfReader(f'{op_path}') 
        print("done")
        pages = reader.pages
        pages_list = [page.extract_text() for page in pages]
        pages_string = " ".join(str(element) for element in pages_list)    
        sound_result = gTTS(text=pages_string, lang=language, slow=False)
        sound_result.save("result.mp3")

    elif split_tup[-1] == ".docx":
        print("robie")
        print(op_path)
        doc = docx.Document(op_path)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
        docs_string = " ".join(str(element) for element in fullText)    
        sound_result = gTTS(text=docs_string, lang=language, slow=False)
        sound_result.save("result.mp3")


root = tk.Tk()
root.title("PDF to SPEECH CONVERTER")
root.geometry("750x350")
background_path = "background.png"
bg =tk.PhotoImage( file = r"background.png")
background_label = tk.Label( root, image = bg)
background_label.place(x = 0,y = 0)
l = tk.Label(root, text = "Choose file to speech convert", bg="gainsboro")
l.config(font =("Courier", 14))
l.place(x=235, y=30)
search_button = tk.Button(command=search, text="Choose File", bg="lavender blush", highlightthickness=0)
search_button.place(x=315, y=150, width=150, height=40)
language = 'pl'




tk.mainloop()