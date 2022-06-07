import telebot

bot = telebot.TeleBot("5457646039:AAGJfExqkSzflrYfIjMTsszsJYJquYSeE-E")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()