# comments: Grant Stoebner, Module #1, 15hrs, 8hrs.
import whisper
import datetime
from textblob import TextBlob
from tkinter import *
from tkinter import filedialog

def saveFile():
    savefile = input("\nWould you like to save (Y/n): ").upper()
        
    if savefile == "Y":
        original = input("\nWould you like to save the original or corrected copy?: \n[1] Original \n[2] Corrected Version\nPlease choose: ")    
       
        if original == "1":
            file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[("Text File", ".txt"),("Word", ".doc"), ("All files", ".*"),])
            file.write(result["text"])
            file.close
 
        else:
            file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[("Text File", ".txt"),("Word", ".doc"), ("All files", ".*"),])
            file.write(spellCorrect)
            file.close
    else:
        exit

# Greeting on Open
now = datetime.datetime.now()
hour = now.hour

if hour < 12:
    greeting = "Good morning"
elif hour < 18:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"

print("{}!".format(greeting))

print("\nWhat would you like to do today? \n[1] Open an audio File: \n[2] Open a text file:\n[3] Exit: ")
selection = input("Please make your selection: ")

if selection == "1":
    audiopath = filedialog.askopenfilename(title="Select Audio File", filetypes= (("Audio Files", ["*.wav", "*.m4a", "*.mp3","*.mp4"]),("All Files", "*.*")))
    #audio.mainloop()
    
    model = whisper.load_model("base")
    result = model.transcribe(audiopath)
    print(result["text"])
    
    spellCheck = input("\nWould you like to spellcheck (Y/n): ").upper()
    
    if spellCheck == "Y":
        spellaudio = TextBlob(result["text"])
        spellCorrect = str(spellaudio.correct())
        print(spellCorrect)
        saveFile()
    else:
        saveFile()

elif selection == "2":
    textpath = filedialog.askopenfilename(title="Select Text File", filetypes= (("Text File", ["*.txt", "*.doc", "*.docx"]),("All Files", "*.*")))
    #text.mainloop()
    
    file = open(textpath)
    tb=file.read()
    print("\nFile Loaded! ")
   # print(type(tb))
    tCheck = TextBlob(tb)
    file.close()
    
    spellCheck = input("\nWould you like to spellcheck (Y/n): ").upper()
    
    if spellCheck == "Y":
        spellText = str(tCheck.correct)
        print(spellText)
        textSave = input("\nWould you like to save the new text? (Y/n): ").upper()
        if textSave == "Y":
            newfile = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[("Text File", ".txt"),("Word", ".doc"), ("All files", ".*"),])
            newfile.write(spellText)
            newfile.close
        #saveFile()
    else:
        exit 
        #saveFile()

else:
    exit    



