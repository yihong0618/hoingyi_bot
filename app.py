from config import TOKEN
import telebot

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "hello":
        bot.reply_to(message, "fuckyou")
    bot.reply_to(message, message.text)

bot.polling()
