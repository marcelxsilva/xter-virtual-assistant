import speech_recognition as sr
import os
import services


def run():

    # enable microphone
    microphone = sr.Recognizer()
    with sr.Microphone() as source:
        # noise reduction
        microphone.adjust_for_ambient_noise(source)
        audio = microphone.listen(source)
    try:
        # speech recognition
        services.identifyCommand(
            microphone.recognize_google(audio, language='pt-BR'))
        run()
    except:
        run()


run()
