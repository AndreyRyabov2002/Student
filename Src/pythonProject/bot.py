import sqlite3
import telebot
from telethon import TelegramClient

bot = telebot.TeleBot("5457646039:AAGJfExqkSzflrYfIjMTsszsJYJquYSeE-E")
api_id =14123444
api_hash = "ecab1808dbe1520bd8e1f165779ec9ef"
client = TelegramClient('bot', api_id, api_hash)

@bot.message_handler(commands=['start'])
def start(message):
	connect = sqlite3.connect('users_db')
	cursor = connect.cursor()

	cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
		id INTEGER 
		username TEXT
	)""")

	connect.commit()

	#check id in fields
	people_id = message.chat.id
	cursor.execute(f"SELECT id FROM login_id WHERE id = {people_id}")
	data = cursor.fetchone()
	if data is None:

		users_list = [message.chat.id]
		cursor.execute("INSERT INTO login_id VALUES(?);", users_list)
		connect.commit()
	else:
		bot.send_message(message.chat.id, 'Такой пользователь уже существует.')



@bot.message_handler(commands=['delete'])
def delete(message):
	pass

bot.infinity_polling()

conn = sqlite3.connect("database2.db.db")
cursor = conn.cursor()
cursor.execute("""
               SELECT botik2.username
               FROM botik2, language, user_language
               WHERE (user.id = user_language.user_id AND
               language.id = user_language.language_id)
                """).fetchall()