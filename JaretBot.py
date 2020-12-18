import telebot
from chatterbot import ChatBot

bot = telebot.TeleBot("1307350389:AAEHB1gnJ7wkFv8M1azlU8ThvWYDzu7q5GM")

# Usare el bot personal para la conversacion
def bot_conversacion(message):

    Bot = ChatBot("JaretBot", trainer = "chatterbot.trainers.ChatterBotCorpusTrainer")
    respuesta = Bot.get_response(message)
    respuesta = str(respuesta)

    mensajes = open("respuesta.txt", "w")
    mensajes.write(respuesta)
    mensajes.close()

# Se envia y se recibe una respueta al comando /start o /ayuda
# Se utiliza el decorador(@) para darle funcionalidad al bot junto a la funcion message_handler
@bot.message_handler(commands =["ayuda", "start"])
def enviar(message):
    bot.reply_to(message, "hola soy JaretBot, estoy para servirte")

# Recibimos cualquier otro mensaje
@bot.message_handler(func=lambda message: True)
def mensaje(message):
    bot_conversacion(message.text)
    respuesta = open("respuesta.txt", "r")
    respuesta = respuesta.read()
    bot.reply_to(message, respuesta)

bot.polling()