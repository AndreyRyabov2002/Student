'''import sqlite3
import telebot
from telethon import TelegramClient
bot = telebot.TeleBot("5457646039:AAGJfExqkSzflrYfIjMTsszsJYJquYSeE-E")
api_id =14123444
api_hash = "ecab1808dbe1520bd8e1f165779ec9ef"
client = TelegramClient('bot_test', api_id, api_hash)


conn = sqlite3.connect('database.db', check_same_thread=False)
cursor = conn.cursor()


def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
	cursor.execute('INSERT INTO botik (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
				   (user_id, user_name, user_surname, username))
	conn.commit()


@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, 'Напиши "привет"')




@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text.lower() == 'привет':
		bot.send_message(message.chat.id, 'Что бы посмотреть базу данных, напиши "бд"')

		us_id = message.from_user.id
		us_name = message.from_user.first_name
		us_sname = message.from_user.last_name
		username = message.from_user.username

		db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

	elif message.text == 'бд':
         file = open('database.db', 'rb')
         bot.send_document(message.chat.id, file)



bot.infinity_polling()
'''