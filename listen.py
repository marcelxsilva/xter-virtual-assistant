import speech_recognition as sr
import os
from gtts import gTTS
from pygame import mixer


def say(message):
	tts = gTTS(message, lang='pt-BR')
	tts.save("msg.mp3")

	mixer.init()
	mixer.music.load('msg.mp3')
	mixer.music.play()
	os.popen('rm -rf msg.mp3')

def listen():
	
	#enable microphone
	microphone = sr.Recognizer()
	with sr.Microphone() as source:
		#noise reduction
		microphone.adjust_for_ambient_noise(source)

		# print("Say something: ")
		#save audio
		audio = microphone.listen(source)

	try:
		#speech recognition
		command = microphone.recognize_google(audio,language='pt-BR')

		if command == 'Bom dia':
			say('Olá, Marcelo. bom dia. estou preparando o seu ambiente de trabalho, voce possui 3 projetos para hoje, e duas reuniões.')
			os.popen('code /Users/marcelxsilva/Documents/projects/dpsp-covid-appointments')

		# print("You say: " + command)
		listen()

	except:
		listen()
		return

	return
	
listen()