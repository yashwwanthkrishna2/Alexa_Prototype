import speech_recognition as sr 
import pywhatkit


def get_audio():
    recorder = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm Listening......")
        audio = recorder.listen(source)


    text = recorder.recognize_google(audio)
    print(f"You said: {text}")
    return text

text = get_audio()

if "youtube" in text.lower():
    pywhatkit.playonyt(text)
else:
    pywhatkit.search(text)