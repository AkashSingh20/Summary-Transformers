#av to text, failed
# doesnt work

import pyttsx3
import moviepy.editor as mp
import speech_recognition as sr
engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 3
        audio = r.listen(source, phrase_time_limit=3)


    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Command: {query}\n")

    except Exception as e:
            
        speak("Sorry! i cannot understant you. ")  
        return "None"
    return query

def vidtoaudio():
    clip = mp.VideoFileClip(r"Video File")
    clip.audio.write_audiofile(r"Audio File")

if __name__=="__main__":
    while True:
        query=takeCommand().lower()