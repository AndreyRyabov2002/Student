'''from telethon.sync import TelegramClient


api_id = 14123444
api_hash = "ecab1808dbe1520bd8e1f165779ec9ef"
username = "messagestatistics2399bot"


client = TelegramClient(phone, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

print('Fetching Members...')
all_participants = []
all_participants = client.get_participants(my_chat_id, aggressive=True)
'''