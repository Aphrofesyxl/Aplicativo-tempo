import requests

API_KEY = '00e8da6ffe221e5e84ca0b620d65d8c7'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

city = input('Enter a city name: ')
request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print(weather)
    temperature = round(data['main']['temp'] - 273.15)
    
    print('Weather:', weather)
    print('Temperature:', temperature, 'celsius')
else:
    print('An error occurred.')
