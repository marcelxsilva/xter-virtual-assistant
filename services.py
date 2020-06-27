from pygame import mixer
from gtts import gTTS
import json
import os


def say(message):
    tts = gTTS(message, lang='pt-BR')
    tts.save("msg.mp3")

    mixer.init()
    mixer.music.load('msg.mp3')
    mixer.music.play()
    os.popen('rm -rf msg.mp3')


def run(command):
    os.popen(command)


def identifyCommand(phrase):
    file = open('commands.json')

    data = json.load(file)
    for i in data:
        if i["phrase"].lower() == phrase.lower():
            say(i["message"])
            run(os.popen(i["command"]))
    file.close()
