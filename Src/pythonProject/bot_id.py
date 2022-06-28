

import sqlite3
import telebot
from telethon import TelegramClient
from sqlite3 import Connection
bot = telebot.TeleBot("5457646039:AAGJfExqkSzflrYfIjMTsszsJYJquYSeE-E")
#api_id =14123444
#pi_hash = "ecab1808dbe1520bd8e1f165779ec9ef"
#client = TelegramClient('bot_test', api_id, api_hash)


conn = sqlite3.connect('database.db', check_same_thread=False)
cursor = conn.cursor()

user_messages = ""

def db_table_val(user_id: int, user_name: str, username: str, user_messages: int):
	cursor.execute('INSERT INTO botik (user_id, user_name, username, user_messages) VALUES (?, ?, ?, ?)',
					(user_id, user_name, username, user_messages))
	conn.commit()

def analytics(func: callable):

	user_messages = 0
	def analytics_wrapper(message):

		nonlocal user_messages
		user_messages += 1

		print("New message:", message.text, "Total message:", user_messages)
		return func(message)

	return analytics_wrapper

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, 'Напиши "привет"')




@bot.message_handler(content_types=['text'])
@analytics
def get_text_messages(message):
	if message.text.lower() == 'привет':
		bot.send_message(message.chat.id, 'Что бы посмотреть базу данных, напиши "бд"')

		us_id = message.from_user.id
		us_name = message.from_user.first_name
		username = message.from_user.username
		us_message = message.from_user.last_name

		db_table_val(user_id=us_id, user_name=us_name, username=username, user_messages=us_message)

	elif message.text == 'бд':
		file = open('database.db', 'rb')
		bot.send_document(message.chat.id, file)




bot.infinity_polling()