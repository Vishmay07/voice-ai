import pyttsx3
import speech_recognition as sr
import eel

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice' ,voices[0].id)
    engine.setProperty('rate',174)
    print(voices)
    engine.say(text)
    engine.runAndWait()
@eel.expose
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage('listening...')
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, timeout=15, phrase_time_limit=10)


    try:
        print("Recognizing...")
        eel.DisplayMessage('Recognizing...')
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
        eel.DisplayMessage(query)
        speak(query)
        eel.showHood()
    except Exception as e:
        return""
    
    return query.lower()
