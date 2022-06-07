import requests

url = 'http://worldtimeapi.org/api/timezone/Europe/Kirov'
response = requests.get(url)

print(response.text,'text')
#print(response.json(),'json')
#print(response.content,'content')
