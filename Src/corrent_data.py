import requests

headers = {
    "User-Agent": "LSKLDS"
    }

#url = 'http://worldtimeapi.org/api/timezone/Europe/Kirov'
response = requests.get('http://worldtimeapi.org/api/timezone/Europe/Kirov', headers=headers)

print(response.json()['datetime'])
#print(response.datetime,'datetime')
#print(response.json(),'json')
#print(response.content,'content')
