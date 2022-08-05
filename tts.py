import pyttsx3 as tts

def text_to_speech(a):
    engine = tts.init()
    newVoiceRate = 120
    engine.setProperty('rate', newVoiceRate)
    engine.say(a)
    engine.runAndWait()


