import speech_recognition as sr
import openai
from elevenlabs import set_api_key
from elevenlabs import generate, play
import textwrap
import config

openai.api_key = config.OPENAI_API_KEY
set_api_key(config.ELEVENLABS_API_KEY)


messages = []
rec = sr.Recognizer()
# use the microphone on the computer to listen to your voice
with sr.Microphone() as source:
    print("What type of ChatBot would you like to create?")
    # if the user doesn't speak within 3 seconds the mic will stop listening
    rec.pause_threshold = 3
    # records the user speaking to a variable
    audio = rec.listen(source)
# try and except statements for error handling
try:
    # If voice is recognized it relays to the user it is processing

    # it will translate the audio variable into english and hold in text variable
    assistant = rec.recognize_google(audio, language='en-in')

    if assistant.lower() == "exit":
        print("Goodbye!")
        exit()
    else:
        messages.append({"role": "system", "content": assistant})

except Exception as e:
    # if some problem occurred than this message will be shown
    print("say that again please")

# system_msg = input("What type of ChatBot would you like to create?: ")
print("Processing......")
print("Your new '" + assistant + "' assistant is ready!\n Type 'exit' to leave the chat!'")


# def main():
while True:
    rec = sr.Recognizer()
    # use the microphone on the computer to listen to your voice
    with sr.Microphone() as source:
        print("\nWhat would you like to know?")
        # if the user doesn't speak within 3 seconds the mic will stop listening
        # rec.pause_threshold = 3
        # records the user speaking to a variable
        audio = rec.listen(source)
    # try and except statements for error handling
    try:
        # If voice is recognized it relays to the user it is processing

        # it will translate the audio variable into english and hold in text variable
        message = rec.recognize_google(audio, language='en-in')

        if message.lower() == "exit":
            print("\nGoodbye!")
            exit()
        else:
            print("User: " + message)
            print("Processing......")
            messages.append({"role": "user", "content": message})
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.5,
                max_tokens=100,
            )
            reply = chat.choices[0].message.content
            # response["choice"] [0] ["message"] ["content"]
            messages.append({"role": "assistant", "content": reply})
            print("\nChatBot : ---------------------------------------------\n")
            wrapper = textwrap.TextWrapper(width=80)
            replyOutput = wrapper.wrap(text=reply)
            for element in replyOutput:
                print(element)
            audio = generate(
                text=reply,
                voice="Domi",
                model="eleven_monolingual_v1"
            )
            play(audio)
    except Exception as e:
        print("An error has occurred: {}".format(e))

# try:
    #     message = input("User: ")
    #     if message.lower() == "exit":
    #         print("Goodbye!")
    #         exit()
    #     else:
    #         messages.append({"role": "user", "content": message})
    #         chat = openai.ChatCompletion.create(
    #             model="gpt-3.5-turbo",
    #             messages=messages,
    #             temperature=0.5,
    #             max_tokens=100,
    #         )
    #     reply = chat.choices[0].message.content
    #     response["choice"] [0] ["message"] ["content"]
        # messages.append({"role": "assistant", "content": reply})
        # print("\nChatBot : ---------------------------------------------\n" + reply + "\n")
        # audio = generate(
        #     text=reply,
        #     voice="Domi",
        #     model="eleven_monolingual_v1"
        # )
        # play(audio)
    # except Exception as e:
    #     print("An error has occurred: {}".format(e))
