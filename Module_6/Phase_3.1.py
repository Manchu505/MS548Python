import cv2
import speech_recognition as sr
import os
import datetime
from pydub import AudioSegment
from pydub.playback import play




recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "cascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
eyeCascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')
font = cv2.FONT_HERSHEY_SIMPLEX

id = 0

def voice_input():
    while True:
        # if count == 0:
        with sr.Microphone() as source:
            rec = sr.Recognizer()
            rec.adjust_for_ambient_noise(source)
            audio = rec.listen(source)

        try:
            message = rec.recognize_google(audio, language='en-in')
            if message.lower() == "exit":
                print("\nGoodbye!")
                speak("Goodbye")
                # exit()
                exit_program()

            elif message.lower() == "start over":
                print("Starting Over?")
                speak("Starting Over")
                os.system("pause")

            elif message.lower() == "start chat":
                print("Starting ChatBot...........................")
                speak("Starting Chatbot")
                os.system("pause")

            else:
                print("Try again!")
                print("\nListening ..................................")

        except sr.UnknownValueError:
            print("Please say that again ")

def speak(text):
    voice = 'en-US-GuyNeural'
    command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "data.mp3" --write-subtitles=x'
    os.system(command)
    audio = AudioSegment.from_mp3("data.mp3")
    play(audio)

def recognized():
    now = datetime.datetime.now()
    hour = now.hour
    print('hello ' + id)
    if hour < 12:
        speak("good morning " + id)
    elif hour < 18:
        speak("good afternoon" + id)
    else:
        speak("good evening" + id)

    voice_input()
    exit_program()
    # exit()

def unrecognized():
    now = datetime.datetime.now()
    hour = now.hour
    print('I am sorry I do not recognised you!')
    if hour < 12:
        speak("good morning welcome to HEX SHIELD, I am sorry I do not recognize you -- Please press any key to try again.  ")
    elif hour < 18:
        speak("good afternoon welcome to HEX SHIELD I am sorry I do not recognize you -- Please press any key to try again.  ")
    else:
        speak("good evening welcome to HEX SHIELD I am sorry I do not recognize you -- Please press any key to try again.  ")
    os.system('pause')

def exit_program():
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()
    exit()



# names related to ids: example ==> Grant: id=1,  etc
names = ['None', 'Grant', 'Hayley', 'Darwin', 'Grant1', 'Grant2']

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # set video width
cam.set(4, 480)  # set video height

# Define min window size to be recognized as a face
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)

while True:

    ret, img = cam.read()

    count = 0
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )

    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

        # Check if confidence is less them 100 ==> "0" is perfect match
        if (confidence < 73):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
            count = count + 1
        else:
            id = "unknown"
            count = 0
        cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)


    cv2.imshow('camera', img)


    if id == "Grant":
        recognized()
    elif id == "Hayley":
        recognized()
    elif id == "Darwin":
        recognized()
    elif id == "unknown":
        unrecognized()


    k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
    if k == 27:
        exit_program()
