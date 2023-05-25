import speech_recognition as sr
import openai
import os
import textwrap
import config
from pydub import AudioSegment
from pydub.playback import play

openai.api_key = config.OPENAI_API_KEY

messages = []


def maleTone():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nHi my name is Chris - to start Please set the Tone for your ChatBot .")
        voice1 = 'en-US-ChristopherNeural'
        maletone = f'edge-tts --voice "{voice1}" --text "Hi my name is Chris - to start Please set the Tone for your ChatBot ." --write-media "data.mp3" --write-subtitles=x'
        os.system(maletone)
        tone = AudioSegment.from_mp3("data.mp3")
        play(tone)
        # rec.pause_threshold = 3
        print("\nListening ..................................")
        audio = rec.listen(source)

    try:
        assistant = rec.recognize_google(audio, language='en-in')
        if assistant.lower() == "exit":
            print("Goodbye!")
            exit()
        elif assistant.lower() == "start over":
            print("Starting Over?")
            voice2 = 'en-US-ChristopherNeural'
            maletone = f'edge-tts --voice "{voice2}" --text "Starting over!" --write-media "data.mp3" --write-subtitles=x'
            os.system(maletone)
            tone = AudioSegment.from_mp3("data.mp3")
            play(tone)
            welcome()
        else:
            messages.append({"role": "system", "content": assistant})
            print("\nProcessing......")
            print("\nYour new '" + assistant + "' assistant is ready!\n Say 'exit' to leave the chat!'")
            print("\n How can I help you today?")
            voice2 = 'en-US-ChristopherNeural'
            maletone = f'edge-tts --voice "{voice2}" --text "How can I help you today?" --write-media "data.mp3" --write-subtitles=x'
            os.system(maletone)
            try:
                song = AudioSegment.from_mp3("data.mp3")
                play(song)

            except Exception as e:
                print(e)

    except Exception as e:
            print("say that again please")

    while True:
        rec = sr.Recognizer()
        with sr.Microphone() as source:
            # rec.pause_threshold = 3
            print("\nListening ..................................")
            audio = rec.listen(source)
        try:
            message = rec.recognize_google(audio, language='en-in')

            if message.lower() == "exit":
                print("\nGoodbye!")
                exit()
            elif message.lower() == "start over":
                print("Starting Over?")
                voice2 = 'en-US-ChristopherNeural'
                maletone = f'edge-tts --voice "{voice2}" --text "Starting over!" --write-media "data.mp3" --write-subtitles=x'
                os.system(maletone)
                tone = AudioSegment.from_mp3("data.mp3")
                play(tone)
                welcome()
            else:
                print("User: " + message)
                print("Processing......")
                messages.append({"role": "user", "content": message})
                chat = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                    temperature=0.5,
                    max_tokens=500,
                )
                reply = chat.choices[0].message.content
                messages.append({"role": "assistant", "content": reply})
                print("\nChatBot : ---------------------------------------------\n")
                wrapper = textwrap.TextWrapper(width=80)
                replyOutput = wrapper.wrap(text=reply)
                for element in replyOutput:
                    print(element)
                voice = 'en-US-ChristopherNeural'
                command = f'edge-tts --voice "{voice}" --text "{reply}" --write-media "data.mp3" --write-subtitles=x'
                os.system(command)

                try:
                    song = AudioSegment.from_mp3("data.mp3")
                    play(song)

                except Exception as e:
                    print(e)

        except Exception as e:
         print("say that again please")

