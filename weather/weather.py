import requests
from pprint import pprint
from datetime import datetime
from conf import WEATHER_TOKEN


def get_weather(city, token):
    try:
        request = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid'
                               f'={token}&units=metric')
        data = request.json()
        # pprint(data)

        city = data['name']
        current_temp = data['main']['temp']
        current_feel = data['main']['feels_like']
        current_humidity = data['main']['humidity']
        current_pressure = data['main']['pressure']
        current_visibility = data['visibility'] / 1000
        sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.fromtimestamp(data['sys']['sunset'])
        return f'City: {city}\nTemp: {current_temp}C\nFeels like: {current_feel}C\n' \
               f'Humidity: {current_humidity}%\nPressure: {current_pressure}\n' \
               f'Visibility: {current_visibility}km\nSunrise: {sunrise}\nSunset: {sunset}\n'

    except:
        return f'Invalid city name!'


cit = "pattaya"
print(get_weather(cit, WEATHER_TOKEN))
