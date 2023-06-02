from tkinter import *
import ttkbootstrap as ttk
import speech_recognition as sr
import time
import datetime
import openai
from pydub import AudioSegment
import os
import winsound
import config

openai.api_key = config.OPENAI_API_KEY
messages = []
# Speach to text -- this should be asynchronous
def speak(text):
    voice = 'en-US-GuyNeural'
    command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "data.mp3" --write-subtitles=x'
    os.system(command)
    src = "data.mp3"
    dst = "data.wav"
    audio = AudioSegment.from_mp3(src)
    audio.export(dst, format="wav")

    winsound.PlaySound("data.wav", winsound.SND_ASYNC)
# Clear old data from the windows
def clearwindow():
    try:
        question.destroy()
        answer.destroy()
        welcome.destroy()
        chat_question.destroy()
        chat_answer.destroy()
    finally:
        return
# Shut down - verbally or via a button
def shut_down():
    speak("Shutting down, Thank you for using H3X - Take Care, Good Bye.")
    time.sleep(6)
    exit(0)
# Opening introduction of the ChatBot
def wishme():
    global welcome
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        text = "Good Morning. I am H3X. How can I Help you?"
    elif 12 <= hour < 18:
        text = "Good Afternoon. I am H3X. How can I Help you?"
    else:
        text = "Good Evening. I am H3X. How can I Help you?"

    welcome = ttk.Label(answer_frame, text=text, width=50, font=('Candara Light', -15, 'bold italic'))
    welcome.pack(pady=5, side=TOP, anchor="w")
    speak(text)
# This is the OpenAI ChatGPT module:
def takecommand():
    global chat_question
    global chat_answer
# Clear before input
    clearwindow()
    # Listen on microphone
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        speak("I am listening.")
        time.sleep(2)
        print("\nListening ..................................")
        audio = rec.listen(source, timeout=4, phrase_time_limit=4)
    try:
        message = rec.recognize_google(audio, language='en-in')
        if 'shutdown' in message or 'quit' in message or 'stop' in message or 'goodbye' in message:
            shut_down()

        else:
            chat_question = ttk.Label(question_frame, text=message, width=50, font=('congenial', -15, 'bold italic'), wraplength=300,)
            chat_question.pack(pady=5, side=TOP, anchor="w")

            # frame2 = Label(text=message, width=50, font=('fixedsys', -15, 'bold italic'))
            # frame2.grid(row=0, column=1, pady=5, padx=5)

            print("User: " + message)
            print("Processing......")
# ChatGPT specific data
            messages.append({"role": "user", "content": message})
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.5,
                max_tokens=500,
            )
            reply = chat.choices[0].message.content
            messages.append({"role": "assistant", "content": reply})
            chat_answer = ttk.Label(answer_frame, text=reply, width=50, font=('congenial', -15, 'bold italic'), wraplength=300,)
            chat_answer.pack(pady=5, side=TOP, anchor="w")

            speak(reply)

    except Exception as e:
        print(e)
        speak("Say that again please")
        return "None"

# this is the GUI Window
window = ttk.Window(themename="yeti")
window.title("Intelligent Chatbot")
window.geometry("1400x600")
window.resizable(width=False, height=False)
left_frame = ttk.Frame(window)
right_frame = ttk.Frame(window)

# Two Frames within the window
left_frame.place(x=0, y=0, relwidth=.5, relheight=1)
right_frame.place(relx=.5,  y=0, relwidth=.5, relheight=1)

# This is the start of the left frame:
image1 = PhotoImage(file="button-green.png")
image2 = PhotoImage(file="NewBot.png")

image_frame = ttk.Frame(left_frame)
img = ttk.Label(image_frame, image=image2)
img.image = image2

question_Button = ttk.Button(left_frame, text="Ask Me A Question!", command=takecommand)
question_Button.image = image1
# Configure the layout and placement of widgets in the left frame
left_frame.columnconfigure((0, 1, 2), weight=1, uniform="a")
left_frame.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")

image_frame.grid(row=0, column=0, rowspan=3, columnspan=3, sticky='nsew')
img.pack()

question_Button.grid(row=4, column=1, sticky='nsew')

# This is the start of the right frame:

# Audible input will be taken on this top block
question_frame = ttk.Labelframe(right_frame, borderwidth=5,  padding=5, bootstyle="dark")
question = ttk.Label(question_frame )

#Audible answers will be delivered in this bottom block:
answer_frame = ttk.Labelframe(right_frame,  borderwidth=5,  padding=5,  bootstyle="info")
answer = ttk.Label(answer_frame)

reset_button = ttk.Button(right_frame, text="Reset", command=clearwindow)

close_button = ttk.Button(right_frame, text="Close", command=shut_down)

# Configure the layout and placement of widgets in the right frame
right_frame.rowconfigure((0, 1, 2), weight=1, uniform="a")
right_frame.columnconfigure(0,  weight=1, uniform="a")

question_frame.grid(row=0, column=0, rowspan=1,  sticky='nsew')
question.pack()

answer_frame.grid(row=1, column=0, rowspan=2, columnspan=1, sticky='nsew')
answer.pack()

reset_button.place(relx=0.4, rely=0.95, anchor='center')
close_button.place(relx=0.6, rely=0.95, anchor='center')

# Run
wishme()
window.mainloop()
