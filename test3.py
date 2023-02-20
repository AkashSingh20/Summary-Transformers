# basic google audio to text
import os
import speech_recognition as sr
from os import path
from pydub import AudioSegment

command2mp3 = "ffmpeg -i conan.mp4 conan.mp3"
command2wav = "ffmpeg -i conan.mp3 conan.wav"

os.system(command2mp3)
os.system(command2wav)

AUDIO_FILE = "conan.wav"
r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)                 

        print("Transcription: " + r.recognize_google(audio))