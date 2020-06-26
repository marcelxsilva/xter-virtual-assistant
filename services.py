from gtts import gTTS
from pygame import mixer
import os

# this method performs the conversion of text to audio.
#  plays and then erases.


def say(message):
    tts = gTTS(message, lang='pt-BR')
    tts.save("msg.mp3")

    mixer.init()
    mixer.music.load('msg.mp3')
    mixer.music.play()
    os.popen('rm -rf msg.mp3')
