from pyttsx3 import voice

import linkgen,sel
import speech_recognition as sr
import cv2
import word_lib
from googletrans import Translator
import pyttsx3 as tts
import tts
translator = Translator()
# create the recognizer
r = sr.Recognizer()

# define the microphone
mic = sr.Microphone(device_index=0)

print("Start speaking")

# record your speech
with mic as source:
    print("start now")
    audio = r.listen(source,phrase_time_limit=3)
    print("stop now")


try:
    result = r.recognize_google(audio)
except sr.RequestError:
    # API was unreachable or unresponsive
    exit("API is unreachable")
# except KeyboardInterrupt:
#     print("Audio Recorded")
except sr.UnknownValueError:
    # speech was unintelligible
    exit("Unable to recognize speech! Were you speaking")

# speech recognition
result = r.recognize_google(audio)

# export the result
print(result)
with open('my_speech.txt', mode='w') as file:
    file.write(result)

print("The audio has been stored.")

link=linkgen.link(result)
sel=sel.sel(link)
print(sel)
sansglish = word_lib.words_change(sel)
tts.text_to_speech(sansglish)
translator.detect(sel)
#playsound in sanskrit