def femaleTone():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nHi my name is Michelle - to start Please set the Tone for your ChatBot .")
        voice2 = 'en-US-JennyNeural'
        femaletone = f'edge-tts --voice "{voice2}" --text "Hi my name is Michelle - to start Please set the Tone for your ChatBot ." --write-media "data.mp3" --write-subtitles=x'
        os.system(femaletone)
        tone = AudioSegment.from_mp3("data.mp3")
        play(tone)
        # rec.pause_threshold = 3
        print("\nListening ..................................")
        audio = rec.listen(source)

    try:
        assistant = rec.recognize_google(audio, language='en-in')
        if assistant.lower() == "exit":
            print("Goodbye!")
            welcome()
            # exit()


        elif assistant.lower() == "start over":
            print("Starting Over?")
            voice2 = 'en-US-JennyNeural'
            femaletone = f'edge-tts --voice "{voice2}" --text "Starting over!" --write-media "data.mp3" --write-subtitles=x'
            os.system(femaletone)
            tone = AudioSegment.from_mp3("data.mp3")
            play(tone)
            welcome()

        else:
            messages.append({"role": "system", "content": assistant})
            print("\nProcessing......")
            print("\nYour new '" + assistant + "' assistant is ready!\n Say 'exit' to leave the chat!'")
            print("\n How can I help you today?")
            voice2 = 'en-US-JennyNeural'
            femaletone = f'edge-tts --voice "{voice2}" --text "How can I help you today?" --write-media "data.mp3" --write-subtitles=x'
            os.system(femaletone)
            tone = AudioSegment.from_mp3("data.mp3")
            play(tone)

    except Exception as e:
        print("say that again please")

    while True:
        rec = sr.Recognizer()
        with sr.Microphone() as source:
            # rec.pause_threshold = 3
            print("\nListening ..................................")
            audio = rec.listen(source)
        try:
            message = rec.recognize_google(audio, language='en-in')

            if message.lower() == "exit":
                print("\nGoodbye!")
                exit()
            elif message.lower() == "start over":
                print("Starting Over?")
                voice2 = 'en-US-JennyNeural'
                femaletone = f'edge-tts --voice "{voice2}" --text "Starting over!" --write-media "data.mp3" --write-subtitles=x'
                os.system(femaletone)
                tone = AudioSegment.from_mp3("data.mp3")
                play(tone)
                welcome()

            else:
                print("User: " + message)
                print("Processing......")
                messages.append({"role": "user", "content": message})
                chat = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                    temperature=0.5,
                    max_tokens=500,
                )
                reply = chat.choices[0].message.content
                messages.append({"role": "assistant", "content": reply})
                print("\nChatBot : ---------------------------------------------\n")
                wrapper = textwrap.TextWrapper(width=80)
                replyOutput = wrapper.wrap(text=reply)
                for element in replyOutput:
                    print(element)
                voice = 'en-US-JennyNeural'
                command = f'edge-tts --voice "{voice}" --text "{reply}" --write-media "data.mp3" --write-subtitles=x'
                os.system(command)

                try:
                    song = AudioSegment.from_mp3("data.mp3")
                    play(song)

                except Exception as e:
                    print(e)

        except Exception as e:
            print("say that again please")

def welcome():

    print("\nWelcome Back!")
    voice = 'en-US-GuyNeural'
    welcome = f'edge-tts --voice "{voice}" --text "Welcome Back" --write-media "data.mp3" --write-subtitles=x'
    os.system(welcome)
    try:
        song = AudioSegment.from_mp3("data.mp3")
        play(song)

    except Exception as e:
        print(e)

    print("\nWould you like to talk to Chris or Michelle?")
    voice1 = 'en-US-GuyNeural'
    voice2 = 'en-NZ-MollyNeural'
    malevoice = f'edge-tts --voice "{voice1}" --text "Would you like to talk to Chris" --write-media "data.mp3" --write-subtitles=x'
    femalevoice = f'edge-tts --voice "{voice2}" --text "or Michelle?" --write-media "data1.mp3" --write-subtitles=x'
    os.system(malevoice)
    os.system(femalevoice)
    try:
        audio1 = AudioSegment.from_file("data.mp3")
        audio2 = AudioSegment.from_file("data1.mp3")
        combined = audio1.append(audio2)
        play(combined)
        print("\nListening ..................................")
    except Exception as e:
        print(e)
        print("\nListening ..................................")


    while True:
        rec = sr.Recognizer()
        with sr.Microphone() as source:
            #rec.pause_threshold = 3
            audio = rec.listen(source)

        try:
            print("Processing.................")
            voiceselect = rec.recognize_google(audio, language='en-in')

            if voiceselect.lower() == "exit":
                print("\nGoodbye!")
                exit()

            elif voiceselect.lower() == "chris":
                voice1 = 'en-US-GuyNeural'
                malevoice = f'edge-tts --voice "{voice1}" --text "You will be transfered to Chris" --write-media "data.mp3" --write-subtitles=x'
                os.system(malevoice)
                voiceselect = AudioSegment.from_mp3("data.mp3")
                play(voiceselect)
                maleTone()

            elif voiceselect.lower() == "michelle":
                voice2 = 'en-NZ-MollyNeural'
                femalevoice = f'edge-tts --voice "{voice2}" --text "You will be transfered to Michelle" --write-media "data.mp3" --write-subtitles=x'
                os.system(femalevoice)
                voiceselect = AudioSegment.from_mp3("data.mp3")
                play(voiceselect)
                femaleTone()

            else:
                print("Try again!")
                print("\nListening ..................................")

        except Exception as e:
            print('An error has occurred: ')
            print("\nListening ..................................")


welcome()
