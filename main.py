from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging

logging.basicConfig(filename = 'archivarlog.log', level = logging.DEBUG)

Bot = ChatBot("JaretBot")

Entrenador = ChatterBotCorpusTrainer(Bot)

Entrenador.train('chatterbot.corpus.spanish')

while True:
    solicitud = input("Yo: ")
    respuesta = Bot.get_response(solicitud)
    print("JaretBot: ", respuesta)
