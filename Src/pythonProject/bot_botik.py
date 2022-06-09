from telethon import TelegramClient, events

api_id =14123444
api_hash = "ecab1808dbe1520bd8e1f165779ec9ef"
client = TelegramClient('botok', api_id, api_hash)


@client.on(events.NewMessage(chats=('@messagestatistics2399bot')))
async def normal_handler(event):
#    print(event.message)
    print(event.message.to_dict()['message'])


client.start()
client.run_until_disconnected()